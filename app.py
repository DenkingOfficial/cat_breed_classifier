import gradio as gr
import numpy as np
import requests
import tensorflow as tf
from fastapi import FastAPI
from io import BytesIO
from PIL import Image
from pydantic import BaseModel
from cat_breeds_dict import CAT_BREEDS, CAT_DESCRIPTIONS
from scripts.crop_image import crop_image


class Url(BaseModel):
    link: str


MODEL = tf.keras.models.load_model('./models/cats_18_EfficientNetB0.h5')
GRADIO_PATH = '/'
INPUT_SHAPE = MODEL.layers[0].input_shape[1]
NUM_CLASSES = MODEL.layers[-1].output_shape[1]
app = FastAPI()


def predict(image, api_mode=False):
    image = crop_image(image, INPUT_SHAPE, INPUT_SHAPE)
    image = image.resize((INPUT_SHAPE, INPUT_SHAPE))
    image = np.asarray(image)
    image = image.reshape(1, INPUT_SHAPE, INPUT_SHAPE, 3)

    prediction = MODEL.predict(image)[0]
    predicted_breed = CAT_BREEDS[np.argmax(prediction)]
    breed_description = CAT_DESCRIPTIONS[predicted_breed]

    all_predictions = {
        CAT_BREEDS[i]: float(prediction[i]) for i in range(NUM_CLASSES)
        }

    if api_mode:
        breed_description = ' '.join(breed_description.replace('\n', '.')
                                                      .replace('#', '')
                                                      .split())

        return {
            'breed': predicted_breed,
            'description': breed_description,
            'predictions': all_predictions
            }
    return all_predictions, breed_description, gr.HTML.update(visible=True), gr.Markdown.update(visible=True)


@app.post('/predict_breed/')
def predict_api(url: Url):
    try:
        image = requests.get(url.link).content
    except Exception as e:
        return {'error': 'Invalid link', 'exception': str(e)}
    image = Image.open(BytesIO(image))
    return predict(image, api_mode=True)


with gr.Blocks(css='./static/style.css', title="Cat Classifier") as gradio_ui:

    gr.Markdown(
        """
        # Классификатор пород котов
        Разработано студентами Шершневым А.А, Онучиной М.К., Ивановым С.С, Шалаевой И.Г. и
        Ильиным С.С.
        Группы: РИМ-120906, РИМ-120907, РИМ-120908
        """,
        elem_id='md-text'
    )

    with gr.Row(elem_id='main-row') as row:

        with gr.Column(scale=2, elem_id='first-col') as col_1:
            user_image = gr.Image(
                label='Загрузите фотографию котика сюда',
                type='pil',
                elem_id='user-image'
            )
            predict_button = gr.Button(value='Определить породу')

        with gr.Column(scale=1, elem_id='second-col') as col_2:
            predicted_labels = gr.Label(
                num_top_classes=5,
                label='Результат определения породы',
                elem_id='predictions-text'
            )

    breed_description = gr.Markdown(elem_id='breed-description')
    banner_text = gr.Markdown(
        """
        # <center>Места, которые будут Вам интересны</center>
        """, visible=False
    )
    embedded_map = gr.HTML('''
    <iframe src="https://yandex.ru/map-widget/v1/?um=constructor%3A8cead4799165c7f6356c4f269f2847032ef2803cb46871dbfd6dd68c09834f4c&amp;source=constructor" width="100%" height="500" frameborder="0"></iframe>
    ''', visible=False, elem_id='embedded-map')

    predict_button.click(
        fn=predict,
        inputs=[user_image],
        outputs=[
            predicted_labels, breed_description,
            embedded_map, banner_text
            ]
    )

    app = gr.mount_gradio_app(app, gradio_ui, path=GRADIO_PATH)

import gradio as gr
import numpy as np
import requests
import tensorflow as tf
from fastapi import FastAPI
from io import BytesIO
from PIL import Image
from pydantic import BaseModel
from cat_breeds_dict import CAT_BREEDS, CAT_DESCRIPTIONS


class Url(BaseModel):
    link: str


MODEL = tf.keras.models.load_model('./models/20_cat_classes_model_v2.h5')
GRADIO_PATH = '/'

app = FastAPI()


def predict(image, api_mode=False):
    image = image.resize((128, 128))
    image = np.asarray(image)
    image = image.reshape(1, 128, 128, 3)

    prediction = MODEL.predict(image)[0]
    predicted_breed = CAT_BREEDS[np.argmax(prediction)]
    breed_description = CAT_DESCRIPTIONS[predicted_breed]

    all_predictions = {CAT_BREEDS[i]: float(prediction[i]) for i in range(20)}

    if api_mode:
        breed_description = ' '.join(breed_description.replace('\n', '.')
                                                      .replace('#', '')
                                                      .split())

        return {
            'breed': predicted_breed,
            'description': breed_description,
            'predictions': all_predictions
            }
    return all_predictions, breed_description


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
        Разработано студентами Шершневым А.А, Ивановым С.С, Шалаевой И.Г. и
        Ильиным С.С.
        Группы: РИМ-120906, РИМ-120907
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

    predict_button.click(
        fn=predict,
        inputs=[user_image],
        outputs=[predicted_labels, breed_description]
    )

    app = gr.mount_gradio_app(app, gradio_ui, path=GRADIO_PATH)

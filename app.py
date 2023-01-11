import gradio as gr
import tensorflow as tf
import numpy as np
from cat_breeds_dict import CAT_BREEDS, CAT_DESCRIPTIONS

MODEL = tf.keras.models.load_model('./models/20_cat_classes_model.h5')

def predict(image):
    image = image.resize((128, 128))
    image = np.asarray(image)
    image = image.reshape(1, 128, 128, 3)

    prediction = MODEL.predict(image)[0]
    predicted_breed = CAT_BREEDS[np.argmax(prediction)]
    breed_description = CAT_DESCRIPTIONS[predicted_breed]

    return {CAT_BREEDS[i]: float(prediction[i]) for i in range(20)}, breed_description

with gr.Blocks(css='./static/style.css') as app:
    
    gr.Markdown(
        """
        # Классификатор пород котов
        Разработано студентами Шершневым А.А, Ивановым С.С, Шалаевой И.Г. и Ильиным С.С.
        Группы: РИМ-120906, РИМ-120907
        """, elem_id='md-text')
    
    with gr.Row(elem_id='main-row') as row:

        with gr.Column(scale=2, elem_id='first-col') as col_1:
            user_image = gr.Image(label='Загрузите фотографию котика сюда',        \
                                  type='pil',                                      \
                                  elem_id='user-image')
            predict_button = gr.Button(value='Определить породу')
        
        with gr.Column(scale=1, elem_id='second-col') as col_2:
            predicted_labels = gr.Label(num_top_classes=5,                         \
                                        label='Результат определения породы',      \
                                        elem_id='predictions-text')
    
    breed_description = gr.Markdown(elem_id='breed-description')
    
    predict_button.click(fn=predict,                                               \
                         inputs=[user_image],                                      \
                         outputs=[predicted_labels, breed_description])

if __name__ == '__main__':
    app.launch(debug=True)
import gradio as gr
import tensorflow as tf
import numpy as np
from cat_breeds_list import CAT_BREEDS

MODEL = tf.keras.models.load_model('./models/20_cat_classes_model.h5')

def predict(image):
    image = image.resize((128, 128))
    image = np.asarray(image)
    image = image.reshape(1, 128, 128, 3)
    prediction = MODEL.predict(image)[0]
    return {CAT_BREEDS[i]: float(prediction[i]) for i in range(20)}

with gr.Blocks() as app:
    with gr.Row() as row:
        with gr.Column() as col_1:
            image = gr.Image(label='Загрузите фотографию котика сюда', type='pil')
            button = gr.Button(value='Определить породу')
        with gr.Column() as col_2:
            text = gr.Label(num_top_classes=5, label='Результат определения породы')
    button.click(fn=predict, inputs=image, outputs=text)

if __name__ == '__main__':
    app.launch(debug=True)
import gradio as gr
import tensorflow as tf

model = tf.keras.models.load_model('./models/20_cat_classes_model.h5')

def predict():
    return 'Hello World!'

with gr.Blocks() as app:
    with gr.Row() as row:
        with gr.Column() as col_1:
            image = gr.Image(label='Загрузите фотографию котика сюда')
            button = gr.Button(value='Определить породу')
        with gr.Column() as col_2:
            text = gr.Label(label='Результат определения породы')
    button.click(fn=predict, outputs=text)

if __name__ == '__main__':
    app.launch(debug=True)
import gradio as gr
import tensorflow as tf

model = tf.keras.models.load_model('./models/20_cat_classes_model.h5')

def predict():
    return 'Hello World!'

with gr.Blocks() as app:
    with gr.Row() as row:
        with gr.Column() as col_1:
            image = gr.Image()
            button = gr.Button()
        with gr.Column() as col_2:
            text = gr.Label()
    button.click(fn=predict, outputs=text)

if __name__ == '__main__':
    app.launch(debug=True)
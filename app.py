import gradio as gr
import tensorflow as tf

model = tf.keras.models.load_model('./models/20_cat_classes_model.h5')

def predict():
    return 'Hello World!'

with gr.Blocks() as app:
    image = gr.Image()
    button = gr.Button()
    text = gr.Label()
    button.click(fn=predict, outputs=text)

if __name__ == '__main__':
    app.launch(debug=True)
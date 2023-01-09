import gradio as gr

def predict():
    return 'Hello World!'

with gr.Blocks() as app:
    image = gr.Image()
    button = gr.Button()
    text = gr.Label()
    button.click(fn=predict, outputs=text)

if __name__ == '__main__':
    app.launch(debug=True)
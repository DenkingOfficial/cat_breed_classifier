import gradio as gr
import tensorflow as tf

CAT_BREEDS = ['Бенгальская', 'Бомбейская', 'Бритнаская короткошерстная',    \
              'Бурмилла', 'Девон-рекс', 'Европейская короткошерстная',      \
              'Экзотическая короткошерстная', 'Мейн-кун', 'Нибелунг',       \
              'Персидская','Питерболд', 'Рэгдолл', 'Русская голубая',       \
              'Саванна','Шотландская вислоухая','Сибирская','Сингапурская', \
              'Сомалийская','Сфинкс','Черепаховая']

model = tf.keras.models.load_model('./models/20_cat_classes_model.h5')

def predict(image):
    image = image.reshape((1, 128, 128, 3))
    prediction = model.predict(image)[0]
    return {CAT_BREEDS[i]: float(prediction[i]) for i in range(20)}

with gr.Blocks() as app:
    with gr.Row() as row:
        with gr.Column() as col_1:
            image = gr.Image(shape=(128, 128), label='Загрузите фотографию котика сюда')
            button = gr.Button(value='Определить породу')
        with gr.Column() as col_2:
            text = gr.Label(num_top_classes=5, label='Результат определения породы')
    button.click(fn=predict, inputs=image, outputs=text)

if __name__ == '__main__':
    app.launch(debug=True)
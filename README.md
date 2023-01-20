# \[EN\] Cat Breed Classifier

![build status](https://img.shields.io/github/actions/workflow/status/DenkingOfficial/cat_breed_classifier/python-app.yml?style=flat-square)
[![Try on HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-Try%20on%20HuggingFace-yellow?style=flat-square)](https://huggingface.co/spaces/duuuuuuuden/cat_breed_classifier)

This is an app that can classify the breed of a cat based on a photo.

It uses a EfficientNetB0 ImageNet model finetuned on images of cats of various breeds. The model is able to recognize 18 breeds. See list [here](https://github.com/DenkingOfficial/cat_breed_classifier/tree/main/models).

## Requirements

- Python 3.8 or higher
- Gradio 3.15.0
- Tensorflow 2.10
- Numpy 1.23.3
- Requests 2.25.1
- Pillow 9.0.1
- FastApi 0.88.0
- Uvicorn 0.20.0 or higher
- Smartcrop.py

## How to use

1. Clone this repository using `git clone https://github.com/DenkingOfficial/cat_breed_classifier.git`
2. Enter the cloned directory `cd cat_breed_classifier`
3. Install requirements by running `pip install -r requirements.txt`
4. Download a model from [here](https://www.dropbox.com/s/jqzwew182acdohn/cats_18_EfficientNetB0.h5) and place it into `models` folder
5. Run app using `uvicorn app:app`

## Demonstration

![App demonstration](https://user-images.githubusercontent.com/38957619/212042151-8cded892-4153-48d2-b98b-7430e0149bba.gif)

## Authors

This app was developed by students of Ural Federal University (UrFU):

- Shershnev Andrey, RIM-120907 - Model Training, App Development
- Onuchina Margarita, RIM-120908 - UI Styling, Dataset collection
- Shalaeva Irina, RIM-120906 - UI Styling, Dataset collection
- Ilyin Semen, RIM-120907 - App Development, Dataset collection
- Ivanov Sergey, RIM-120906 - API Development, Dataset collection

---

# \[RU\] Классификатор пород кошек

![build status](https://img.shields.io/github/actions/workflow/status/DenkingOfficial/cat_breed_classifier/python-app.yml?style=flat-square)
[![Try on HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-Try%20on%20HuggingFace-yellow?style=flat-square)](https://huggingface.co/spaces/duuuuuuuden/cat_breed_classifier)

Это веб-приложение, которое позволяет определять породу кошки по фотографии.

Оно использует модель EfficientNetB0 ImageNet тонко настроенную на изображениях кошек разных пород. Данная модель позволяет определять 18 пород. Посмотреть список можно [здесь](https://github.com/DenkingOfficial/cat_breed_classifier/tree/main/models).

## Зависимости

- Python 3.8 или новее
- Gradio 3.15.0
- Tensorflow 2.10
- Numpy 1.23.3
- Requests 2.25.1
- Pillow 9.0.1
- FastApi 0.88.0
- Uvicorn 0.20.0 или новее
- Smartcrop.py

## Как использовать

1. Загрузить данный репозиторий используя команду `git clone https://github.com/DenkingOfficial/cat_breed_classifier.git`
2. Перейти в директорию репозитория `cd cat_breed_classifier`
3. Установить зависимости используя команду `pip install -r requirements.txt`
4. Скачать модель [отсюда](https://www.dropbox.com/s/jqzwew182acdohn/cats_18_EfficientNetB0.h5) и скопировать ее в папку `models`
5. Запустить приложение используя команду `uvicorn app:app`

## Авторы

Это приложение было разработано студентами Уральского Федерального университета (УрФУ):

- Шершнев Андрей, РИМ-120907 - тренировка модели, разработка приложения
- Онучина Маргарита, РИМ-120908 - стилизация интерфейса, сбор датасета
- Шалаева Ирина, РИМ-120906 - стилизация интерфейса, сбор датасета
- Ильин Семен, РИМ-120907 - разработка приложения, сбор датасета
- Иванов Сергей, РИМ-120906 - разработка API, сбор датасета

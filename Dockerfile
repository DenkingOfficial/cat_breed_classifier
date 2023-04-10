FROM python:3.8
EXPOSE 8000
WORKDIR /cat_breed_classifier
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
WORKDIR /cat_breed_classifier/models
RUN curl -L https://www.dropbox.com/s/jqzwew182acdohn/cats_18_EfficientNetB0.h5 -o cats_18_EfficientNetB0.h5
WORKDIR /cat_breed_classifier
COPY . .
CMD uvicorn app:app
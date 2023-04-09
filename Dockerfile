FROM python:3.8
EXPOSE 7860
WORKDIR /cat_breed_classifier
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
RUN curl -LO https://www.dropbox.com/s/jqzwew182acdohn/cats_18_EfficientNetB0.h5
COPY /cats_18_EfficientNetB0.h5 /cat_breed_classifier/models/cats_18_EfficientNetB0.h5
COPY . .
CMD uvicorn app:app
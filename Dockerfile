FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN apk add  --no-cache ffmpeg
RUN pip install -r requirements.txt
EXPOSE 8080
CMD python ./main.py
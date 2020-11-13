FROM python:3.9-alpine

ADD . /app/

WORKDIR /app

RUN pip install -r requirements.txt

USER 1000

CMD ["python", "main.py"]
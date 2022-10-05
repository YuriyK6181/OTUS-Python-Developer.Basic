FROM python:3.9-buster
#FROM python:3.10-bullseye
WORKDIR /app
# RUN apt update && apt install -y python3

RUN pip install --upgrade pip
RUN pip install poetry==1.1.14
RUN poetry config virtualenvs.create false

COPY poetry.lock .
COPY pyproject.toml .

RUN poetry install

COPY web-app .

EXPOSE 8000

CMD uvicorn main:app --host=0.0.0.0 --port=8000
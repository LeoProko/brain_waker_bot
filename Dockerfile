# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /brain_waker_bot

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "run_bot.py"]

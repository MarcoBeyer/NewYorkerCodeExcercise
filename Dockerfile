FROM python:3

WORKDIR /usr/src/app
COPY src/. .

ENTRYPOINT [ "python", "./workflow.py"]
FROM python:alpine3.18

RUN python3 --version

COPY reducer.py /

CMD python3 reducer.py
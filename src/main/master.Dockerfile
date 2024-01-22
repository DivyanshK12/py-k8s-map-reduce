FROM python:alpine3.18

RUN python3 --version

COPY master.py /

CMD python3 master.py
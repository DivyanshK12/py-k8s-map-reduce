FROM python:3.11

RUN python3 --version

RUN pip install kafka-python

COPY master.py /

CMD python3 master.py
FROM python:3.11

RUN python3 --version

RUN pip install kafka-python
RUN pip install cassandra-driver

COPY master.py /

CMD python3 master.py
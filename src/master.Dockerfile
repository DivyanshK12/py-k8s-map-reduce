FROM python:alpine3.18

RUN python3 --version

ENV MAP_POD_COUNT=5
ENV REDUCE_POD_COUNT=3

COPY master.py /

CMD python3 master.py
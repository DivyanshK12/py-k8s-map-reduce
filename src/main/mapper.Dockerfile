FROM python:alpine3.18

RUN python3 --version

COPY mapper.py /

CMD python3 mapper.py
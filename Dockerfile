FROM python:3.8.16-bullseye

RUN pip install click
# Note: these packages should be shipped w/ python env, so no need to pip install:
# json, os, Path, datetime

ADD fake_script.py /home

ENTRYPOINT [ "python3", "/home/fake_script.py" ]
FROM python:3.8.16-bullseye

RUN pip install click

ADD fake_script.py /home

ENTRYPOINT [ "python3", "/home/fake_script.py" ]
FROM python3/ubuntu18:2.0
ADD . /code
WORKDIR /code
RUN pip3 install -r requirements.txt
CMD python3 run.py

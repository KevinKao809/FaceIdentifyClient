FROM jjanzic/docker-python3-opencv

COPY . /app
WORKDIR /app

RUN pip install -r /app/requirements.txt

CMD ["python3", "-u" , "/app/run.py"]

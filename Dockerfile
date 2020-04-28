FROM ubuntu:20.04

RUN apt update
RUN apt install python3-pip -y && pip3 install -r requirements.txt 


WORKDIR /app

COPY . .

CMD ["python3", "./main.py"]

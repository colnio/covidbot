FROM ubuntu:20.04

WORKDIR /app

RUN apt update
RUN apt upgrade -y
RUN apt install python3-pip -y 
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . .
RUN python3 main.py

CMD ["python3", "./main.py"]

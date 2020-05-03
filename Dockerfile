FROM ubuntu:20.04

RUN sudo apt update
RUN sudo apt upgrade -y
RUN apt install python3-pip -y 
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

WORKDIR /app

COPY . .

CMD ["python3", "./main.py"]

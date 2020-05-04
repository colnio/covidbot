FROM ubuntu:18.04

WORKDIR /app

RUN apt update
RUN apt upgrade -y
RUN apt install python3-pip -y 
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY /home/yra200111ruz_gmail_com/covidbot ./

CMD ["python3", "main.py"]

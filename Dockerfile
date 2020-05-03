FROM ubuntu:20.04

RUN apt update
RUN apt install python3-pip -y && pip3 install -r requirements.txt 
RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY main.py ./
RUN yarn install

COPY . .

CMD ["python3", "./main.py"]

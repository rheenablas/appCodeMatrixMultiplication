FROM python:latest


WORKDIR /usr/app/src

COPY Lab1.py ./

CMD [ "python", "./Lab1.py"]


#the Dockerfile originally
#source: https://www.youtube.com/watch?v=uvTl6GefR9o
#FROM ubuntu:latest

#RUN apt update
#RUN apt install python3 -y

#WORKDIR /usr/app/src

#COPY Lab1.py ./

#CMD [ "python", "./Lab1.py"]
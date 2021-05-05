  
FROM ubuntu:20.04
RUN apt-get update
RUN apt-get upgrade
RUN apt-get install git
# Y
RUN apt-get install python3-pip
# Y
RUN git clone -b feat/dockerfile https://github.com/sangcholi/Text_summarization.git

WORKDIR /Text_summarization
RUN pip3 install -r requirements.txt
RUN python3 summarizaion.py
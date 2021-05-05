  
FROM ubuntu:20.04
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
git \
python3-pip

RUN git clone -b feat/dockerfile https://github.com/sangcholi/Text_summarization.git

WORKDIR /Text_summarization
RUN pip3 install -r requirements.txt
RUN python3 summarizaion.py
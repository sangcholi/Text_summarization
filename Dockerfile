FROM gpuci/miniconda-cuda:11.2-runtime-ubuntu20.04
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
git \
python3-pip

RUN git clone https://github.com/sangcholi/Text_summarization.git

WORKDIR /Text_summarization
RUN pip3 install -r requirements.txt

ENTRYPOINT [ "flask" ]
CMD [ "run --host=0.0.0.0" ]
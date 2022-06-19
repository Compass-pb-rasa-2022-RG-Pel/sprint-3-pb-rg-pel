FROM jupyter/tensorflow-notebook:latest

RUN pip install requests feature_engine \
    pip install -q tfds-nightly tensorflow matplotlib\
    pip install tensorflow-datasets\
    pip install tfds-nightly

USER root
# apt-utils is missing and needed to avoid warning about skipping debconf
RUN apt-get update && apt-get --yes install apt-utils
# install whatever else you want on this line
RUN apt-get --yes install curl
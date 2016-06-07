# Start with TensorFlow image
FROM tensorflow/tensorflow:latest-devel-gpu
MAINTAINER Antti

# Install required packages
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    wget \
    python-pip \
    python-dev \
    build-essential \
    g++ \
    python-nose \
    python-six \
    cython \
    curl \
    net-tools \
    unzip \
    python \
    libffi-dev \
    libssl-dev \
 && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

COPY flask_application /home/root/flask_application
COPY static /home/root/static
COPY manage.py /home/root/manage.py
COPY entrypoint.sh /usr/bin/entrypoint.sh
RUN chmod a+x /usr/bin/entrypoint.sh

WORKDIR /home/root
ENTRYPOINT /usr/bin/entrypoint.sh

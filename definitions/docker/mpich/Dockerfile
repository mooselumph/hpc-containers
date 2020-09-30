FROM python:3.8.5-slim-buster

# Setup Environment
RUN apt-get update && \
    apt-get install -y \
      build-essential \
      gfortran \
      wget \
      git \
      bzip2 \
      unzip \
      ssh

ENV LC_ALL=C

RUN apt-get dist-upgrade -y
    
# Install MPICH
ARG MPICH_VERSION="3.3.2"

RUN mkdir /tmp/mpich-src && \
    cd /tmp/mpich-src && \
    wget http://www.mpich.org/static/downloads/${MPICH_VERSION}/mpich-${MPICH_VERSION}.tar.gz && \
    tar xfz mpich-${MPICH_VERSION}.tar.gz && \
    cd mpich-${MPICH_VERSION} && \
    ./configure ${MPICH_CONFIGURE_OPTIONS} && \
    make && make install && \
    cd / && \
    rm -rf /tmp/mpich-src

RUN pip install mpi4py

# Installation of Obspy without conda: https://github.com/obspy/obspy/wiki/Installation-on-Linux-via-Apt-Repository

RUN echo "deb http://deb.obspy.org buster main" > /etc/apt/sources.list.d/docker.list && \
    wget --quiet -O - https://raw.githubusercontent.com/obspy/obspy/master/misc/debian/public.key | apt-key add -
    
RUN apt-get update && \
    apt-get install -y python-obspy python3-obspy
    
RUN apt-get clean
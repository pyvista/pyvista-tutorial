FROM ghcr.io/pyvista/pyvista:0.33.2
MAINTAINER "PyVista Developers"
SHELL ["/bin/bash", "-c"]

ARG NB_USER=jovyan
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}

WORKDIR $HOME

COPY requirements.txt $HOME

RUN pip install -r requirements.txt

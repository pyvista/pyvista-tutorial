FROM ghcr.io/pyvista/pyvista:0.33.2
MAINTAINER "PyVista Developers"
SHELL ["/bin/bash", "-c"]


COPY requirements.txt $HOME

RUN pip install -r requirements.txt

FROM ghcr.io/pyvista/pyvista:v0.33.2
MAINTAINER "PyVista Developers"
SHELL ["/bin/bash", "-c"]


COPY . $HOME

RUN pip install -r requirements.txt

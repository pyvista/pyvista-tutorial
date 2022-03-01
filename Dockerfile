FROM ghcr.io/pyvista/pyvista:v0.33.3
MAINTAINER "PyVista Developers"
SHELL ["/bin/bash", "-c"]


COPY . $HOME

RUN pip install -r requirements.txt

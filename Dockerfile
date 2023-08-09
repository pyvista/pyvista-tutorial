FROM ghcr.io/pyvista/pyvista:v0.41.1
MAINTAINER "PyVista Developers"
SHELL ["/bin/bash", "-c"]


COPY . $HOME

RUN pip install pyvista
RUN pip install pyinstaller==5.1
RUN pip install sphinx
RUN pip install tqdm
RUN pip install imageio>=2.5.0
RUN pip install imageio-ffmpeg
RUN pip install matplotlib
RUN pip install cmocean
RUN pip install trame

FROM jupyter/datascience-notebook:python-3.8.6


ARG PYTHON_VERSION=3.8
SHELL [ "/bin/bash", "-l", "-c" ]

USER root
ENV NVM_DIR /usr/local/nvm
ENV CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
ENV GEOS_VERSION 3.8.0
ENV PROJ4_VERSION 6.3.1
ENV GDAL_VERSION 3.1.0
ENV ENCODING UTF-8
ENV LOCALE en_US

RUN apt-get update && \ 
    apt-get install -y --no-install-recommends \
    python3-rtree \
    software-properties-common \
    graphviz \
    ca-certificates \
    build-essential \
    libsqlite3-dev \
    zlib1g-dev \
    manpages-dev \
    curl && \   
    add-apt-repository -y ppa:ubuntu-toolchain-r/test && apt update -q -y && \
    apt install -q -y g++ && export CXX=g++ && \
	pip install jupyter_contrib_nbextensions jupyter_nbextensions_configurator version_information jupyterlab && jupyter contrib nbextension install --sys-prefix && jupyter nbextensions_configurator enable

RUN mkdir -p "$NVM_DIR"; \
    curl -o- \
        "https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh" | \
        bash \
    ; \
    source $NVM_DIR/nvm.sh; \
    nvm install --lts --latest-npm
RUN npm install @mapbox/mapbox-gl-style-spec --global

Run git clone https://github.com/mapbox/tippecanoe.git && \
	cd tippecanoe && \
	make -j && make install && cd ..
RUN export CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt 
# Having to install gdal through conda gaves me chills; trying installing it through pip is failing badly. no time to dig depply on what is going on probably issues with path.
RUN conda update -n base conda && conda install -c conda-forge python-blosc cytoolz gdal dask==2.30 xhistogram lz4 nomkl dask-labextension==3.0 python-graphviz tini==0.18.0 xarray=0.16.1
# Add requirements file
COPY jupyter_notebook_config.py /etc/jupyter/ 
COPY requirements.txt /app/
Run pip install wheel -r /app/requirements.txt 

# Enable extensions
RUN jupyter nbextension install --sys-prefix --py vega && \
    jupyter nbextension enable vega --py --sys-prefix &&  \
    jupyter nbextension enable --py --sys-prefix ipyleaflet && \
    jupyter labextension install @jupyter-widgets/jupyterlab-manager dask-labextension@2.0.2 && \ 
    jupyter nbextension install --py jupytemplate --sys-prefix && \
     jupyter nbextension enable jupytemplate/main --sys-prefix 

RUN mkdir /opt/app

# Jupyter with Docker Compose
EXPOSE 8888
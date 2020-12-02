FROM jupyter/datascience-notebook:python-3.8.6

SHELL [ "/bin/bash", "-l", "-c" ]

USER root
ENV NVM_DIR /usr/local/nvm
ENV CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt

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
    mkdir -p "$NVM_DIR"; \
    curl -o- \
        "https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh" | \
        bash \
    ; \
    source $NVM_DIR/nvm.sh; \
    nvm install --lts --latest-npm \
    && npm install @mapbox/mapbox-gl-style-spec --global

Run git clone https://github.com/mapbox/tippecanoe.git && \
	cd tippecanoe && \
	make -j && make install && cd ..
RUN export CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
# Having to install gdal through conda gaves me chills; trying installing it through pip is failing badly. no time to dig depply on what is going on probably issues with path.
RUN conda update -n base conda && conda install -c conda-forge python-blosc cytoolz gdal dask==2.30 xhistogram lz4 nomkl dask-labextension==3.0 python-graphviz tini==0.18.0 xarray=0.16.1
RUN pip install jupyter_contrib_nbextensions \
                jupyter_nbextensions_configurator \
                version_information \
                jupyterlab \
                nbdev \
                autopep8 \
                nbdime \
                vega \
                ipyleaflet

# Enable extensions
RUN jupyter contrib nbextension install --sys-prefix && \
                jupyter nbextensions_configurator enable  && \
                jupyter nbextension install --sys-prefix --py vega && \
                jupyter nbextension enable vega --py --sys-prefix &&  \
                jupyter nbextension enable --py --sys-prefix ipyleaflet && \
                jupyter labextension install @jupyter-widgets/jupyterlab-manager dask-labextension@2.0.2 && \
                jupyter nbextension install --py jupytemplate --sys-prefix && \
                jupyter nbextension enable jupytemplate/main --sys-prefix

# Add requirements file
COPY requirements.txt /app/
RUN pip install wheel -r /app/requirements.txt



COPY jupyter_notebook_config.py /etc/jupyter/
RUN mkdir /opt/app

# Jupyter with Docker Compose
EXPOSE 8888

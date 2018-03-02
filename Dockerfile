
FROM nvidia/cuda:9.0-cudnn7-runtime

# Add some dependencies
RUN apt-get clean && apt-get update -y -qq
RUN apt-get install -y curl git build-essential
RUN apt-get update && apt-get -y install sudo && apt-get install gosu

# last cuda version, to change - LASTEST_CONDA
ENV LATEST_CONDA "5.0.1"
ENV PATH="/opt/anaconda/anaconda3/bin:${PATH}"

# download and install conda
RUN curl --silent -O https://repo.continuum.io/archive/Anaconda3-$LATEST_CONDA-Linux-x86_64.sh \
    && bash Anaconda3-$LATEST_CONDA-Linux-x86_64.sh -b -p /opt/anaconda/anaconda3

# tensorflow and keras
RUN pip install tensorflow-gpu==1.5.0rc0
RUN pip install keras && conda install pygpu

# opencv
RUN conda install -c conda-forge opencv -yy

# other python files
RUN pip install shapely tqdm tqdm h5py scikit-image matplotlib pandas pillow geojson tifffile

# other packages
RUN apt-get install nano && apt-get install vim -yy

# rasterio installation
RUN conda install -c conda-forge/label/dev rasterio
# install pytorch
RUN conda install pytorch torchvision -c pytorch

COPY jupyter_notebook_config.py /root/.jupyter/

ARG UID=1000
ARG GID=1000
RUN groupadd -g $GID user && useradd -m -s /bin/bash -u $UID -g user -G root user
RUN usermod -aG sudo user
RUN echo "user:user" | chpasswd
WORKDIR /home/user
COPY --chown=user:user jupyter_notebook_config.py /home/user/.jupyter/
COPY runuser.sh /opt/run/
RUN echo "export PATH='/opt/anaconda/anaconda3/bin:${PATH}'" >> /home/user/.bashrc
RUN chmod +x /opt/run/runuser.sh

# start custom entrypoint
ENTRYPOINT ["/opt/run/runuser.sh"]


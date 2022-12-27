# fedora-36 
FROM registry.fedoraproject.org/fedora:36 

WORKDIR /vagrant

COPY requirements.txt /vagrant

RUN \
    dnf -y install \
#      python3 \
      sqlite \
      pip \
      gcc \
      python3-devel \
    && \
    dnf clean all

RUN \    
    python3 -m pip install -r requirements.txt

COPY app_setup.sh /vagrant

ENTRYPOINT /bin/bash /vagrant/app_setup.sh

EXPOSE 8000/tcp

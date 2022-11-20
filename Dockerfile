FROM kalilinux/kali-rolling:amd64
ENV DEBIAN_FRONTEND noninteractive

# hadolint ignore=DL3008,DL3009

RUN apt update -y && apt upgrade -y && apt-get autoremove -y && apt-get clean -y && apt-get -y install --no-install-recommends \
    nmap \
    zaproxy \ 
    gnupg2 \
    pass \
    python3-pip \
    openssh-client \
    jq \
    python-tk \
    git \
    wget \ 
    curl \
    expect 

RUN pip3 install \
    pipenv \
    xmltodict \
    PyJSONViewer \
    requests \
    pandas \
    python-logging-loki 

RUN curl --request GET \
    --url 'https://www.tenable.com/downloads/api/v2/pages/nessus/files/Nessus-10.4.1-ubuntu1404_amd64.deb' \
    --output 'Nessus-10.4.1-ubuntu1404_amd64.deb'

RUN dpkg -i Nessus-10.4.1-ubuntu1404_amd64.deb


WORKDIR /
RUN mkdir APP RESULTS
WORKDIR /APP
RUN wget https://hackers-utopia.s3.amazonaws.com/burpsuite_community ./
RUN wget https://hackers-utopia.s3.amazonaws.com/burpsuite_community_linux_v2022_9_6.sh ./
RUN wget https://hackers-utopia.s3.amazonaws.com/burpsuite_pro ./
RUN wget https://hackers-utopia.s3.amazonaws.com/burpsuite_pro_linux_v2022_9_6.sh ./
COPY burpsuite_community burpsuite_pro entrypoint.sh burpsuite_pro_linux_v2022_9_6.sh burpsuite_community_linux_v2022_9_6.sh ./
RUN chmod +x entrypoint.sh burpsuite_pro_linux_v2022_9_6.sh burpsuite_community_linux_v2022_9_6.sh
RUN ./burpsuite_pro && ./burpsuite_community
RUN cd /usr/share/nmap/scripts/ && \
    git clone https://github.com/vulnersCom/nmap-vulners.git && \
    wget https://raw.githubusercontent.com/daviddias/node-dirbuster/master/lists/directory-list-2.3-medium.txt
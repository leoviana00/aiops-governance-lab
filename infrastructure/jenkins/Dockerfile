FROM jenkins/jenkins:lts-jdk21

USER root

# Remove repos antigos
RUN rm -rf /etc/apt/sources.list.d/*

# Repos Debian
RUN echo "deb http://deb.debian.org/debian bookworm main" > /etc/apt/sources.list && \
    echo "deb http://deb.debian.org/debian bookworm-updates main" >> /etc/apt/sources.list

# Instala dependências
RUN apt-get -o Acquire::Check-Valid-Until=false update && \
    apt-get install -y \
        curl \
        git \
        lsof \
        iproute2 \
        net-tools \
        ca-certificates \
        gnupg

# Instala Docker CLI oficial (versão moderna)
RUN install -m 0755 -d /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | \
    gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
    chmod a+r /etc/apt/keyrings/docker.gpg && \
    echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
    https://download.docker.com/linux/debian bookworm stable" \
    > /etc/apt/sources.list.d/docker.list

RUN apt-get update && \
    apt-get install -y docker-ce-cli && \
    apt-get clean

# Jenkins roda como root para acessar docker.sock
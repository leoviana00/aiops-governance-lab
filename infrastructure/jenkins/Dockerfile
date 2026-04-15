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



# =========================
# SSH AUTOMÁTICO
# =========================

RUN mkdir -p /root/.ssh

# copiar chave
COPY ssh/id_ed25519 /root/.ssh/id_ed25519
COPY ssh/id_ed25519.pub /root/.ssh/id_ed25519.pub

# permissões
RUN chmod 700 /root/.ssh && \
    chmod 600 /root/.ssh/id_ed25519 && \
    chmod 644 /root/.ssh/id_ed25519.pub

# adicionar gitlab aos hosts conhecidos
#RUN ssh-keyscan gitlab >> /root/.ssh/known_hosts

# garantir permissões
#RUN chmod 644 /root/.ssh/known_hosts

# garantir que git use essa chave
RUN echo "Host gitlab\n\
  HostName gitlab\n\
  User git\n\
  IdentityFile /root/.ssh/id_ed25519\n\
  StrictHostKeyChecking no\n" >> /root/.ssh/config

RUN chmod 600 /root/.ssh/config


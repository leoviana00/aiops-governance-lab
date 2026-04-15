docker exec -it aiops-jenkins bash

ssh-keygen -t ed25519 -C "jenkins@gitlab"

mkdir -p /var/jenkins_home/.ssh

mv /root/.ssh/id_ed25519 /var/jenkins_home/.ssh/
mv /root/.ssh/id_ed25519.pub /var/jenkins_home/.ssh/

chown -R jenkins:jenkins /var/jenkins_home/.ssh
chmod 700 /var/jenkins_home/.ssh
chmod 600 /var/jenkins_home/.ssh/id_ed25519

ssh-keyscan gitlab >> /var/jenkins_home/.ssh/known_hosts
chown jenkins:jenkins /var/jenkins_home/.ssh/known_hosts
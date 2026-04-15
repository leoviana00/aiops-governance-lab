#!/bin/bash

set -e

mkdir -p /var/jenkins_home/.ssh

if ! grep -q gitlab ~/.ssh/known_hosts 2>/dev/null; then
  echo "Adding GitLab SSH key..."
  ssh-keyscan gitlab >> /var/jenkins_home/.ssh/known_hosts
fi

chown -R jenkins:jenkins /var/jenkins_home/.ssh

exec /usr/bin/tini -- /usr/local/bin/jenkins.sh
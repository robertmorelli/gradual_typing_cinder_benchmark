#!/bin/bash
set -euo pipefail

sudo apt-get upgrade
sudo apt-get install -y libz-dev

# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install -y ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
# Add the repository to Apt sources:
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get install -y $pkg; done

if ! command -v go &>/dev/null; then
    GO_TAR="go1.26.1.linux-amd64.tar.gz"
    wget -q "https://go.dev/dl/$GO_TAR" -O "/tmp/$GO_TAR"
    sudo tar -C /usr/local -xzf "/tmp/$GO_TAR"
    export PATH=$PATH:/usr/local/go/bin
    echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
fi

git submodule update --init
bash cinder_env/setup.sh

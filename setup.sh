#!/bin/bash
set -euo pipefail

# Apt config: force IPv4, swap to a reliable mirror
echo 'Acquire::ForceIPv4 "true";' | sudo tee /etc/apt/apt.conf.d/99force-ipv4 > /dev/null
sudo sed -i 's|http://[a-z.]*archive.ubuntu.com/ubuntu|http://mirrors.kernel.org/ubuntu|g' /etc/apt/sources.list
sudo sed -i 's|http://security.ubuntu.com/ubuntu|http://mirrors.kernel.org/ubuntu|g' /etc/apt/sources.list

# Remove any pre-existing Docker packages that conflict with Docker CE
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do
    if dpkg -l "$pkg" &>/dev/null; then
        sudo apt-get remove -y "$pkg"
    fi
done

sudo apt-get update
sudo apt-get install -y ca-certificates curl gnupg

# Docker repo + GPG key (idempotent)
sudo install -m 0755 -d /etc/apt/keyrings
sudo rm -f /etc/apt/keyrings/docker.gpg
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

arch=$(dpkg --print-architecture)
codename=$(. /etc/os-release && echo "$VERSION_CODENAME")
echo "deb [arch=$arch signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $codename stable" \
    | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Add current user to docker group so we can run docker without sudo
sudo usermod -aG docker "$USER"

# Install Go if missing
if ! command -v go &>/dev/null; then
    GO_TAR="go1.24.2.linux-amd64.tar.gz"
    wget -q "https://go.dev/dl/$GO_TAR" -O "/tmp/$GO_TAR"
    sudo tar -C /usr/local -xzf "/tmp/$GO_TAR"
    if ! grep -q '/usr/local/go/bin' ~/.bashrc; then
        echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
    fi
fi
export PATH=$PATH:/usr/local/go/bin

# GitHub CLI (idempotent)
sudo mkdir -p -m 755 /etc/apt/keyrings
sudo rm -f /etc/apt/keyrings/githubcli-archive-keyring.gpg
wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg \
    | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg >/dev/null
sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$arch signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" \
    | sudo tee /etc/apt/sources.list.d/github-cli.list >/dev/null
sudo apt-get update
sudo apt-get install -y gh

git config --global user.name "robertmorelli"
git config --global user.email "robertondino@outlook.com"

git submodule update --init --recursive

# Run the docker-using subscript with the new group active in this shell
sg docker -c "bash cinder_env/setup.sh"
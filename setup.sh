#!/bin/bash
set -euo pipefail

# Force IPv4 for apt and swap to a more reliable mirror before doing anything
echo 'Acquire::ForceIPv4 "true";' | sudo tee /etc/apt/apt.conf.d/99force-ipv4 > /dev/null
sudo sed -i 's|us.archive.ubuntu.com|archive.ubuntu.com|g' /etc/apt/sources.list
sudo sed -i 's|//.*archive.ubuntu.com|//archive.ubuntu.com|g' /etc/apt/sources.list.d/*.list 2>/dev/null || true

# Remove any conflicting Docker packages that might be installed
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do
    if dpkg -l "$pkg" &>/dev/null; then
        sudo apt-get remove -y "$pkg"
    fi
done

# Add Docker's official GPG key
sudo apt-get update
sudo apt-get install -y ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add Docker repository to apt sources
arch=$(dpkg --print-architecture)
codename=$(. /etc/os-release && echo "$VERSION_CODENAME")
echo "deb [arch=$arch signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $codename stable" \
    | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Install Go if not already present
if ! command -v go &>/dev/null; then
    GO_TAR="go1.24.2.linux-amd64.tar.gz"
    wget -q "https://go.dev/dl/$GO_TAR" -O "/tmp/$GO_TAR"
    sudo tar -C /usr/local -xzf "/tmp/$GO_TAR"
    export PATH=$PATH:/usr/local/go/bin
    if ! grep -q '/usr/local/go/bin' ~/.bashrc; then
        echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
    fi
fi

# Install GitHub CLI
sudo mkdir -p -m 755 /etc/apt/keyrings
wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg \
    | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg >/dev/null
sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" \
    | sudo tee /etc/apt/sources.list.d/github-cli.list >/dev/null
sudo apt-get update
sudo apt-get install -y gh

git config --global user.name "robertmorelli"
git config --global user.email "robertondino@outlook.com"

git submodule update --init

bash cinder_env/setup.sh
#!/bin/bash
set -e

if ! command -v go &>/dev/null; then
    GO_TAR="go1.26.1.linux-amd64.tar.gz"
    wget -q "https://go.dev/dl/$GO_TAR" -O "/tmp/$GO_TAR"
    sudo tar -C /usr/local -xzf "/tmp/$GO_TAR"
    export PATH=$PATH:/usr/local/go/bin
    echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
fi

git submodule update --init
sh cinder_env/setup.sh

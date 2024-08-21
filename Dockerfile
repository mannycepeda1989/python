# Includes GIT, Python3.9 and build-essentials (node-gyp) and uses Yarn@3.5.0
FROM debian:bullseye-20230502-slim
RUN groupadd --gid 1000 node && useradd --uid 1000 --gid node - -shell /bin/bash --create-home node
ENV NODE_VERSION=18.20.4
RUN /bin/sh -c ARCH= && dpkgArch="$(dpkg --print-architecture)" && case "${dpkgArch##*_}" in amd64) ARCH='х64';; p
RUN apt-get update && apt-get install -y ca-certificates curl get jq vim net-tools props bash python3.9 git buil
RUN corepack enable
RUN corepack prepare yarn@3.5.0 --activate
ENV PYTHON=/usr/bin/python3.9

---
sidebar_position: 1
slug: setup
---

## Prerequirements

1. Install Docker Engine and Docker Compose.

## All-in-one deployment with Docker Compose

Just run `docker-compose up`. It will spin up multiple containers:
- `portrait` for Ubuntu Portrait.

## Building the Ubuntu Portrait container from source

1. Build the Docker image: `docker build --tag portrait --file Dockerfile.portrait .`
2. Create a new container based on the image: `docker run --name portrait --env "PORTRAIT_RECOVERY_PASSPHRASE=<secret_key>" --publish 8080:8080 portrait`

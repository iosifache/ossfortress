---
sidebar_position: 1
slug: setup
---

## Ubuntu Portrait

### Using GitHub Container Registry

1. Pull the image: `docker pull ghcr.io/iosifache/oss_fortress_portrait:main`
2. Create a new container based on the image: `docker run --name portrait --env "PORTRAIT_RECOVERY_PASSPHRASE=<secret_key>" --publish 8080:8080 ghcr.io/iosifache/oss_fortress_portrait`

### Building from source

1. Build the Docker image: `docker build --tag portrait .`
2. Create a new container based on the image: `docker run --name portrait --env "PORTRAIT_RECOVERY_PASSPHRASE=<secret_key>" --publish 8080:8080 portrait`

## Analysis infrastructure

TBD

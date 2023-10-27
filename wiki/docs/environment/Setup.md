---
sidebar_position: 2
slug: setup
---

## Setup approaches

The infrastructure mentioned in [the tooling page](/environment/analysis-infrastructure) can be setup:
- Manually: Follow the installation guide provided in the documentation of each each tool. The documentations are linked in the pages for each tool.
- By using the provided Docker Compose infrastructure.

## Docker Compose 

Please ensure you have installed [Docker Engine](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/).

For building the images from `Dockerfile`, use `docker compose build`. `docker compose up` will splin up the services, but can use the upstream images if the build command was not ran before.

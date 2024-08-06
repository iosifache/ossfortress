---
sidebar_position: 7
slug: analysis-infrastructure
---

## Tooling

The tools that will be used during the workshop are:
- [OWASP Threat Dragon](/threat-modelling/owasp-threat-dragon) for modelling the cyberthreats for a given application;
- [Gitleaks](/secret-scanning/gitleaks) for scanning a Git repository for leaked secrets;
- [OSV-Scanner](/dependency-scanning/osv-scanner) for scanning dependencies for vulnerabilities;
- [flawfinder](/linting/flawfinder) for statically analysing C code to find security concerns;
- [Bandit](/linting/bandit) for statically analysing Python code to find security concerns;
- [Semgrep](/code-query/semgrep) for code querying;
- [AFL++](/fuzzing/aflplusplus) for fuzzing C code; and
- [KLEE](/symbolic-execution/klee) for symbolically executing C code.

## Docker infrastructure

For the analysed application and the above tooling, the workshop provides a Docker Compose infrastructure with the following services/containers:

### Sand Castle

- **Service name**: `sandcastle`
- **Description**: Demo Sand Castle instance
- **Docker Compose profiles**
    - `sandcastle`
    - `all`
- **`Dockerfile` in the `ossfortress` repository**: `sandcastle/Dockerfile`
- **Hosted image**: `iosifache/sandcastle:main` in GitHub Container Registry
- **Exposed ports**: `8000` for the web UI
- **User**: `root`
- **Credentials**: N/A
- **Relevant folders**: N/A

### OWASP Threat Dragon

- **Service name**: `owasp_threat_dragon`
- **Description**: OWASP Threat Dragon instance, accessible from [`localhost`](http://localhost:8081)
- **Docker Compose profiles**
    - `threat-modelling`
    - `all`
- **`Dockerfile` in the `ossfortress` repository**: N/A
- **Hosted image**: `owasp/threat-dragon:latest` in Docker Hub
- **Exposed ports**: `8001` for the web UI
- **User**: `root`
- **Credentials**: N/A
- **Relevant folders**: N/A

### Coder

- **Service name**: `coder`
- **Description**: [Coder](https://coder.com) instance, accessible from [`localhost`](http://localhost:8082/?folder=/home/coder)
- **Docker Compose profiles**
    - `threat-modelling`
    - `all`
- **`Dockerfile` in the `ossfortress` repository**: `tooling/coder/Dockerfile`
- **Hosted image**: `iosifache/coder:main` in GitHub Container Registry
- **Exposed ports**: `8002` for the web UI
- **User**: `coder`
- **Credentials**: `ossfortress` as the password for authenticating in the user interface
- **Relevant folders**
    - `/home/coder/codebase` for Sand Castle's codebase
    - `/home/coder/tooling` for the tooling-related information
    - `/home/coder/analysis` for files resulted during the analysis of the vulnerable codebase

### Static analysers

- **Service name**: `static-analysers`
- **Description**: Ubuntu container with static analysers (Gitleaks, OSV-Scanner, flawfinder, Bandit, and Semgrep) installed
- **Docker Compose profiles**
    - `static-analysis`
    - `all`
- **`Dockerfile` in the `ossfortress` repository**: `tooling/static-analysers/Dockerfile`
- **Hosted image**: `iosifache/static-analysers:main` in GitHub Container Registry
- **Exposed ports**: N/A
- **User**: `root`
- **Credentials**: N/A
- **Relevant folders**
    - `/home/coder/codebase` for the Sand Castle codebase
    - `/home/coder/tooling` for the tooling-related information
    - `/root/analysis` for files resulted during the analysis of the vulnerable codebase

### AFL++

- **Service name**: `aflplusplus`
- **Description**: Container with AFL++ installed
- **Docker Compose profiles**
    - `dynamic-analysis`
    - `all`
- **`Dockerfile` in the `ossfortress` repository**: `tooling/aflplusplus/Dockerfile`
- **Hosted image**: `iosifache/aflplusplus:main` in GitHub Container Registry
- **Exposed ports**: N/A
- **User**: `root`
- **Credentials**: N/A
- **Relevant folders**
    - `/home/coder/codebase` for the Sand Castle codebase
    - `/home/coder/tooling` for the tooling-related information
    - `/root/analysis` for files resulted during the analysis of the vulnerable codebase

### KLEE

- **Service name**: `klee`
- **Description**: Container with KLEE installed
- **Docker Compose profiles**
    - `dynamic-analysis`
    - `all`
- **`Dockerfile` in the `ossfortress` repository**: N/A
- **Hosted image**: `klee/klee:latest` in GitHub Container Registry
- **Exposed ports**: N/A
- **User**: `root`
- **Credentials**: N/A
- **Relevant folders**
    - `/home/coder/codebase` for the Sand Castle codebase
    - `/home/coder/tooling` for the tooling-related information
    - `/root/analysis` for files resulted during the analysis of the vulnerable codebase

## Overview

The below infrastructure presents the recommended workflow for analysis, using the recommended tooling and [Docker Compose services](#docker-infrastructure).

_![Analysis infrastructure](/img/diagrams/analysis-infra.svg)_

## Setup

The infrastructure can be setup:
- Manually: Follow the installation guide provided in the documentation of each each tool. The documentations are linked in the pages for each tool.
- By using the provided Docker Compose infrastructure.

### Docker Compose 

Please ensure you have installed [Docker Engine](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/).

:::tip

On Debian-based operating systems, it's as easy as [running the convenience script](https://docs.docker.com/engine/install/debian/#install-using-the-convenience-script) and installing `docker-compose-plugin` via `apt`.

:::

Clone [the GitHub repository](https://github.com/iosifache/ossfortress) as follows:

```bash
git clone https://github.com/iosifache/ossfortress
```

You can use `docker-compose --profile all pull` to pull the GHCR images. Otherwise, use `docker-compose --profile all build` for building the images from scratch. If the build fails, try running again after setting the `DOCKER_BUILDKIT` environment variable as follows: `export DOCKER_BUILDKIT=1`.

`docker-compose --profile all up` will spin up the services.

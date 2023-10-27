FROM codercom/code-server:latest

ENV DOCKER_USER=coder
ENV PASSWORD="oss-fortress"

WORKDIR /home/coder

COPY vscode-config /home/coder/.vscode

COPY extensions /home/coder/extensions

RUN code-server --install-extension /home/coder/extensions/*.vsix

EXPOSE 8080

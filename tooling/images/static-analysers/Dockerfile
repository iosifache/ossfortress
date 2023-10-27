FROM ubuntu:mantic

WORKDIR /root

RUN apt update

# Install CA certificates
RUN apt install -y ca-certificates
RUN update-ca-certificates

# Install OSV-Scanner
RUN apt install -y golang-go
RUN go install github.com/google/osv-scanner/cmd/osv-scanner@v1
RUN mv /root/go/bin/osv-scanner /bin

# Install Python
RUN apt install -y python3 python3-pip
RUN rm /usr/lib/python3.11/EXTERNALLY-MANAGED

# Install Semgrep
RUN pip3 install semgrep

# Install Flawfinder
RUN pip install flawfinder

# Install Bandit
RUN pip install bandit

# Install Gitleaks
WORKDIR /tmp
RUN apt install -y git
RUN git clone https://github.com/gitleaks/gitleaks.git
WORKDIR /tmp/gitleaks
RUN make build
RUN cp /tmp/gitleaks/gitleaks /bin

WORKDIR /root/

ENTRYPOINT ["tail", "-f", "/dev/null"]

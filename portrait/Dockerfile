# Set the base image
FROM python

# Create a new user
RUN useradd ubuntu
RUN echo "ubuntu:ubuntu" | chpasswd

# Set the environment configuration, and install the Python toolchain
RUN pip install -U pip setuptools
RUN pip install poetry
ENV PATH="${PATH}:${POETRY_VENV}/bin"

# Copy the application
COPY . /app

# Compile the C shared object
RUN apt update
RUN apt install -y gcc make
WORKDIR /app/portrait/c_modules
RUN make

# Set the application configuration
ENV PORTRAIT_RECOVERY_PASSPHRASE="passphrase"

# Expose a port
EXPOSE 8080

# Run the application
WORKDIR /app
RUN poetry install
CMD [ "poetry", "run", "portrait" ]

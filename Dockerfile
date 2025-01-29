# Use Python 3.10 as the base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy everything into the container
COPY . .

# Upgrade pip and install flake8 (norminette)
RUN pip install --upgrade pip setuptools wheel \
    && pip install flake8

# Default command when running the container
ENTRYPOINT ["/bin/bash"]

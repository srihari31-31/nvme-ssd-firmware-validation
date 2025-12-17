FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3 python3-pip nvme-cli \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

CMD ["python3", "run_validation.py"]

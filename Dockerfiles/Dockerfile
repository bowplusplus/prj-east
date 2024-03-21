FROM ubuntu:22.04 as dev

WORKDIR /app

RUN apt update && apt install -y \
    python3 \
    python3-pip \
    curl \
    wget \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip3 install pandas dbt dbt-duckdb prefect dagster duckdb pytest

CMD ["tail", "-f", "/dev/null"]
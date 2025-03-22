FROM python:3.11

WORKDIR /app

COPY ./app ./app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y supervisor && rm -rf /var/lib/apt/lists/*

COPY supervisord.conf /etc/supervisord.conf

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
FROM python:3.10

ENV TZ=Singapore

# Place timezone data /etc/timezone
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Running CRON
RUN apt-get update
RUN apt-get install -y cron 
COPY cronms /etc/cron.d/cronms
RUN chmod 0644 /etc/cron.d/cronms
RUN crontab /etc/cron.d/cronms
RUN touch /var/log/cron.log

WORKDIR /app

COPY startup.sh .
RUN chmod +x startup.sh

COPY bus.sh .
RUN chmod +x bus.sh

COPY .env .

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["bash", "./startup.sh"]
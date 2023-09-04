# FROM python:3.10

# RUN apt-get update && apt-get install cron -y 

# WORKDIR /app

# COPY requirements.txt .

# COPY ./startup.sh .
# RUN chmod +x startup.sh

# RUN (crontab -l -u root; echo "* 0-2,10-23 * * * echo 'Hello' >> /app/logs/cron.log") | crontab

# # COPY ./cronjobs /etc/cron.d/my-cron-file
# # RUN chmod 0644 /etc/cron.d/my-cron-file
# # RUN crontab /etc/cron.d/my-cron-file


# RUN pip install -r requirements.txt
# CMD ["sh", "./startup.sh"]

FROM python:3.10

ENV TZ=Singapore

# place timezone data /etc/timezone
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

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

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["bash", "./startup.sh"]
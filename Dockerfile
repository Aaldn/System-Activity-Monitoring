FROM debian:bullseye-slim

RUN apt-get update && apt-get -y install python3 python3-pip cron nano

COPY app app
COPY cron/log.sh /etc/cron.d/log.sh

# python commands will be executed from "app" directory
RUN echo "export PYTHONPATH=/app" >> ~/.bashrc

RUN python3 -m pip install -r app/requirements.txt

RUN chmod 0744 /etc/cron.d/log.sh

# setup tasks
RUN crontab /etc/cron.d/log.sh

# the file passed to "tail" command is the last modified log file
# "sed" is used to remove special characters
CMD cron -f && tail -f $(echo "$(ls -Art | tail -n 1)" | sed -r "s/\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]//g")
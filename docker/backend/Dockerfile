# docker/backend/Dockerfile

FROM python:3.6

WORKDIR /app
ADD ./backend/village-profile/requirements.txt /app/backend/


RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install -r backend/requirements.txt

ADD ./docker /app/docker
ADD ./backend /app/backend
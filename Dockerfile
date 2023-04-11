# pull official base image
FROM python:3.9.6-alpine

# set work directory
WORKDIR /usr/src

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/entrypoint.sh
RUN chmod +x /usr/src/entrypoint.sh
# copy project
COPY . .

# run entrypoint.sh
RUN ash entrypoint.sh
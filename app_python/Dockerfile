FROM python:3.9-slim
MAINTAINER Marina Smirnova "m.smirnova@innopolis.university"

# Use of non root user account
#RUN addgroup -S user && adduser -S user -G user
#USER user

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT ["python"]
CMD ["main.py"]
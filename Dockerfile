FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-dev build-essential

WORKDIR /src

COPY src/ /src/

EXPOSE 5000

CMD ["python3", "/src/task_manager.py"]

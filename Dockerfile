FROM jenkins:v1.0

RUN sudo rm -rf /var/lib/apt/lists/*
RUN sudo apt-get update -y
RUN sudo apt upgrade -y
RUN sudo apt install -y golang
RUN sudo mkdir /home/go_sample

COPY . /home/go_sample

WORKDIR /home/go_sample

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "hello.py" ]

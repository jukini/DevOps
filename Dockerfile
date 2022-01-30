FROM jenkins

MINTAINER "slurvian013@gmail.com"

RUN sudo apt-get update -y && \
    sudo apt update && sudo apt upgrade -y && \
    sudo apt install golang && \
    sudo mkdir /home/go_sample

COPY . /home/go_sample

WORKDIR /home/go_sample

RUN go run go_web.go 

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "hello.py" ]

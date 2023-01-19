FROM alpine:latest

RUN mkfifo /tmp/fifo

CMD while true; do echo -e "HTTP/1.1 200 OK\n\n{"status": "OK"}" | nc -l -w 1 -p 8000; done

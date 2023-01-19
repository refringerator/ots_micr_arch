FROM alpine:latest

RUN mkfifo /tmp/fifo

CMD while true; do \
	echo -e "HTTP/1.1 200 OK\n\n" >/tmp/fifo | \
	nc -l -k -w 1 -p 8000 < /tmp/fifo | \
	grep "GET /health/" | \
	awk '/GET/ {print "{\"status\": \"OK\"}"}' > /tmp/fifo ; \
	done

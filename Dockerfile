FROM alpine:latest

RUN mkfifo /tmp/fifo

CMD while true; do \
	nc -lk -w 1 -p 8000 < /tmp/fifo | \
	grep "GET" | \
	awk -v host=$HOSTNAME 'BEGIN {print "HTTP/1.1 200 OK\n" } {print ($2 == "\/health\/")? "{\"status\": \"OK\"}" : "Hello from " host "!"; exit 0 }' >/tmp/fifo ; \	
	done

FROM alpine:3.7

RUN apk add --no-cache bash curl

RUN curl https://getcaddy.com | bash -s personal tls.dns.digitalocean

EXPOSE 80 443

WORKDIR /root
COPY Caddyfile .

ENTRYPOINT ["/usr/local/bin/caddy"]
CMD ["--log", "stdout", "--env"]

# Bookshop

Required parameters

backend:
* `SECRET`
* `POSTGRES_USER`
* `POSTGRES_PASSWORD`
* `POSTGRES_DB`

proxy:
* `FRONTEND_URL`
* `FRONTEND_URL_WWW`
* `BACKEND_URL`
* `ACCESS_CONTROL_ALLOW_ORIGIN`
* `TLS`
* `DO_AUTH_TOKEN`

db:
* `POSTGRES_USER`
* `POSTGRES_PASSWORD`
* `POSTGRES_DB`

---
## Build

1. `docker-compose build `
2. `docker-compose up`

## Dev

1. `docker-compose -f docker-compose-dev.yml build`
2. `docker-compose -f docker-compose-dev.yml up`

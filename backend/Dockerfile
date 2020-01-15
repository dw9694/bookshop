FROM python:3.7-slim

RUN mkdir -p /opt/services/backend
WORKDIR /opt/services/backend
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["gunicorn", "--bind", ":8000", "backend.wsgi:application"]

# syntax=docker/dockerfile:1
FROM python:3.11-slim

# no .pyc, unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

WORKDIR /app

# install deps
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# copy source
COPY app/ /app/app/

# expose app port
EXPOSE 8000

# run flask app with production WSGI server
# entry points to the factory function in app/server.py
CMD ["waitress-serve", "--host=0.0.0.0", "--port=8000", "--call", "app.server:create_app"]

FROM python:3.12-slim

WORKDIR /app

COPY fibonacci.py .

CMD ["python3", "fibonacci.py"]

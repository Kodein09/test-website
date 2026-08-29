#STEP 1: BUILDER
FROM python:3.12-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY requirements.txt .

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /backend/wheels -r requirements.txt


#STEP 2: RUNNER
FROM python:3.12-slim as runner

WORKDIR /app

COPY --from=builder /backend/wheels /wheels

COPY requirements.txt .

RUN pip install --no-cache-dir /wheels/*

COPY . /app

CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "5000"]
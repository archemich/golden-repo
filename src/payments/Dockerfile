FROM python:3.13-slim


WORKDIR /app
COPY shared/ /app/shared

WORKDIR /app/payments
COPY payments/ .

RUN pip install uv

EXPOSE 8000
ENTRYPOINT ["uv", "run", "golden-payments"]

HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD curl -f http://localhost:8000/ || exit 1

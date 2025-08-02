FROM python:3.13-slim

WORKDIR /api
COPY . .
RUN pip install uv

EXPOSE 8000
ENTRYPOINT ["uv", "run", "golden-api"]
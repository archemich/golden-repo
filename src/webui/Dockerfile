FROM python:3.13-slim

WORKDIR /app
COPY shared/ /app/shared

WORKDIR /app/webui
COPY webui/ .
RUN pip install uv

EXPOSE 8501
ENTRYPOINT ["uv", "run", "streamlit", "run", "./golden/webui/main.py"]
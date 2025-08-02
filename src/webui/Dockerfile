FROM python:3.13-slim

WORKDIR /webui
COPY . .
RUN pip install uv

EXPOSE 8501
ENTRYPOINT ["uv", "run", "streamlit", "run", "./golden/webui/main.py"]
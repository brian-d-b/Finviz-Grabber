FROM python:3.8.5-slim-buster
WORKDIR /python-docker
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "./uploadHeatmap.py"]
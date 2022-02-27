FROM python:3.8
COPY . .
RUN /usr/local/bin/python -m pip install -q flask
EXPOSE 8081
ENTRYPOINT ["python3", "app.py"]

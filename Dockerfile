FROM python:3.9.7-slim-buster
WORKDIR /app
RUN chmod 777 /app
RUN python3 -m pip install -U pip
COPY . .
RUN pip3 install --no-cache-dir -U -r requirements.txt
CMD ["bash", "start"]

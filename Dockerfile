FROM python:3.9.6-slim-buster
WORKDIR /app
RUN chmod 777 /app
RUN python3 -m pip install -U pip
COPY requirements.txt ./
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD ["bash","start"]

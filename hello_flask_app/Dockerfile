
#### stage 1: build the flask app image

FROM python:3.8-slim AS build
WORKDIR /app
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libmariadb-dev \
    pkg-config

COPY . . 

RUN pip install flask mysqlclient
#### stage 2: prod

FROM python:3.8-slim 

WORKDIR /app

RUN apt-get update && apt-get install -y libmariadb3 && rm -rf /var/lib/apt/lists/*

COPY --from=build /app /app

COPY --from=build /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=build /usr/local/bin /usr/local/bin

EXPOSE 5000

CMD ["python", "app.py"]




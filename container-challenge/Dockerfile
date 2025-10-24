##### stage 1: build the flask app image with redis
FROM python:3.8-slim AS build
WORKDIR /app
RUN apt-get update && apt-get install -y gcc python3-dev pkg-config
COPY . .
RUN pip install --no-cache-dir flask redis

##### stage 2: prod
FROM python:3.8-slim
WORKDIR /app
COPY --from=build /app /app
COPY --from=build /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=build /usr/local/bin /usr/local/bin
EXPOSE 5001
CMD ["python", "app.py"]

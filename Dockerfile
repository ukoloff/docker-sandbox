FROM python:3-alpine

WORKDIR web-server

COPY . .

CMD ["python", "web" ]

EXPOSE 80

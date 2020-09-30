FROM python:3-alpine

COPY web web

CMD ["python", "web" ]

EXPOSE 80

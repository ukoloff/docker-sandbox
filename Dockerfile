FROM python:3-alpine

COPY web .

CMD ["python", "web" ]

EXPOSE 80

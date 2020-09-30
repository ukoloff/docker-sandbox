FROM python:3-alpine

COPY *.py .

CMD ["python", "web" ]

EXPOSE 80

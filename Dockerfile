FROM python:3-alpine

COPY *.py .

CMD ["python", "web.py" ]

EXPOSE 80

FROM node:lts-alpine

COPY index.js .

CMD ["node", "." ]

EXPOSE 80

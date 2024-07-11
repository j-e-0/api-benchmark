FROM node:14

WORKDIR /app

COPY package.json /app
COPY . /app

RUN npm install

CMD ["node", "app.js"]

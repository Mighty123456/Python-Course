FROM node:18-alpine

WORKDIR /app

COPY package.json .
RUN npm install --production

COPY . .

EXPOSE 3000

ENV PORT=3000
ENV BACKEND_URL=http://localhost:5000

CMD ["node", "server.js"]

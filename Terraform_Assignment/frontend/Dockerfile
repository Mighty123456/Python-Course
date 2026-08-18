FROM node:18-alpine

WORKDIR /app

COPY . .
RUN npm install --production

EXPOSE 3000

ENV PORT=3000
ENV BACKEND_URL=http://localhost:5000

CMD ["npm", "start"]

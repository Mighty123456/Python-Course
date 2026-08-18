# Line 1: Use official Node 18 Alpine image for minimal container size and security
FROM node:18-alpine

# Line 2: Create application working directory
WORKDIR /app

# Line 3: Copy package definition first to optimize layer caching
COPY package.json .

# Line 4: Install only production dependencies
RUN npm install --production

# Line 5: Copy application source code into the container image
COPY . .

# Line 6: Expose port 3000 for Node Express web server
EXPOSE 3000

# Line 7: Define default environment variables
ENV PORT=3000
ENV BACKEND_URL=http://flask-backend-service:5000

# Line 8: Execute Node server command when container starts
CMD ["node", "server.js"]

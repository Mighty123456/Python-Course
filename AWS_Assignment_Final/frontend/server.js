const express = require('express');
const axios = require('axios');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;
const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:5000';

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// log every request so i can trace issues in ec2 logs
app.use((req, res, next) => {
  console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`);
  next();
});

app.get('/', async (req, res) => {
  let backendData = null;
  let backendStatus = 'Disconnected';
  let responseTime = null;
  const t0 = Date.now();

  try {
    console.log(`Trying to reach backend at ${BACKEND_URL}/api/data`);
    const resp = await axios.get(`${BACKEND_URL}/api/data`, {
      timeout: 4000,
      headers: { Accept: 'application/json' }
    });
    responseTime = Date.now() - t0;
    backendData = resp.data;
    backendStatus = 'Connected';
    console.log(`Backend OK - ${responseTime}ms`);
  } catch (err) {
    console.error(`Could not reach backend: ${err.message}`);
    backendStatus = `Error (${err.code || err.message})`;
  }

  res.render('index', {
    backendStatus,
    backendData,
    backendUrl: BACKEND_URL,
    responseTime: responseTime ? `${responseTime}ms` : 'N/A'
  });
});

// health check for ALB / ECS target group
app.get('/health', (req, res) => {
  res.status(200).json({
    status: 'healthy',
    service: 'express-frontend',
    backend_target: BACKEND_URL,
    uptime: Math.floor(process.uptime())
  });
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`Express server started on port ${PORT}`);
  console.log(`Backend URL configured as: ${BACKEND_URL}`);
});

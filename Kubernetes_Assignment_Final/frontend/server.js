const express = require('express');
const axios = require('axios');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;
const BACKEND_URL = process.env.BACKEND_URL || 'http://flask-backend-service:5000';

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.get('/', async (req, res) => {
  let backendData = null;
  let backendStatus = 'Disconnected';

  try {
    const response = await axios.get(`${BACKEND_URL}/api/data`, { timeout: 3000 });
    backendData = response.data;
    backendStatus = 'Connected';
  } catch (err) {
    console.log(`Backend link failed: ${err.message}`);
  }

  res.render('index', {
    backendStatus,
    backendData,
    backendUrl: BACKEND_URL
  });
});

// Health check endpoint for Kubernetes liveness & readiness probes
app.get('/healthz', (req, res) => {
  res.status(200).json({ status: 'healthy', app: 'express-frontend' });
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`Frontend running on port ${PORT}`);
  console.log(`Connecting to backend at ${BACKEND_URL}`);
});

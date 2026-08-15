const express = require('express');
const axios = require('axios');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;
const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:5000';

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', async (req, res) => {
  let backendData = null;
  let backendStatus = 'Disconnected';

  try {
    const response = await axios.get(`${BACKEND_URL}/api/data`, { timeout: 3000 });
    backendData = response.data;
    backendStatus = 'Connected';
  } catch (error) {
    console.error('Backend connection failed:', error.message);
  }

  res.render('index', {
    backendStatus,
    backendData,
    backendUrl: BACKEND_URL
  });
});

app.get('/health', (req, res) => {
  res.status(200).json({ status: 'healthy', service: 'Express Frontend' });
});

app.listen(PORT, () => {
  console.log(`Express Frontend running on port ${PORT}`);
  console.log(`Connected to Flask Backend at: ${BACKEND_URL}`);
});

import express from 'express';
import axios from 'axios';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3000;
const BACKEND_URL = process.env.BACKEND_URL || 'http://localhost:5000';

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.get('/', async (req, res) => {
  let backendData = null;
  let backendStatus = 'Disconnected';

  try {
    const response = await axios.get(`${BACKEND_URL}/api/health`, { timeout: 3000 });
    backendStatus = response.data.status === 'healthy' ? 'Connected' : 'Disconnected';
  } catch (err) {
    console.error('Backend connection failed:', err.message);
  }

  res.render('index', { backendStatus, backendUrl: BACKEND_URL });
});

app.get('/health', (req, res) => {
  res.status(200).json({ status: 'healthy', service: 'Express Frontend' });
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`Frontend running on port ${PORT}`);
  console.log(`Targeting backend at: ${BACKEND_URL}`);
});

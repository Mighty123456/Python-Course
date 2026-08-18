// pm2 ecosystem configuration file
// Run all apps:     pm2 start ecosystem.config.js
// Reload all apps:  pm2 reload ecosystem.config.js
// Stop all apps:    pm2 stop ecosystem.config.js
// Delete all apps:  pm2 delete ecosystem.config.js
// Save process list: pm2 save
// Enable startup:   pm2 startup  (then run the printed command as sudo)

module.exports = {
  apps: [
    {
      // ─── Flask REST API (Backend) ───────────────────────────────────────────
      name        : 'flask-backend',
      script      : 'venv/bin/gunicorn',
      interpreter : 'none',
      args        : '-w 2 -b 0.0.0.0:5000 app:app',
      cwd         : './backend',
      env: {
        FLASK_ENV : 'production',
        PORT      : '5000',
      },
      // pm2 runtime options
      autorestart : true,
      watch       : false,
      max_memory_restart: '200M',
      error_file  : './logs/flask-backend-error.log',
      out_file    : './logs/flask-backend-out.log',
      log_date_format: 'YYYY-MM-DD HH:mm:ss',
    },

    {
      // ─── Express Web App (Frontend) ─────────────────────────────────────────
      name    : 'express-frontend',
      script  : 'server.js',
      cwd     : './frontend',
      env: {
        NODE_ENV    : 'production',
        PORT        : '3000',
        BACKEND_URL : 'http://localhost:5000',
      },
      // pm2 runtime options
      autorestart : true,
      watch       : false,
      max_memory_restart: '200M',
      error_file  : './logs/express-frontend-error.log',
      out_file    : './logs/express-frontend-out.log',
      log_date_format: 'YYYY-MM-DD HH:mm:ss',
    },
  ],
};

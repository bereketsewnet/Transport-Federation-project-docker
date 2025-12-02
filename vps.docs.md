# 🎯 VPS Service Management Cheat Sheet

This document contains safe commands to manage your **Node.js APIs, Telegram bot, and frontend** deployed on a VPS with `systemd` and Nginx.

---

## 1️⃣ Node.js APIs

### Betting Transaction API
**Service name:** `betting-api`

| Action | Command |
|--------|---------|
| Start | `sudo systemctl start betting-api` |
| Stop | `sudo systemctl stop betting-api` |
| Restart | `sudo systemctl restart betting-api` |
| Reload (after changing service file) | `sudo systemctl daemon-reload && sudo systemctl restart betting-api` |
| Enable on boot | `sudo systemctl enable betting-api` |
| Disable on boot | `sudo systemctl disable betting-api` |
| Check status | `sudo systemctl status betting-api` |
| View live logs | `sudo journalctl -u betting-api -f` |
| View last 50 log lines | `sudo journalctl -u betting-api -n 50` |
| Delete service (stop + remove) | `sudo systemctl stop betting-api && sudo systemctl disable betting-api && sudo rm /etc/systemd/system/betting-api.service && sudo systemctl daemon-reload` |

---

## 2️⃣ Telegram Bot

### Betting Telegram Bot
**Service name:** `betting-bot`

| Action | Command |
|--------|---------|
| Start | `sudo systemctl start betting-bot` |
| Stop | `sudo systemctl stop betting-bot` |
| Restart | `sudo systemctl restart betting-bot` |
| Reload (after changing service file) | `sudo systemctl daemon-reload && sudo systemctl restart betting-bot` |
| Enable on boot | `sudo systemctl enable betting-bot` |
| Disable on boot | `sudo systemctl disable betting-bot` |
| Check status | `sudo systemctl status betting-bot` |
| View live logs | `sudo journalctl -u betting-bot -f` |
| View last 50 log lines | `sudo journalctl -u betting-bot -n 50` |
| Delete service | `sudo systemctl stop betting-bot && sudo systemctl disable betting-bot && sudo rm /etc/systemd/system/betting-bot.service && sudo systemctl daemon-reload` |

---

## 3️⃣ Frontend (Vite React)

Frontend is served via **Nginx** (e.g., `/betting` or `/tcwf`).  
You can reload Nginx safely after changing configs:

| Action | Command |
|--------|---------|
| Reload Nginx config | `sudo nginx -t && sudo systemctl reload nginx` |
| Restart Nginx | `sudo systemctl restart nginx` |
| Check status | `sudo systemctl status nginx` |
| View logs | `sudo tail -f /var/log/nginx/error.log` |
| Access frontend | Open your browser: `http://<your-vps-ip>/<path>` |

---

## 4️⃣ Useful Tips

- Always **check folder permissions** if Node.js or Python services fail to write files.  
  Example: `sudo chown -R www-data:www-data /var/www/betting/betting_transaction_api`
- After modifying `.env` files, **restart the service** to apply changes.
- For TypeScript Node.js API, make sure `dist/` folder exists. If not, build manually:
  ```bash
  cd /var/www/betting/betting_transaction_api
  npm install
  npm run build
For Python bot, ensure the virtual environment is activated in the service:
ExecStart=/var/www/betting/betting_transaction_bot/venv/bin/python /var/www/betting/betting_transaction_bot/app/bot.py


### Quick Summary
# Node API
sudo systemctl restart betting-api
sudo journalctl -u betting-api -f

# Telegram Bot
sudo systemctl restart betting-bot
sudo journalctl -u betting-bot -f

# Frontend / Nginx
sudo nginx -t
sudo systemctl reload nginx
sudo tail -f /var/log/nginx/error.log


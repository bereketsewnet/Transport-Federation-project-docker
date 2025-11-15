# 🐳 Docker Containerization Summary

Your entire Betting Payment Manager stack has been successfully containerized! Here's what was created:

## 📦 Created Files

### Root Directory
- **`docker-compose.yml`** - Main orchestration file for all services
- **`.env.example`** - Environment variables template
- **`.gitignore`** - Git ignore rules
- **`start.sh`** - Quick start script
- **`stop.sh`** - Quick stop script
- **`DOCKER_SETUP.md`** - Comprehensive setup guide
- **`README_DOCKER.md`** - Quick reference guide

### API (betting_transaction_api)
- **`Dockerfile`** - Multi-stage build for Node.js API
- **`.dockerignore`** - Files to exclude from build
- **`docker-entrypoint.sh`** - Startup script with migration handling

### Frontend (betting_transaction_ui)
- **`Dockerfile`** - Multi-stage build with Nginx
- **`.dockerignore`** - Files to exclude from build
- (Uses existing `nginx.conf`)

### Bot (betting_transaction_bot)
- **`Dockerfile`** - Python bot container
- **`.dockerignore`** - Files to exclude from build

## 🚀 Services & Ports

| Service | Container Name | Port | Description |
|---------|---------------|------|-------------|
| MySQL | `betting_mysql` | 3307 | Database server |
| Adminer | `betting_adminer` | 8081 | Database GUI |
| API | `betting_api` | 3001 | Express.js REST API |
| Frontend | `betting_frontend` | 5174 | React web app |
| Bot | `betting_bot` | - | Telegram bot (polling) |

## 🔧 Key Features

### ✅ Automatic Database Setup
- MySQL container with health checks
- Automatic migrations on API startup
- Persistent data volumes

### ✅ Environment Configuration
- Centralized `.env` file
- Build-time variables for frontend
- Runtime variables for all services

### ✅ Network Isolation
- All services on `betting_network`
- Service-to-service communication via service names
- External access via mapped ports

### ✅ Data Persistence
- `mysql_data` - Database files
- `api_uploads` - Uploaded files
- `bot_data` - Bot SQLite database

## 📋 Quick Start

```bash
# 1. Copy environment file
cp .env.example .env

# 2. Start all services
./start.sh

# OR
docker-compose up -d --build

# 3. Seed database (optional)
docker-compose exec api npm run db:seed
```

## 🔍 Access Points

- **Frontend**: http://localhost:5174
- **API**: http://localhost:3001/api/v1
- **Health Check**: http://localhost:3001/health
- **Adminer**: http://localhost:8081
  - Server: `mysql`
  - User: `bettingadminuser`
  - Password: `~HNiBgmo56wag~y3`
  - Database: `rynobet_betting_db`

## 🛠 Common Operations

### View Logs
```bash
docker-compose logs -f [service_name]
```

### Restart Service
```bash
docker-compose restart [service_name]
```

### Rebuild Service
```bash
docker-compose build [service_name]
docker-compose up -d [service_name]
```

### Stop Everything
```bash
docker-compose down
```

### Stop and Remove Data
```bash
docker-compose down -v  # ⚠️ Deletes all data
```

## 🔐 Default Credentials

After seeding:
- **Admin**: `admin@example.com` / `AdminPass123!`
- **Agent**: `agent@example.com` / `AgentPass123!`

## 📝 Environment Variables

Key variables in `.env`:
- `MYSQL_ROOT_PASSWORD` - MySQL root password
- `MYSQL_DATABASE` - Database name
- `TELEGRAM_BOT_TOKEN` - Bot token
- `JWT_SECRET` - JWT secret (change in production!)
- `VITE_API_BASE_URL` - Frontend API URL
- `VITE_SOCKET_URL` - Frontend Socket URL

## 🎯 What's Different from Local Setup

1. **Ports**: Using odd ports (3001, 5174, 3307, 8081) to avoid conflicts
2. **Database**: MySQL runs in container, accessible at `mysql:3306` internally
3. **Networking**: Services communicate via Docker network
4. **Build**: Frontend built at container build time with environment variables
5. **Migrations**: Run automatically on API startup

## 🐛 Troubleshooting

### Port Conflicts
If ports are in use, change them in `docker-compose.yml`:
```yaml
ports:
  - "3002:3000"  # Change external port
```

### Database Connection Issues
1. Wait for MySQL health check to pass
2. Check logs: `docker-compose logs mysql`
3. Verify credentials in `.env`

### Frontend Can't Connect
1. Rebuild frontend with correct API URL:
   ```bash
   docker-compose build frontend
   docker-compose up -d frontend
   ```

### Bot Not Responding
1. Check bot token in `.env`
2. Verify API is accessible: `docker-compose exec bot curl http://api:3000/health`
3. Check logs: `docker-compose logs -f bot`

## 📚 Documentation

- **Full Setup Guide**: See `DOCKER_SETUP.md`
- **Quick Reference**: See `README_DOCKER.md`
- **API Docs**: See `betting_transaction_api/README.md`
- **Frontend Docs**: See `betting_transaction_ui/README.md`
- **Bot Docs**: See `betting_transaction_bot/README.md`

## ✨ Next Steps

1. **Review `.env`** - Update with your actual values
2. **Start services** - Run `./start.sh` or `docker-compose up -d`
3. **Seed database** - Run `docker-compose exec api npm run db:seed`
4. **Test access** - Visit http://localhost:5174
5. **Configure bot** - Update `TELEGRAM_BOT_TOKEN` if needed

---

**🎉 Your entire stack is now containerized and ready to run!**


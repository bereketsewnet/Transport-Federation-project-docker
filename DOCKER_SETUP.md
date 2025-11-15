# Docker Setup Guide

This guide will help you run the entire Betting Payment Manager stack using Docker Compose.

## 🚀 Quick Start

### Prerequisites

- Docker Desktop (or Docker Engine + Docker Compose)
- At least 4GB of available RAM
- Ports available: 3001, 5174, 3307, 8081

### 1. Clone and Navigate

```bash
cd /path/to/betting
```

### 2. Configure Environment

Copy the `.env` file and customize if needed:

```bash
cp .env .env.local  # Optional: create local override
```

**Important**: Update `TELEGRAM_BOT_TOKEN` with your actual bot token if different.

### 3. Start All Services

```bash
docker-compose up -d
```

This will start:
- **MySQL Database** on port `3307`
- **Adminer** (Database GUI) on port `8081`
- **Backend API** on port `3001`
- **Frontend UI** on port `5174`
- **Telegram Bot** (polling mode)

### 4. Initialize Database

The API will automatically run migrations on startup. To seed the database:

```bash
docker-compose exec api npm run db:seed
```

### 5. Access Services

- **Frontend**: http://localhost:5174
- **Backend API**: http://localhost:3001/api/v1
- **API Health**: http://localhost:3001/health
- **Adminer**: http://localhost:8081
  - Server: `mysql`
  - Username: `bettingadminuser`
  - Password: `~HNiBgmo56wag~y3`
  - Database: `rynobet_betting_db`

## 📋 Service Details

### Ports Used

| Service | Port | Description |
|---------|------|-------------|
| Frontend | 5174 | React web application |
| API | 3001 | Express.js REST API |
| MySQL | 3307 | Database server |
| Adminer | 8081 | Database management GUI |

### Default Credentials

After seeding, you can login with:

- **Admin**: `admin@example.com` / `AdminPass123!`
- **Agent**: `agent@example.com` / `AgentPass123!`

## 🛠 Common Commands

### View Logs

```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f api
docker-compose logs -f frontend
docker-compose logs -f bot
docker-compose logs -f mysql
```

### Stop Services

```bash
docker-compose stop
```

### Stop and Remove Containers

```bash
docker-compose down
```

### Stop and Remove Everything (including volumes)

```bash
docker-compose down -v
```

### Rebuild Services

```bash
# Rebuild all
docker-compose build

# Rebuild specific service
docker-compose build api
docker-compose build frontend
docker-compose build bot

# Rebuild and restart
docker-compose up -d --build
```

### Run Commands in Containers

```bash
# Run migrations
docker-compose exec api npm run migrate

# Run seeds
docker-compose exec api npm run db:seed

# undo seeds
docker-compose exec api npm run migrate:undo

# Access API container shell
docker-compose exec api sh

# Access MySQL
docker-compose exec mysql mysql -u bettingadminuser -p rynobet_betting_db

# Access Bot container
docker-compose exec bot sh
```

## 🔧 Configuration

### Environment Variables

All environment variables are defined in the root `.env` file. Key variables:

- `MYSQL_ROOT_PASSWORD`: MySQL root password
- `MYSQL_DATABASE`: Database name
- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token
- `JWT_SECRET`: Secret for JWT tokens (change in production!)

### Network

All services are on the `betting_network` bridge network. Services can communicate using service names:

- API: `http://api:3000`
- MySQL: `mysql:3306`
- Frontend: `http://frontend:80`

## 🗄 Database Management

### Using Adminer

1. Open http://localhost:8081
2. Select **MySQL** as system
3. Enter:
   - Server: `mysql`
   - Username: `bettingadminuser`
   - Password: `~HNiBgmo56wag~y3`
   - Database: `rynobet_betting_db`
4. Click **Login**

### Database Backup

```bash
# Backup
docker-compose exec mysql mysqldump -u bettingadminuser -p~HNiBgmo56wag~y3 rynobet_betting_db > backup.sql

# Restore
docker-compose exec -T mysql mysql -u bettingadminuser -p~HNiBgmo56wag~y3 rynobet_betting_db < backup.sql
```

## 🐛 Troubleshooting

### Services Won't Start

1. Check if ports are available:
   ```bash
   lsof -i :3001
   lsof -i :5174
   lsof -i :3307
   lsof -i :8081
   ```

2. Check logs:
   ```bash
   docker-compose logs
   ```

### Database Connection Issues

1. Wait for MySQL to be healthy (check logs)
2. Verify credentials in `.env`
3. Check network connectivity:
   ```bash
   docker-compose exec api ping mysql
   ```

### API Migration Errors

```bash
# Run migrations manually
docker-compose exec api npm run migrate

# Check migration status
docker-compose exec api npx sequelize-cli db:migrate:status
```

### Bot Not Responding

1. Check bot token in `.env`
2. Verify API is accessible:
   ```bash
   docker-compose exec bot curl http://api:3000/health
   ```
3. Check bot logs:
   ```bash
   docker-compose logs -f bot
   ```

### Frontend Can't Connect to API

1. Verify `VITE_API_BASE_URL` in `.env`
2. Check CORS settings in API
3. Ensure API is running:
   ```bash
   docker-compose ps
   ```

## 📦 Volumes

Data is persisted in Docker volumes:

- `mysql_data`: MySQL database files
- `api_uploads`: API uploaded files
- `bot_data`: Bot SQLite database

To view volumes:
```bash
docker volume ls
```

To remove volumes (⚠️ deletes data):
```bash
docker-compose down -v
```

## 🔄 Development Workflow

### Hot Reload (Development)

For development with hot reload, you may want to mount source code:

```yaml
# In docker-compose.yml, add volumes to api service:
volumes:
  - ./betting_transaction_api/src:/app/src
  - ./betting_transaction_api/config:/app/config
```

Then rebuild:
```bash
docker-compose up -d --build api
```

### Running Tests

```bash
# API tests
docker-compose exec api npm test

# Bot tests
docker-compose exec bot pytest tests/
```

## 🚀 Production Deployment

For production:

1. Set `NODE_ENV=production` in `.env`
2. Change `JWT_SECRET` to a strong random value
3. Set strong MySQL passwords
4. Configure proper CORS origins
5. Use environment-specific `.env` files
6. Enable webhook mode for bot if needed
7. Set up SSL/TLS certificates
8. Configure proper backup strategy

## 📝 Notes

- The bot runs in **polling mode** by default. For production, consider webhook mode.
- Adminer is lightweight and perfect for database management.
- All services restart automatically unless stopped manually.
- Health checks ensure services start in the correct order.

---

## stop all docker ports then remove (when port alsredy eixt to cut like 5173)
docker stop $(docker ps -q)
docker rm $(docker ps -aq)

## network verficiaon
sudo lsof -i :5173
sudo kill -9 <PID>
docker system prune -a --volumes -f


cd /var/www/betting

# Option 1: Undo and re-seed everything
docker-compose exec api npm run db:seed:undo
docker-compose exec api npm run db:seed

# Option 2: Use setup command (migrates + seeds)
docker-compose exec api npm run setup:docker



**Happy Coding! 🎉**


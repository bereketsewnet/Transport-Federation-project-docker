# 🐳 Docker Setup - Quick Reference

## Quick Start

```bash
# 1. Copy environment file
cp .env.example .env

# 2. Start all services
./start.sh

# OR manually:
docker-compose up -d --build
```

## Services & Ports

| Service | Port | URL |
|---------|------|-----|
| Frontend | 5174 | http://localhost:5174 |
| API | 3001 | http://localhost:3001/api/v1 |
| MySQL | 3307 | localhost:3307 |
| Adminer | 8081 | http://localhost:8081 |

## Adminer Login

- **System**: MySQL
- **Server**: `mysql`
- **Username**: `bettingadminuser`
- **Password**: `~HNiBgmo56wag~y3`
- **Database**: `rynobet_betting_db`

## Common Commands

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f [service_name]

# Rebuild a service
docker-compose build [service_name]
docker-compose up -d [service_name]

# Run migrations
docker-compose exec api npm run migrate

# Seed database
docker-compose exec api npm run db:seed

# Access container shell
docker-compose exec [service_name] sh
```

## Default Login Credentials

- **Admin**: `admin@example.com` / `AdminPass123!`
- **Agent**: `agent@example.com` / `AgentPass123!`

## Troubleshooting

### Port Already in Use
```bash
# Check what's using the port
lsof -i :3001
lsof -i :5174
lsof -i :3307
lsof -i :8081
```

### Services Not Starting
```bash
# Check logs
docker-compose logs

# Restart specific service
docker-compose restart [service_name]
```

### Database Issues
```bash
# Reset database (⚠️ deletes all data)
docker-compose down -v
docker-compose up -d
docker-compose exec api npm run migrate
docker-compose exec api npm run db:seed
```

For detailed documentation, see [DOCKER_SETUP.md](./DOCKER_SETUP.md)


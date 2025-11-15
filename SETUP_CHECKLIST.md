# ✅ Docker Setup Checklist

Follow these steps to get your containerized stack running:

## Pre-Flight Checks

- [ ] Docker Desktop is installed and running
- [ ] At least 4GB RAM available
- [ ] Ports 3001, 5174, 3307, 8081 are free

## Setup Steps

### 1. Environment Configuration
- [ ] Copy `.env.example` to `.env`:
  ```bash
  cp .env.example .env
  ```
- [ ] Review `.env` file and update if needed:
  - [ ] `TELEGRAM_BOT_TOKEN` - Your actual bot token
  - [ ] `JWT_SECRET` - Strong secret for production
  - [ ] `MYSQL_ROOT_PASSWORD` - Strong password
  - [ ] `MYSQL_PASSWORD` - Database user password

### 2. Start Services
- [ ] Run the start script:
  ```bash
  ./start.sh
  ```
  OR manually:
  ```bash
  docker-compose up -d --build
  ```

### 3. Verify Services
- [ ] Check all containers are running:
  ```bash
  docker-compose ps
  ```
- [ ] Check API health:
  ```bash
  curl http://localhost:3001/health
  ```
- [ ] Check frontend:
  - [ ] Open http://localhost:5174 in browser
- [ ] Check Adminer:
  - [ ] Open http://localhost:8081
  - [ ] Login with credentials from `.env`

### 4. Database Setup
- [ ] Wait for MySQL to be healthy (check logs)
- [ ] Verify migrations ran (check API logs)
- [ ] Seed database:
  ```bash
  docker-compose exec api npm run db:seed
  ```

### 5. Test Access
- [ ] Frontend loads at http://localhost:5174
- [ ] Can login with default credentials:
  - Admin: `admin@example.com` / `AdminPass123!`
  - Agent: `agent@example.com` / `AgentPass123!`
- [ ] API responds at http://localhost:3001/api/v1
- [ ] Bot is running (check logs):
  ```bash
  docker-compose logs -f bot
  ```

## Troubleshooting

If something doesn't work:

1. **Check logs**:
   ```bash
   docker-compose logs [service_name]
   ```

2. **Restart service**:
   ```bash
   docker-compose restart [service_name]
   ```

3. **Rebuild service**:
   ```bash
   docker-compose build [service_name]
   docker-compose up -d [service_name]
   ```

4. **Full reset** (⚠️ deletes data):
   ```bash
   docker-compose down -v
   docker-compose up -d --build
   docker-compose exec api npm run migrate
   docker-compose exec api npm run db:seed
   ```

## Success Criteria

✅ All containers running  
✅ Frontend accessible  
✅ API health check passes  
✅ Database accessible via Adminer  
✅ Can login to frontend  
✅ Bot is running and connected  

## Next Steps

- [ ] Review `DOCKER_SETUP.md` for detailed documentation
- [ ] Review `DOCKER_SUMMARY.md` for architecture overview
- [ ] Customize environment variables for your needs
- [ ] Set up production configuration
- [ ] Configure backups for database

---

**Once all checks pass, you're ready to go! 🚀**


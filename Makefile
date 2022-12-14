run:
	@docker-compose up -d
stop:
	@docker-compose stop

down:
	@docker-compose down

build:
	@docker-compose build

bash:
	docker-compose exec backend sh

logs-back:
	@docker-compose logs -f backend

logs-db:
	@docker-compose logs -f db

migrations:
	@docker-compose exec backend python3 manage.py makemigrations

migrate:
	@docker-compose exec backend python3 manage.py migrate

test:
	@docker-compose exec backend pytest
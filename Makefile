run:
	uvicorn main:app --reload

pg-up:
	docker compose -f docker_compose_dev.yaml --env-file .env.dev.pg up -d

pg-down:
	docker compose -f docker_compose_dev.yaml --env-file .env.dev.pg down
	docker network prune -f

al-mm:
	alembic revision --autogenerate -m $(c)

al-uh:
	alembic upgrade head
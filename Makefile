run:
	uvicorn main:app --reload

pg-up:
	docker compose -f docker_compose_dev.yaml up -d

pg-down:
	docker compose -f docker_compose_dev.yaml down
	docker network prune -f
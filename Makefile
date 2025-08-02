up:
	docker-compose -f ./deploy/docker-compose.yaml up -d

down:
	docker-compose  -f ./deploy/docker-compose.yaml down

logs:
	docker-compose -f ./deploy/docker-compose.yaml logs -f

lint:
	pre-commit run --all-files
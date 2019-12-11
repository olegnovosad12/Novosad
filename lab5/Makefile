STATES := app tests
REPO := olegnov1203/devops

.PHONY: $(STATES)

$(STATES):
	@docker build -f Dockerfile.$(@) -t $(REPO):$(@) .

run:
	@docker network create --driver=bridge appnet \
	&& docker run --rm --name redis --net=appnet -d redis \
	&& docker run --rm --name app --net=appnet -p 5000:5000 -d $(REPO):app

test-app:
	@docker run --rm -it --name test --net=appnet $(REPO):tests

docker-prune:
	@docker rm $$(docker ps -a -q) --force || true \
	&& docker container prune --force \
	&& docker volume prune --force \
	&& docker network prune --force \
	&& docker image prune --force

docker-clean:
	@docker image prune -a --force
docker-push:
	@docker push olegnov1203/devops:app
	@docker push olegnov1203/devops:tests

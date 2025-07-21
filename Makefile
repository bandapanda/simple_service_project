IMAGE_NAME=simple_service_client
VERSION ?= 1.0.0

build:
	docker build -t $(IMAGE_NAME):$(VERSION) simple_service_client

run-hello:
	docker run \
	-v "$(PWD)/output":/app/output \
	$(IMAGE_NAME):$(VERSION) --mode hello

run-random:
	docker run --rm $(IMAGE_NAME):$(VERSION)  \
	-v $(PWD)/vagrant_project/.vagrant/machines/default/virtualbox/private_key:/root/.ssh/id_rsa:ro \
	-v ~/.ssh/known_hosts:/root/.ssh/known_hosts:ro \
	--mode random

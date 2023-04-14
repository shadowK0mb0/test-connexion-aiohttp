IMAGE_NAME = "testconnexion"

dockerrun:
	docker build -t $(IMAGE_NAME) . --target=dev
	docker run -it --rm -p 8000:8000 $(IMAGE_NAME)

test:
	docker build -t $(IMAGE_NAME):test . --target=test
	docker run -it --rm $(IMAGE_NAME):test
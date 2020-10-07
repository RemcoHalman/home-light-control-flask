# ================================================================== *
# 							  Makefile help							 *
# ================================================================== *

define USAGE
Holiday Countdown ⚙️

Commands:
	BASE:
	build           : Build Docker image
	run             : Run Docker image
	destroy_empty   : Destroy empty docker images
	_____________________________________________
	VUE:
	serve			: Run local Vue instance
	build_vue		: Builds vue app
	fix_vue			: Vue linting
	_____________________________________________
endef

export USAGE

# Makefile Config
PREFIX=remcoha # <change to your name>
APP_NAME=home-light-control-python
IMG_REGISTRY=docker.io/$(PREFIX)
VERSION=0.0.1
LOCAL_PORT=5000
EXPOSE_PORT=3200
IMG_NAME=$(IMG_REGISTRY)/$(APP_NAME):$(VERSION)

# Help Function
help:
	@echo "$$USAGE"

# Docker functions
build:
	docker build -t $(IMG_NAME) .

run:
	docker run -d -p $(EXPOSE_PORT):$(LOCAL_PORT) $(IMG_NAME)

buildrun: build run
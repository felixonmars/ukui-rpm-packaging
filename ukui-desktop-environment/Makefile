
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
all: build  clean

build: 
	@echo ">> building rpms"
	$(DOCKER) run --ulimit=host  --privileged -v `pwd`:/root docker.io/jenningsloy318/ukui-builder:f32  bash  /root/build.sh 

clean:
	@echo ">> clean up"
	rm -rf rpmbuild
	$(DOCKER) container rm -a

.PHONY: build  clean
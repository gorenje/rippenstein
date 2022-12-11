start:
	rm -fr _site
	foreman start web

docker-build:
	docker build -t jekyll .

# beware: Github uses 3.9 but this guys only have 3.8 and 4.0...
start-docker: docker-build
	docker run -it --rm --volume="$$PWD:/srv/jekyll:Z" --publish 127.0.0.1:4000:4000 jekyll jekyll serve --trace --verbose

start-docker-interactive: docker-build
	docker run -it --rm --volume="$$PWD:/srv/jekyll:Z" --publish 127.0.0.1:4000:4000 jekyll /bin/bash

start-docker-network: docker-build
	docker run -it --rm --volume="$$PWD:/srv/jekyll:Z" --publish 192.168.178.41:4000:4000 jekyll jekyll serve

build-horrorscopes:
	rm -fr horrorscope/2*.md
	python3 _tooling/horrorscope.py

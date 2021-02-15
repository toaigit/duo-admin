#!/bin/bash
docker run -ti --rm -v $PWD/scripts:/tmp/workdir --name duo-admin duo-admin /bin/bash

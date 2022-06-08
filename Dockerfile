## Docker Base for modules
# STAGE 1 - Building Dependencies
FROM condaforge/mambaforge-pypy3

# installing build dependencies
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y build-essential gcc


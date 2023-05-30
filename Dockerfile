# Docker Base for modules
FROM condaforge/mambaforge-pypy3

# Installing build dependencies
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y build-essential gcc

# Installing COPT for module solvers
RUN wget -c https://pub.shanshu.ai/download/copt/6.5.3/linux64/CardinalOptimizer-Remote-6.5.3-lnx64.tar.gz -O - | tar -xvz -C /opt/
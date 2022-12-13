# Docker Base for modules
FROM condaforge/mambaforge-pypy3

# Installing build dependencies
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y build-essential gcc

# Installing COPT for module solvers
RUN wget -c https://pub.shanshu.ai/download/copt/6.0.1/linux64/CardinalOptimizer-6.0.1-lnx64.tar.gz -O - | tar -xvz -C /opt/
# Emb3rs GRPC Tools
This repo is to be used to generate the required code to use in the emb3rs project, for gRPC communication.

## Setup Local Environment
Create Conda environment and install packages:
```shell
conda env create -n grpc-module -f environment-py39.yml
conda activate grpc-module
```

## Python gRPC generation
Create Conda environment and install packages:
```shell
conda run python -m grpc_tools.protoc -Iprotos/ \
  --python_out=plibs \
  --grpc_python_out=plibs \
  protos/<module>/<module>.proto
```

## PHP Generation
Requirements:
- protoc
- protobuf
- protoc_php_plugin

if still not enough, check at the links below for more information.
- "https://github.com/grpc/grpc/blob/v1.45.0/src/php/README.md"
- "https://grpc.io/docs/languages/php/quickstart/"
- zsh or bash script (zsh example)
  ```shell
  . generate_php.sh protos/manager/manager.proto
  ```

## Running tests
Server test:
```shell
PYTHONPATH=$PYTHONPATH:plibs python test_server.py
```

Client test:
```shell
PYTHONPATH=$PYTHONPATH:plibs python test_client.py
```

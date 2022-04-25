# Emb3rs GRPC Tools

This repo is to be used to generate the required code to use in the emb3rs project, for gRPC communication.

## Commands

Commands to generate code for the project

### Python Generation


Requirements:

- conda

        $ conda env create -f environment-py310.yml

- zsh or bash script (zsh example)

        $ zsh -i generate_python.sh protos/manager/manager.proto


### PHP Generation

Requirements:

- protoc
- protobuf
- protoc_php_plugin

if still not enough, check at the links below for more information.
- "https://github.com/grpc/grpc/blob/v1.45.0/src/php/README.md"
- "https://grpc.io/docs/languages/php/quickstart/"

- zsh or bash script (zsh example)

        $ zsh -i generate_php.sh protos/manager/manager.proto
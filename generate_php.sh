PHP_PLUGIN=$HOME/.libs/grpc_php_plugin
if [ ! -f "$PHP_PLUGIN" ]; then
    echo "$PHP_PLUGIN does not exist.\n"
    echo "Check if you have the requirements : "
    echo "https://github.com/grpc/grpc/blob/v1.45.0/src/php/README.md"
    echo "https://grpc.io/docs/languages/php/quickstart/"
    exit
fi

if [ $# -eq 0 ]
  then
    echo "No arguments supplied, Need Path to proto.file"
    exit
fi

protoc -I=protos \
--php_out=./php \
--grpc_out=./php \
--plugin=protoc-gen-grpc=$PHP_PLUGIN \
$1
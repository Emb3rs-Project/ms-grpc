
# Checking for Arguments
if [ $# -eq 0 ]
  then
    echo "No arguments supplied, Need Path to proto.file"
    exit
fi

# Activate Conda GRPC Environment
conda activate grpc-module

# Generate Python Files/Update them
python -m grpc_tools.protoc \
-Iprotos/ \
--python_out=. \
--grpc_python_out=. \
$1
# Directory of the .proto files
PROTO_DIR="../protos"
OUTPUT_DIR="../protos"

# Ensure output directory exists
mkdir -p $OUTPUT_DIR

# Generate Python gRPC and protobuf code
python -m grpc_tools.protoc -I=$PROTO_DIR --python_out=$OUTPUT_DIR --grpc_python_out=$OUTPUT_DIR $PROTO_DIR/*.proto

echo "gRPC code generated in $OUTPUT_DIR"

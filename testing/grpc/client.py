import grpc
from protos.generated import mars_rover_pb2
from protos.generated import mars_rover_pb2_grpc
def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = mars_rover_pb2_grpc.RoverServiceStub(channel)
        
        # Turn on headlights
        response = stub.ControlHeadlights(mars_rover_pb2.LEDRequest(on=True))
        print(f"Response: {response.message}")
        
        # Turn off headlights
        response = stub.ControlHeadlights(mars_rover_pb2.LEDRequest(on=False))
        print(f"Response: {response.message}")
        
        # Turn on LED for wheel 1
        response = stub.ControlWheelLEDs(mars_rover_pb2.WheelLEDRequest(wheel_number=1, on=True))
        print(f"Response: {response.message}")
        
        # Turn off LED for wheel 2
        response = stub.ControlWheelLEDs(mars_rover_pb2.WheelLEDRequest(wheel_number=2, on=False))
        print(f"Response: {response.message}")

if __name__ == "__main__":
    run()

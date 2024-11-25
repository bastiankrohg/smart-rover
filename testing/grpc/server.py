import grpc
from concurrent import futures
from protos import mars_rover_pb2
from protos import mars_rover_pb2_grpc

class RoverService(mars_rover_pb2_grpc.RoverServiceServicer):
    # Movement commands (same as before)
    def DriveForward(self, request, context):
        print(f"Driving forward at speed {request.speed}")
        return mars_rover_pb2.CommandResponse(success=True, message="Driving forward")

    def Reverse(self, request, context):
        print(f"Reversing at speed {request.speed}")
        return mars_rover_pb2.CommandResponse(success=True, message="Reversing")

    def TurnLeft(self, request, context):
        print(f"Turning left at {request.angle} degrees with speed {request.speed}")
        return mars_rover_pb2.CommandResponse(success=True, message="Turning left")

    def TurnRight(self, request, context):
        print(f"Turning right at {request.angle} degrees with speed {request.speed}")
        return mars_rover_pb2.CommandResponse(success=True, message="Turning right")

    def TurnOnSpot(self, request, context):
        direction = "left" if request.angle < 0 else "right"
        print(f"Turning on the spot {direction} at {abs(request.angle)} degrees")
        return mars_rover_pb2.CommandResponse(success=True, message="Turning on the spot")

    def RotateSensor(self, request, context):
        direction = "left" if request.angle < 0 else "right"
        print(f"Rotating sensor {direction} at {abs(request.angle)} degrees")
        return mars_rover_pb2.CommandResponse(success=True, message="Rotating sensor")

    def Stop(self, request, context):
        print("Stopping movement")
        return mars_rover_pb2.CommandResponse(success=True, message="Stopped")

    # Measurement commands
    def GetUltrasoundMeasurement(self, request, context):
        distance = 100.0
        print(f"Ultrasound measurement: {distance} cm")
        return mars_rover_pb2.UltrasoundResponse(distance=distance)

    def GetCameraFeed(self, request, context):
        for i in range(10):
            frame = b'\x00\x01' * 100
            print(f"Sending frame {i+1}")
            yield mars_rover_pb2.CameraFrame(image_data=frame)

    # LED Control commands
    def ControlHeadlights(self, request, context):
        status = "on" if request.on else "off"
        print(f"Turning headlights {status}")
        return mars_rover_pb2.CommandResponse(success=True, message=f"Headlights turned {status}")

    def ControlWheelLEDs(self, request, context):
        status = "on" if request.on else "off"
        print(f"Turning LED for wheel {request.wheel_number} {status}")
        return mars_rover_pb2.CommandResponse(success=True, message=f"Wheel {request.wheel_number} LED turned {status}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mars_rover_pb2_grpc.add_RoverServiceServicer_to_server(RoverService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Rover server is running...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()

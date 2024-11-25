import grpc
from concurrent import futures
from protos import mars_rover_pb2
from protos import mars_rover_pb2_grpc



class Coral(mars_rover_pb2_grpc.RoverServiceServicer):
    # Locomotion
    def DriveForward(self, request, context):
        print("DriveForward called with speed:", request.speed)
        return mars_rover_pb2.CommandResponse(success=True, message="DriveForward executed")

    def Reverse(self, request, context):
        print("Reverse called with speed:", request.speed)
        return mars_rover_pb2.CommandResponse(success=True, message="Reverse executed")

    def TurnLeft(self, request, context):
        print("TurnLeft called with angle:", request.angle)
        return mars_rover_pb2.CommandResponse(success=True, message="TurnLeft executed")

    def TurnRight(self, request, context):
        print("TurnRight called with angle:", request.angle)
        return mars_rover_pb2.CommandResponse(success=True, message="TurnRight executed")

    def RotateOnSpot(self, request, context):
        print("RotateOnSpot called with angle:", request.angle)
        return mars_rover_pb2.CommandResponse(success=True, message="RotateOnSpot executed")

    # POV
    def RotatePeriscope(self, request, context):
        print("RotatePeriscope called with angle:", request.angle)
        return mars_rover_pb2.CommandResponse(success=True, message="RotatePeriscope executed")

    def ControlHeadlights(self, request, context):
        print("ControlHeadlights called with on:", request.on)
        return mars_rover_pb2.CommandResponse(success=True, message="ControlHeadlights executed")

    def ControlWheelLEDs(self, request, context):
        print(f"ControlWheelLEDs called for wheel {request.wheel_number} with on:", request.on)
        return mars_rover_pb2.CommandResponse(success=True, message="ControlWheelLEDs executed")

    # Measurements
    def GetUltrasoundMeasurement(self, request, context):
        print("GetUltrasoundMeasurement called")
        return mars_rover_pb2.UltrasoundResponse(distance=123.45)

    # Camera
    def GetCameraStream(self, request, context):
        print("GetCameraStream called")
        return mars_rover_pb2.CameraStreamResponse(stream_url="rtsp://<raspberry_pi_ip>:8554/live")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mars_rover_pb2_grpc.add_RoverServiceServicer_to_server(Coral(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server is running...")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()

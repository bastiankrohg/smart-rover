import grpc
from protos import mars_rover_pb2
from protos import mars_rover_pb2_grpc


class Pi:
    def __init__(self, server_address="localhost:50051"):
        self.channel = grpc.insecure_channel(server_address)
        self.stub = mars_rover_pb2_grpc.RoverServiceStub(self.channel)

    # Locomotion
    def drive_forward(self, speed):
        request = mars_rover_pb2.DriveRequest(speed=speed)
        response = self.stub.DriveForward(request)
        print("DriveForward Response:", response.message)

    def stop(self, request, context):
        request = mars_rover_pb2.StopRequest()
        response = self.stub.Stop(request)
        print("DriveForward Response:", response.message)

    def reverse(self, speed):
        request = mars_rover_pb2.DriveRequest(speed=speed)
        response = self.stub.Reverse(request)
        print("Reverse Response:", response.message)

    def turn_left(self, angle):
        request = mars_rover_pb2.TurnRequest(angle=angle)
        response = self.stub.TurnLeft(request)
        print("TurnLeft Response:", response.message)

    def turn_right(self, angle):
        request = mars_rover_pb2.TurnRequest(angle=angle)
        response = self.stub.TurnRight(request)
        print("TurnRight Response:", response.message)

    def rotate_on_spot(self, angle):
        request = mars_rover_pb2.TurnRequest(angle=angle)
        response = self.stub.TurnOnSpot(request)
        print("RotateOnSpot Response:", response.message)

    # POV
    def rotate_periscope(self, angle):
        request = mars_rover_pb2.RotateRequest(angle=angle)
        response = self.stub.RotatePeriscope(request)
        print("RotatePeriscope Response:", response.message)

    def control_headlights(self, on):
        request = mars_rover_pb2.LEDRequest(on=on)
        response = self.stub.ControlHeadlights(request)
        print("ControlHeadlights Response:", response.message)

    def control_wheel_leds(self, wheel_number, on):
        request = mars_rover_pb2.WheelLEDRequest(wheel_number=wheel_number, on=on)
        response = self.stub.ControlWheelLEDs(request)
        print("ControlWheelLEDs Response:", response.message)

    # Measurements
    def get_ultrasound_measurement(self):
        request = mars_rover_pb2.UltrasoundRequest()
        response = self.stub.GetUltrasoundMeasurement(request)
        print("Ultrasound Measurement:", response.distance)

    # Camera
    def get_camera_stream(self):
        request = mars_rover_pb2.CameraStreamRequest()
        response = self.stub.GetCameraStream(request)
        print("Camera Stream URL:", response.stream_url)


if __name__ == "__main__":
    #pi_client = Pi(server_address="<coral_dev_board_ip>:50051")
    pi_client = Pi(server_address="localhost:50051")

    # Test each function
    pi_client.drive_forward(5.0)
    pi_client.reverse(2.5)
    pi_client.turn_left(90)
    pi_client.turn_right(45)
    pi_client.rotate_on_spot(180)

    pi_client.rotate_periscope(45)
    pi_client.control_headlights(True)
    pi_client.control_wheel_leds(3, True)

    pi_client.get_ultrasound_measurement()
    pi_client.get_camera_stream()

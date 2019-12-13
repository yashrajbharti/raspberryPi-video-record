import picamera
import time

camera = picamera.PiCamera()
camera.vflip = true
# vertical flip if needed

camera.start_recording('examplevid.h264')
# video with file name examplevid.h264 has started recording

time.sleep(5)
# records for 5 seconds

camera.stop_recording
# recording stops

import ctypes
import _ctypes
import pygame
import sys
import numpy as np
import cv2

# Import Kinect v2 library
import pykinect2
from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *

# Initialize Kinect v2 sensor
kinect = PyKinectV2.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color | PyKinectV2.FrameSourceTypes_Depth)

# Initialize pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((kinect.color_frame_desc.Width, kinect.color_frame_desc.Height), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE, 32)

# Main loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get color frame from Kinect v2
    if kinect.has_new_color_frame():
        frame = kinect.get_last_color_frame()
        frame = frame.reshape((kinect.color_frame_desc.Height, kinect.color_frame_desc.Width, 4))
        frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB)

        # Display color frame
        frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
        screen.blit(frame_surface, (0, 0))
        pygame.display.update()

    # Process other Kinect v2 frames (depth, body, etc.) as needed

    # Optional: limit the frame rate
    pygame.time.wait(33)

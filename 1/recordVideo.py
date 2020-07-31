import cv2
import time
from pathlib import Path
from os import path

# Create a capture video object.
# Try replacing 1 with 0 if it doesn't work
capture = cv2.VideoCapture(0)

# Get the video resolution.
w = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = round(capture.get(cv2.CAP_PROP_FPS))

# Check if the fps variable has a correct value.
fps = fps if fps > 0 else 30

# Create a record video object.
isColor = True
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
outputFile = str(Path(path.dirname(
    path.realpath(__file__))) / "outputs/recording.mov")
record = cv2.VideoWriter(outputFile, fourcc, fps, (w, h), isColor)

# Create an OpenCV window.
cv2.namedWindow("Video", cv2.WINDOW_AUTOSIZE)

# This will run while there is a new frame in the video file or
# while the user do not press the "q" (quit) keyboard button.
while True:
    # Capture frame-by-frame.
    retval, frame = capture.read()

    # Check if there is a valid frame.
    if not retval:
        break

    # Convert the input image to grayscale.
    record.write(frame)

    # Resize the input image.
    image = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # Display the resulting frame.
    cv2.imshow("Video", image)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# When everything done, release the capture and record objects.
record.release()
capture.release()
cv2.destroyAllWindows()

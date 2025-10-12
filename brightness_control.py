# Importing Libraries
import cv2
import numpy as np

try:
    import screen_brightness_control as sbc

    BRIGHTNESS_CONTROL_AVAILABLE = True
except ImportError:
    print("Screen brightness control not available")
    BRIGHTNESS_CONTROL_AVAILABLE = False

# Start capturing video from webcam
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

print("Simple Brightness Control")
print("Press 'q' to quit")

brightness_set = False  # Track if brightness has been set

try:
    while True:
        # Read video frame by frame
        ret, frame = cap.read()

        # If frame is not read correctly, break
        if not ret:
            print("Error: Can't receive frame")
            break

        # Flip image
        frame = cv2.flip(frame, 1)

        # Display instructions on frame
        cv2.putText(
            frame,
            "Brightness Control",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )
        cv2.putText(
            frame,
            "Press q to quit",
            (10, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )

        # Show the frame
        cv2.imshow("Brightness Control", frame)

        # Set brightness to a fixed level if available and not already set
        if BRIGHTNESS_CONTROL_AVAILABLE and not brightness_set:
            try:
                monitors = sbc.list_monitors()
                print("Detected monitors:", monitors)
                if not monitors:
                    print("No monitors detected that support brightness control.")
                    BRIGHTNESS_CONTROL_AVAILABLE = False
                for m in monitors:
                    print(f"Current brightness for {m}:", sbc.get_brightness(display=m))
                sbc.set_brightness(50)
                print("Brightness set to 50%. New values:")
                for m in monitors:
                    print(f"Brightness for {m}:", sbc.get_brightness(display=m))
                brightness_set = True
            except Exception as e:
                print(f"Brightness control error: {e}")
                BRIGHTNESS_CONTROL_AVAILABLE = False

        # Exit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
finally:
    # Release everything
    cap.release()
    cv2.destroyAllWindows()

import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import urllib.request
import os

# --------------------------------------------------
# Download model if not present
# --------------------------------------------------
MODEL_PATH = "hand_landmarker.task"
if not os.path.exists(MODEL_PATH):
    print("Downloading hand model...")
    url = "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"
    urllib.request.urlretrieve(url, MODEL_PATH)
    print("Model downloaded!")

# --------------------------------------------------
# Initialize HandLandmarker
# --------------------------------------------------
base_options = python.BaseOptions(model_asset_path=MODEL_PATH)
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1,
    min_hand_detection_confidence=0.6,
    min_hand_presence_confidence=0.6,
    min_tracking_confidence=0.6
)
detector = vision.HandLandmarker.create_from_options(options)

# --------------------------------------------------
# Webcam
# --------------------------------------------------
cap = cv2.VideoCapture(0)

# --------------------------------------------------
# Finger landmark IDs
# --------------------------------------------------
FINGERS_Y = {
    "Index": (8, 6, 5),
    "Middle": (12, 10, 9),
    "Ring": (16, 14, 13),
    "Pinky": (20, 18, 17)
}

THUMB_TIP = 4
THUMB_IP = 3

HAND_CONNECTIONS = [
    (0,1),(1,2),(2,3),(3,4),
    (0,5),(5,6),(6,7),(7,8),
    (0,9),(9,10),(10,11),(11,12),
    (0,13),(13,14),(14,15),(15,16),
    (0,17),(17,18),(18,19),(19,20),
    (5,9),(9,13),(13,17)
]

print("Finger detection started (Thumb included). Press 'q' to quit.")

# --------------------------------------------------
# Main Loop
# --------------------------------------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)

    result = detector.detect(mp_image)

    if result.hand_landmarks:
        for i, hand_landmarks in enumerate(result.hand_landmarks):
            h, w, _ = frame.shape

            # Draw landmarks
            for lm in hand_landmarks:
                x, y = int(lm.x * w), int(lm.y * h)
                cv2.circle(frame, (x, y), 4, (0, 255, 0), -1)

            for start, end in HAND_CONNECTIONS:
                s = hand_landmarks[start]
                e = hand_landmarks[end]
                cv2.line(
                    frame,
                    (int(s.x * w), int(s.y * h)),
                    (int(e.x * w), int(e.y * h)),
                    (255, 0, 0),
                    2
                )

            wrist = hand_landmarks[0]
            y_offset = 40

            # ---------------------------------
            # Detect handedness
            # ---------------------------------
            handedness = result.handedness[i][0].category_name

            # ---------------------------------
            # THUMB detection (X-axis)
            # ---------------------------------
            thumb_tip = hand_landmarks[THUMB_TIP]
            thumb_ip = hand_landmarks[THUMB_IP]

            if handedness == "Right":
                thumb_up = thumb_tip.x > thumb_ip.x
            else:
                thumb_up = thumb_tip.x < thumb_ip.x

            thumb_status = "Thumb: UP" if thumb_up else "Thumb: DOWN"
            cv2.putText(
                frame,
                thumb_status,
                (10, y_offset),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0) if thumb_up else (0, 0, 255),
                2
            )
            y_offset += 30

            # ---------------------------------
            # Other fingers (Y-axis)
            # ---------------------------------
            for finger, (tip_id, pip_id, mcp_id) in FINGERS_Y.items():
                tip = hand_landmarks[tip_id]
                pip = hand_landmarks[pip_id]
                mcp = hand_landmarks[mcp_id]

                if (tip.y < pip.y < mcp.y) and \
                   (abs(tip.y - wrist.y) > abs(pip.y - wrist.y)):
                    status = f"{finger}: UP"
                    color = (0, 255, 0)
                else:
                    status = f"{finger}: DOWN"
                    color = (0, 0, 255)

                cv2.putText(
                    frame,
                    status,
                    (10, y_offset),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    color,
                    2
                )
                y_offset += 30

    else:
        cv2.putText(
            frame,
            "No hand detected",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    cv2.imshow("Finger Detection (All 5 Fingers)", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# --------------------------------------------------
# Cleanup
# --------------------------------------------------
cap.release()
cv2.destroyAllWindows()
detector.close()
print("Program ended.")

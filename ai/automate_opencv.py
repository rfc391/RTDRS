
import cv2
import numpy as np

def perform_object_detection():
    # Load a sample model (use your trained model for actual use)
    net = cv2.dnn.readNetFromCaffe(
        'path_to_prototxt_file.prototxt', 
        'path_to_caffemodel_file.caffemodel'
    )

    # Load a sample image (replace with real-time camera feed or video file)
    image = cv2.imread('sample_image.jpg')
    h, w = image.shape[:2]

    # Pre-process the image for the model
    blob = cv2.dnn.blobFromImage(image, 1.0, (300, 300), (104.0, 177.0, 123.0))
    net.setInput(blob)
    detections = net.forward()

    # Draw detections on the image
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:  # Confidence threshold
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)

    # Display the output
    cv2.imshow("Detections", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    perform_object_detection()

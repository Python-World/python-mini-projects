import cv2

# cv2 method to capture frames from live video
cap = cv2.VideoCapture(0)

# loop to get frames
while(1): 

	# read every frame from 
	ret, videoframe = cap.read() 

	# Display the frame
	cv2.imshow('Camera',videoframe) 
	
	# delay
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
#  camera realesing 
cap.release() 

# destroying all windows
cv2.destroyAllWindows() 

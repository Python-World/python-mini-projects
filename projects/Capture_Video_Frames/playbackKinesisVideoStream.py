
import boto3
import cv2

STREAM_NAME = "your_stream_name"
kvs = boto3.client("kinesisvideo", )
# Grab the endpoint from GetDataEndpoint
endpoint = kvs.get_data_endpoint(
    APIName="GET_HLS_STREAMING_SESSION_URL",
    StreamName=STREAM_NAME
    )['DataEndpoint']

print(endpoint)

# # Grab the HLS Stream URL from the endpoint
kvam = boto3.client("kinesis-video-archived-media", endpoint_url=endpoint)
url = kvam.get_hls_streaming_session_url(
    StreamName=STREAM_NAME,
    #PlaybackMode="ON_DEMAND",
    PlaybackMode="LIVE"
    )['HLSStreamingSessionURL']

print(url)

vcap = cv2.VideoCapture(url)

while(True):
    # Capture frame-by-frame
    ret, frame = vcap.read()

    if frame is not None:
        # Display the resulting frame
        cv2.imshow('frame',frame)

        # Press q to close the video windows before it ends if you want
        if cv2.waitKey(2) & 0xFF == ord('q'):
            break
    else:
        print("Frame is None")
        break

# When everything done, release the capture
vcap.release()
cv2.destroyAllWindows()
print("Video stop")


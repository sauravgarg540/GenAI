import runpod
import base64
import os
import time
import os


runpod.api_key = os.environ.get("API_KEY")

endpoint = runpod.Endpoint(os.environ.get("ENDPOINT"))

def wit_runsync():


    start = time.time()
    run_request = endpoint.run_sync(
        {"input":
             {"text": "Hello, My name is Saurav Gupta. I have just deployed a text2speech model on runpod with run_sync"}
         }
    )
    print(time.time()-start)
    audio_name = os.path.basename(run_request["name"])
    with open(audio_name, 'wb') as f:
        ascii = run_request["wav"].encode("ascii")
        bytes_decoded = base64.b64decode(ascii)
        f.write(bytes_decoded)

def with_run(count):

    run_request = endpoint.run(
        {"input":
             {"text": f"Hello, My name is Saurav Gupta. I have just deployed a text2speech model on runpod with run {count}"}}
    )

    # Check the status of the endpoint run request
    print(run_request)
    print(run_request.status())

    # Get the output of the endpoint run request, blocking until the endpoint run is complete.
    output = run_request.output(timeout=60)
    audio_name = os.path.basename(output["name"])
    with open(audio_name, 'wb') as f:
        ascii = output["wav"].encode("ascii")
        bytes_decoded = base64.b64decode(ascii)
        f.write(bytes_decoded)

if __name__ == "__main__":
    for i in range(5):
        with_run(i)

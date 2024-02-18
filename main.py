import runpod
import base64
import os
import time

runpod.api_key = os.environ.get("API_KEY")

def wit_runsync():
    endpoint = runpod.Endpoint(os.environ.get("ENDPOINT"))

    start = time.time()
    run_request = endpoint.run_sync(
        {"input":
            {
                "text": f"Hello, My name is Saurav Gupta. I have just deployed a text2speech model on runpod with runsync",
                "embedding_path": "/runpod-volume/embeddings",
                "voice_preset": "test4"}}
    )
    audio_name = os.path.basename(run_request["name"])
    with open(audio_name, 'wb') as f:
        ascii = run_request["wav"].encode("ascii")
        bytes_decoded = base64.b64decode(ascii)
        f.write(bytes_decoded)

def with_run():
    endpoint = runpod.Endpoint(os.environ.get("ENDPOINT"))
    run_request = endpoint.run(
        {"input":
            {
                "text": "Hello, My name is Saurav Gupta. I have just deployed a text2speech model on runpod with run",
                "embedding_path": None
               }}
        )
    # Check the status of the endpoint run request
    print(run_request.job_id)
    print(run_request.status())

    # Get the output of the endpoint run request, blocking until the endpoint run is complete.
    output = run_request.output(timeout=200)
    audio_name = os.path.basename(output["name"])
    with open(audio_name, 'wb') as f:
        ascii = output["wav"].encode("ascii")
        bytes_decoded = base64.b64decode(ascii)
        f.write(bytes_decoded)

def generate_embeddding(wav_file_path):
    endpoint = runpod.Endpoint(os.environ.get("ENDPOINT_A2E"))

    with open(wav_file_path, "rb") as wav_file:
        # Read the WAV file content
        wav_content = wav_file.read()

        # Encode the content to base64
        base64_encoded = base64.b64encode(wav_content).decode('ascii')
        run_request = endpoint.run_sync(
            {"input":
                 {
                "audio_file": base64_encoded,
                 "speaker_name": "test1"}
             }
        )

        print(run_request)

if __name__ == "__main__":
    # generate_embeddding("1708273081_ghottu.wav")
    with_run()

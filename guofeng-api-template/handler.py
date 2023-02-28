import runpod
import subprocess
import requests
import time

def check_api_availability(host):
    while True:
        try:
            response = requests.get(host)
            return
        except requests.exceptions.RequestException as e:
            print(f"API is not available, retrying in 5s... ({e})")
        except Exception as e:
            print('something went wrong')
        time.sleep(5)

check_api_availability("http://127.0.0.1:3000/sdapi/v1/txt2img")

print('run handler')

def handler(event):
    '''
    This is the handler function that will be called by the serverless.
    '''
    print('got event')
    print(event)

    response = requests.post(url=f'http://127.0.0.1:3000/sdapi/v1/txt2img', json=event["input"])

    json = response.json()
    # do the things

    print(json)

    # return the output that you want to be returned like pre-signed URLs to output artifacts
    return json


runpod.serverless.start({"handler": handler})
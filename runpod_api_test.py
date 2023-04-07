import time

import requests
import base64

runpod_key = ''
api_name = ''

prompt = '<lora:koreanDollLikeness_v15:0.66>, best quality, ultra high res, (photorealistic:1.4), 1girl, solo focus, ((blue long dress)), elbow dress, black thighhighs, frills, ribbons, studio background, (Kpop idol), (aegyo sal:1), (platinum blonde hair:1), ((puffy eyes)), looking at viewer, facing front, smiling, laughing'
negative_prompt = 'paintings, sketches, (worst quality:2), (low quality:2), (normal quality:2), lowres, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, age spot, glans, nsfw, nipples'


def generation():
    res = requests.post(f'https://api.runpod.ai/v1/{api_name}/run', headers={
        'Content-Type': 'application/json',
        "Authorization": f"Bearer {runpod_key}"
    }, json={
        "input": {"prompt": prompt, "steps": 28, "negative_prompt": negative_prompt, "width": 512, "height": 768, "sampler_index": "DPM++ SDE Karras",
                  "batch_size": 1, "seed": -1},
    })
    if res.status_code != 200:
        print(f"request failed: url: {res.url}, status code: {res.status_code}, text: {res.text}")
        return

    task_id = res.json()['id']

    while True:
        res = requests.get(f'https://api.runpod.ai/v1/{api_name}/status/{task_id}', headers={
            'Content-Type': 'application/json',
            "Authorization": f"Bearer {runpod_key}"
        })
        if res.status_code != 200:
            print(f"request failed: url: {res.url}, status code: {res.status_code}, text: {res.text}")
            break

        status = res.json()['status']
        print(status)
        if status == 'COMPLETED':
            for imgstring in res.json()['output']['images']:
                with open(f"test_{time.time()}.png", "wb") as fh:
                    imgdata = base64.b64decode(imgstring)
                    fh.write(imgdata)
            print(res.json())
            break

        if status == 'FAILED':
            print(res.json())
            break
        time.sleep(10)


if __name__ == '__main__':
    generation()

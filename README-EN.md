<p align="center">
  English
  | 
  <a href="README.md">简体中文</a>
</p>


##  How to Run ChilloutMix and LORA in RunPod Serverless


By far [RunPod](https://runpod.io?ref=78g53ap2) is the easiest way to run ChilloutMix and LORA in serverless.

I tried [Replicate](https://replicate.com/), but failed. Maybe will try it later..


### 1. Create a [RunPod](https://runpod.io?ref=78g53ap2) account

### 2. Go to [Serverless My Template](https://www.runpod.io/console/serverless/user/templates), Click New Template

You can set your preferred tempalte name, but container name should be **chilloutai/auto-api:1.0.0**

The docker image building process is in the repo.

<img width="500" alt="image" src="https://user-images.githubusercontent.com/95554104/221343335-12bc53fa-cef3-4173-bf14-60fac025d071.png">

### 3. Go to [Serverless My APIs](https://www.runpod.io/console/serverless/user/apis), Click New API

Set your api name and choose the template you create in last step

<img width="500" alt="image" src="https://user-images.githubusercontent.com/95554104/221343564-8d8a7d4a-17ab-4785-982d-17e09d45e563.png">

After create you will get the API below

### 4. Go to [Settings](https://www.runpod.io/console/user/settings) to create a API key 

<img width="500" alt="image" src="https://user-images.githubusercontent.com/95554104/221343665-39ff47e6-6e0b-478c-96ab-eeaad310f6aa.png">


### 5. Now Test it.

Set API key and name into runpod_api_test.py, then run `python runpod_api_test.py`
After 30s-1min, you will see the pictures.



Hope this guide can help you! If you want to support me, please use my [RunPod Referral link](https://runpod.io?ref=78g53ap2)


Here is the demo app I created with this api: https://chilloutai.com/

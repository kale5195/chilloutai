<p align="center">
  <a href="README.md">English</a>
  | 
  简体中文
</p>


##  如何在 RunPod Serverless 环境中运行 ChilloutMix 和 LORA


[RunPod](https://runpod.io?ref=78g53ap2) 应该是目前在 Serverless 环境中运行 ChilloutMix 和 LORA 最简单和最便宜的方式。


我尝试过 [Replicate](https://replicate.com/), 但没成功，之后可能再试试.

以下是使用步骤：

### 1. 创建一个 [RunPod](https://runpod.io?ref=78g53ap2) 账号

### 2. 前往 [Serverless My Template](https://www.runpod.io/console/serverless/user/templates), 点击 New Template

可以设置一个 tempalte name, 但 container name 必须是 **chilloutai/auto-api:1.0.0**

Docker 镜像构建过程在仓库中。

<img width="500" alt="image" src="https://user-images.githubusercontent.com/95554104/221343335-12bc53fa-cef3-4173-bf14-60fac025d071.png">

### 3. 前往 [Serverless My APIs](https://www.runpod.io/console/serverless/user/apis), 点击 New API

设置 api name 并选择上一步创建的 template name

<img width="500" alt="image" src="https://user-images.githubusercontent.com/95554104/221343564-8d8a7d4a-17ab-4785-982d-17e09d45e563.png">

创建完成后，可以在下方看到 API 接口

### 4. 前往 [Settings](https://www.runpod.io/console/user/settings) to 创建 API key 

<img width="500" alt="image" src="https://user-images.githubusercontent.com/95554104/221343665-39ff47e6-6e0b-478c-96ab-eeaad310f6aa.png">


### 5. 测试一下是否正常使用

把 API key 和 name 放到 runpod_api_test.py,然后运行 `python runpod_api_test.py`

30 秒到 1 分钟后，应该可以在目录下看到图片。


希望这个过程可以帮助你！如果想支持我以下，可以使用 [RunPod Referral link](https://runpod.io?ref=78g53ap2) 这个链接注册


另外我还根据这个 api 创建了一个小网站，可以试一下: https://chilloutai.com/

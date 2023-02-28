希望这个过程可以帮助你！如果想支持一下，可以使用 [RunPod Referral link](https://runpod.io?ref=78g53ap2) 这个链接注册


##  如何在 RunPod WebUI 环境中运行 ChilloutMix 和 LORA


[RunPod](https://runpod.io?ref=78g53ap2) 应该是运行 ChilloutMix 和 LORA 最简单和最便宜的方式。

此教程不同于 [Runpod Serverless](https://github.com/kale5195/automatic-chillout/blob/main/serverless-zh.md)，是在 Runpod 中运行 Stable Diffussion Web UI 进行出图

该教程使用的 docker images 里边已有 ChilloutMix base Model + LORA，所以可以部署后一键使用，包含的 LORA 如下：

koreanDollLikeness_v15.safetensors   
japaneseDollLikeness_v10.safetensors   
taiwanDollLikeness_v10.safetensors   
yaemikoMixed.safetensors   
russianDollLikeness_v3.safetensors   
koreanDollLikeness_v10.safetensors   

以下是具体使用步骤：

### 1. 创建一个 [RunPod](https://runpod.io?ref=78g53ap2) 账号

### 2. 点击使用我创建的 [Template](https://runpod.io/gsc?template=m0nobj7c2t&ref=78g53ap2) 

这个模板中已有所有的 model，可以一键使用

### 3. 选择最便宜的 Pod 进行部署

<img width="500" alt="image" src="https://user-images.githubusercontent.com/95554104/221786576-f8e05203-c83f-40e2-89a3-1c32bdcb6923.png">


### 4. 等待部署，当CPU 利用率降为 0% 表示部署成功
<img width="521" alt="image" src="https://user-images.githubusercontent.com/95554104/221787748-55b49267-02fd-4bbc-9dc0-f83243d1e01d.png">

### 5. 点击 connect，进入 web ui 

从 civikit 中 copy generation data 到 prompt , 点击右侧小箭头会自动帮你填充参数，然后点击 Generate 就可以一键出图
<img width="1030" alt="image" src="https://user-images.githubusercontent.com/95554104/221788124-ae4f41ce-21ff-4e56-90c3-7ef34d6e0256.png">





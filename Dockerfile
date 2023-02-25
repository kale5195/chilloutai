FROM chilloutai/stable-diffusion:1.0.0

SHELL ["/bin/bash", "-c"]

ENV PATH="${PATH}:/workspace/stable-diffusion-webui/venv/bin"

WORKDIR /

ADD model.safetensors /

RUN pip install -U xformers
RUN pip install runpod

ADD koreanDollLikeness_v15.safetensors /workspace/stable-diffusion-webui/models/Lora/koreanDollLikeness_v15.safetensors
ADD japaneseDollLikeness_v10.safetensors /workspace/stable-diffusion-webui/models/Lora/japaneseDollLikeness_v10.safetensors
ADD taiwanDollLikeness_v10.safetensors /workspace/stable-diffusion-webui/models/Lora/taiwanDollLikeness_v10.safetensors

ADD handler.py .
ADD start.sh /start.sh
RUN chmod +x /start.sh

CMD [ "/start.sh" ]

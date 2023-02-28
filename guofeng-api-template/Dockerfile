FROM chilloutai/guofeng-template:1.0.0

SHELL ["/bin/bash", "-c"]

ENV PATH="${PATH}:/workspace/stable-diffusion-webui/venv/bin"

WORKDIR /

RUN pip install -U xformers
RUN pip install runpod

ADD webui.py /workspace/stable-diffusion-webui/webui.py
ADD handler.py .
ADD start.sh /start.sh
RUN chmod +x /start.sh

CMD [ "/start.sh" ]

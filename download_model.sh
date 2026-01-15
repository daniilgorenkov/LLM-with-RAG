mkdir -p /root/qwen2.5-14b-instruct
HF_HUB_ENABLE_HF_TRANSFER=1 huggingface-cli download Qwen/Qwen2.5-14B-Instruct --local-dir /root/qwen2.5-14b-instruct
#!/bin/bash

MODEL_NAME="HuggingFaceTB/SmolVLM-Instruct"

export PYTHONPATH=src:$PYTHONPATH

python src/merge_lora_weights.py \
    --model-path /home/fmaaf/fulong/vlm/SmolVLM-Finetune/output/lora_vision_test \
    --model-base $MODEL_NAME  \
    --save-model-path /home/fmaaf/fulong/vlm/SmolVLM-Finetune/output/merge_test \
    --safe-serialization
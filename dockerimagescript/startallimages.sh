#!/bin/bash
nohup docker run -p 8501:8501 dzmyolov5-ascend8501 > logs/dzmyolov5-ascend8501.out 2>&1 &
nohup docker run -p 8502:8502 webrtc8502 > logs/webrtc8502.out 2>&1 &
nohup docker run -p 8503:8503 streamlitmainpage8503 > logs/streamlitmainpage8503.out 2>&1 &
nohup docker run -p 8505:8505 wfccellseg8505 > logs/wfccellseg8505.out 2>&1 & 
nohup docker run -p 8504:8504 hyx8504 > logs/hyx8504.out 2>&1 &

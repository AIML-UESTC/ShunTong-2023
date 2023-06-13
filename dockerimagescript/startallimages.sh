#!/bin/bash
nohup docker run -p 8501:8501 dzmyolov5-ascend8501 > /home/cq/qiteam/dokcerlogs/dzmyolov5-ascend8501.out 2>&1 &
nohup docker run -p 8502:8502 webrtc8502 > /home/cq/qiteam/dokcerlogs/webrtc8502.out 2>&1 &
nohup docker run -p 8503:8503 streamlitmainpage8503 > /home/cq/qiteam/dokcerlogs/streamlitmainpage8503.out 2>&1 &
nohup docker run -p 8505:8505 wfccellseg8505 > /home/cq/qiteam/dokcerlogs/wfccellseg8505.out 2>&1 & 
nohup docker run -p 8504:8504 hyx8504 > /home/cq/qiteam/dokcerlogs/hyx8504.out 2>&1 &
nohup docker run -p 8506:8506 wj8506 > /home/cq/qiteam/dokcerlogs/wj8506.out 2>&1 &

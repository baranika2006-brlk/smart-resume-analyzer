@echo off 
title Frontend Web Server - Port 5500 
cd /d "C:\Users\HP\OneDrive\Documents\Desktop\Smart Resume Analyzer\frontend" 
python -m http.server 5500 --bind 127.0.0.1 
pause 

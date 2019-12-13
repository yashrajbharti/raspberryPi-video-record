# raspberryPi-video-record   
![](https://www.raspberrypi.org/app/uploads/2011/10/Raspi-PGB001-300x267.png)  
    
## Terminal  
```
sudo apt-get install python-picamera
nano cameraexample2.py
python cameraexample2.py
omxplayer examplevid.h264
```
  
## What it does?
1. It first installs python-picamera so we can use the supersimple camera module that we get for Raspberry Pi (Ignore if already installed).   
2. Then we write the python code in nano. **see cameraexample2.py**, That's the code I wrote.  
3. Finally we execute the code with python cameraexample2.py and the camera module records a 5 second video and saves it as "examplevid.h264".  
4. If we want to see our video we perform omxplayer _video name_ which is "examplevid.h264" in our case.  

  

    
  
  

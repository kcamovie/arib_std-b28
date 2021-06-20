# Generating multiformat colorbar still image complying to ARIB STD-B28

## Introduction

This is a multiformat colorbar generator complying to ARIB STD-B28. Unlike exported from NLE or general video processing software, raw data generated by this code have YUV444 precision and are very faithful to the defined standards by ARIB (Association of Radio Industries and Businesses).  
*This code is made for ARIB colorbar used in Japan, not SMPTE coloabar.

### Sample
ARIB STD-B28 Multiformat Color Bar 1min - YouTUbe  
https://www.youtube.com/watch?v=dAWGwhC1VVw  
[![ARIB STD-B28 Multiformat Color Bar 1min](https://img.youtube.com/vi/dAWGwhC1VVw/1.jpg)](https://www.youtube.com/watch?v=dAWGwhC1VVw "ARIB STD-B28 Multiformat Color Bar 1min")

## Prerequisites

- python and numpy module installed
- ffmpeg installed (if you generate video)

## How to use

Colorbar still image can generated by following :
```
python std-b28.py
```

then still image named "std-b28_1920x1080_yuv444p10le.yuv" appears.

This still image can preview by ffplay, like following :
```
ffplay -video_size 1920x1080 -pixel_format yuv444p10le "std-b28_1920x1080_yuv444p10le.yuv"
```

## Generating video

By using ffmpeg, the still image can be converted to video, like following :
```
ffmpeg -s 1920x1080 -pix_fmt yuv444p10le -framerate 60000/1001 -stream_loop -1 -i "std-b28_1920x1080_yuv444p10le.yuv" -t 60 -pix_fmt yuv420p -r 60000/1001 "out.mp4"
```

If you need uncompressed video, for example YUV420 10bit (v210),
```
ffmpeg -s 1920x1080 -pix_fmt yuv444p10le -framerate 60000/1001 -stream_loop -1 -i "std-b28_1920x1080_yuv444p10le.yuv" -t 60 -pix_fmt yuv422p10le -c:v v210 -r 60000/1001 "out.avi"
```

Futhermore, if you need video with 1kHz sine audio, add options following :
```
-f lavfi -i "sine=frequency=1000:sample_rate=48000:duration=60,volume=-2dB" -ac 2 -c:a pcm_s24le
```

## References
- ARIB STD-B28 Multiformat Color Bar - 
https://www.arib.or.jp/english/std_tr/broadcasting/std-b28.html

## Disclaimer
Please use this code at your own lisk. I do not take any responsibility or liability for you using this code.

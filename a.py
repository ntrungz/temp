ffmpeg -re -stream_loop 20 -i "https://awevideo.s3.amazonaws.com/video-29742488-4335f71eb6aff00adb4fff349097be1c.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJSCJQ2NM3XLFPVKA%2F20240721%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240721T081238Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e5bff99775abc5254875eabef84bee3493343234f974fff1e06a243865e22c33" -vcodec libx264 -preset superfast -ar 44100 -s 1920x1080 -f flv "rtmp://a.rtmp.youtube.com/live2/v32r-5m0s-1fuc-aezt-1tad"

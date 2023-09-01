This is a thin subprocess wrapper of FFMPEG to perform specific tasks for manipulating frames of videos.

While in development all testing is done in Windows. Linux has different command line options so this will unlikely work, but easy to port.
If you find this package useful and need Linux support, raise an issue and I will put in the time to port it.

# Installation

NOTE: ffmpeg must be installed on your system and be available in the path. 
I intend to be more helpful, but for the time being a quick Google search for ffmpeg installation should suffice.
(TODO: Add information on how to install ffmpeg)

```
git clone https://github.com/saltchicken/pyframes
cd pyframes
python setup.py install
```

# Usage

Convert video to individual frames
```
pyframes -i input_video.mp4 -o output_folder -r 10 --video
```

Convert individual frames to video
```
pyframes -i input_folder -o output_video.mp4 -r 10 --frames
```

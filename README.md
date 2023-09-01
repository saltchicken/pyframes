This is a thin subprocess wrapper of FFMPEG to perform specific tasks for manipulating frames of videos.

While in development all testing is done in Windows. Linux has different command line options so this will unlikely work, but easy to port.
If you find this package useful and need Linux support, raise an issue and I will put in the time to port it.

# Installation

NOTE: ffmpeg must be installed on your system and be available in the path. TODO: Add information on how to install ffmpeg
I intend to be more helpful, but for the time being a quick Google search for ffmpeg installation should suffice.

```
git clone https://github.com/saltchicken/pyframes
cd pyframs
python setup.py install
```

# Usage

Convert video to individual frames
```
pyframes input_video.mp4 output_folder 10
```
input_video - Target video
output_folder - Where to place frames
10 - Frames per second. Be careful with this setting, higher values will result in a LOT of frames (TODO: Provide example of potential memory usage)
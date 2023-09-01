import subprocess, os, sys
import argparse

def video_to_frames(input, output_folder, rate):
    if os.path.exists(output_folder):
        print(f"The directory {output_folder} exists.")
        # TODO: Check if folder is not empty and if so throw an error
    else:
        print(f"The directory '{output_folder}' does not exist.")
        os.mkdir(output_folder)
        
    ffmpeg_command = [
        'ffmpeg',
        '-i', input,
        '-r', rate + ":1",
        output_folder + '/%05d.png'
    ]

    # Run the ffmpeg command
    try:
        subprocess.run(ffmpeg_command, check=True)
        print(f'Conversion complete.')
    except subprocess.CalledProcessError as e:
        print(f'Error during conversion: {e}')
        
def frames_to_video(input_folder, output, rate):
    # ffmpeg -framerate 20 -pattern_type sequence -start_number 00000 -i ‘%05d-100.png’ -c:v libx264 -pix_fmt yuv420p out.mp4
    ffmpeg_command = [
        'ffmpeg',
        '-framerate', rate,
        '-pattern_type', 'sequence',
        '-start_number', '00000',
        '-i', input_folder + '/' + '%05d.png',
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        output,
    ]
    
    try:
        subprocess.run(ffmpeg_command, check=True)
        print(f'Conversion complete.')
    except subprocess.CalledProcessError as e:
        print(f'Error during conversion: {e}')

def main():
    parser = argparse.ArgumentParser(description="Sample face from an image and force resolution to 512 X 512")
    
    parser.add_argument('-i', '--input', required=True, help='Input video to convert to frames or folder to convert to video')
    parser.add_argument('-o', '--output', required=True, type=str, help='Output folder for frames or output filename for video')
    parser.add_argument('-r', '--rate', default='1', type=str, help='Frames per second')
    parser.add_argument('--video', action='store_true', help='Converting video to frames')
    parser.add_argument('--frames', action='store_true', help='Converting frames to video')
    args = parser.parse_args()
    
    # Make one of --video or --frames has been declared.
    if args.video and args.frames:
        print("Can't use both --video and --frames")
        sys.exit(1)
    elif not args.video and not args.frames:
        print("Please specify either --video or --frames")
        sys.exit(1)
        
    if args.video:
        print(f"Converting {args.input} to frames in {args.output}")
        if int(args.rate) > 60:
            print("Your FPS is too high")
            #TODO: Add a confirmation message to run this in case user REALLY wants to do this. For now just exit the program.
            sys.exit(1)
        video_to_frames(args.input, args.output, args.rate)
        # TODO: Check if everything ran correctly.
        return True
    
    if args.frames:
        print(f"Converting frames folder {args.input} to video {args.output}")
        frames_to_video(args.input, args.output, args.rate)
        # TODO: Check if everything ran correctly.
        return True
        
    print("If this is reached some other issue happened.")
        
    
    
if __name__ == '__main__':
    main()
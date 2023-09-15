# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 14:34:05 2023

@author: seema
"""

import cv2
import time
import os

def video_to_frames(input_loc, output_loc):
    """Function to extract frames from input video file
    and save them as separate frames in an output directory.
    Args:
        input_loc: Input video file.
        output_loc: Output directory to save the frames.
    Returns:
        None
    """
    try:
        os.mkdir(output_loc)
    except OSError:
        pass
    # Log the time
    time_start = time.time()
    # Start capturing the feed
    cap = cv2.VideoCapture(input_loc)
    # Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print ("Number of frames: ", video_length)
    count = 0
    print ("Converting video..\n")
    # Start converting the video
    while cap.isOpened():
        # Extract the frame
        ret, frame = cap.read()
        if not ret:
            continue
        # Write the results back to output location.
        cv2.imwrite(output_loc + "/%#05d.jpg" % (count+1), frame)
        count = count + 1
        # If there are no more frames left
        if (count > (video_length-1)):
            # Log the time again
            time_end = time.time()
            # Release the feed
            cap.release()
            # Print stats
            print ("Done extracting frames.\n%d frames extracted" % count)
            print ("It took %d seconds for conversion." % (time_end-time_start))
            break

if __name__=="__main__":

    input_loc = r"C:\Users\seema\Desktop\Seema - Personal\Desktop\COURSE\360DigiTMG Course\Projects\Pre-processing Code (Python)\8mm\VID20230413105037.mp4"
    output_loc = r"C:\Users\seema\Desktop\Seema - Personal\Desktop\COURSE\360DigiTMG Course\Projects\Pre-processing Code (Python)\Output file 8mm"
    video_to_frames(input_loc, output_loc)
    
'''
if __name__=="__main__":

        input_loc = r"C:\Users\seema\Desktop\Seema - Personal\Desktop\COURSE\360DigiTMG Course\Projects\Pre-processing Code (Python)\16mm\VID20230413113846.mp4"
        output_loc = r"C:\Users\seema\Desktop\Seema - Personal\Desktop\COURSE\360DigiTMG Course\Projects\Pre-processing Code (Python)\Output file 16mm"
        video_to_frames(input_loc, output_loc)
     
        
if __name__=="__main__":

            input_loc = r"C:\Users\seema\Desktop\Seema - Personal\Desktop\COURSE\360DigiTMG Course\Projects\Pre-processing Code (Python)\32mm\VID20230413123338.mp4"
            output_loc = r"C:\Users\seema\Desktop\Seema - Personal\Desktop\COURSE\360DigiTMG Course\Projects\Pre-processing Code (Python)\Output file 32mm"
            video_to_frames(input_loc, output_loc)
'''       

# For 8mm     
'''
Number of frames:  1282
Converting video..

Done extracting frames.
1282 frames extracted
It took 182 seconds for conversion.
'''
    
    
# For 16mm     
'''
Number of frames:  2505
Converting video..

Done extracting frames.
2505 frames extracted
It took 341 seconds for conversion.
'''


# For 32mm
'''
Number of frames:  3779
Converting video..

Done extracting frames.
3779 frames extracted
It took 508 seconds for conversion.
'''


    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
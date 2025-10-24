## What This Project Does

A video whose frames are out of order looks like the motion disappears. This project goes through the extracted frames of the disordered video, analyzes how similar or related they are in terms of motion, and then reconstructs them in the correct order. At last, it glues the frames together to a normal video that is in the right order.

It is a camera movement kind of heavy motion work kind of thing.

***

## Why I Used Optical Flow and Then Came Back to SSIM

The beginning was the easiest: just use the most renowned

**Optical Flow**

method to see how pixels move from one image to another and then deduce the correct sequence based on the continuous movement of the object. The technique gave excellent results for videos with one

clear

and

consistent

movement.

But, actual videos are not always that great. Sometimes the camera shakes, or minimal motion or repetitive backgrounds may be there. In such instances, Optical Flow could hardly do the job—it was not always capable of identifying the next frame.

Thus, I decided to work with the

SSIM (Structural Similarity Index Measure)

once again.

Compared to Optical Flow, SSIM is not dependent on motion; rather, it considers overall visual similarity—contrast, brightness, and structure. By integrating SSIM with Optical Flow, I was able to extend the possibilities of the latter. In the end, the combination yielded more fluent and visually consistent reconstructions.

***

## How the Project Works

1. **Frame Extraction:** The video is transformed into stills (frames).

2. **Frame Reordering:** The relation between one frame and the others is established through either movement flow or visual similarity.

3. **Reconstruction:** The reordered frames are stitched together again to form a continuous video.

***

## Setting Up the Environment

Be sure to have a suitable Python environment before you run the scripts.

1. **Make sure to have Python 3.8 or a more recent version.**


2. **Creating a virtual environment** 

Let your terminal point to the project folder and execute the following:

**For Windows:**

```

python -m venv venv

venv\Scripts\activate

```

**For Mac/Linux:**

```

python3 -m venv venv

source venv/bin/activate

```

3. **Install the necessary packages**

If your environment is turned on, then you can run the following command:

```

pip install opencv-python scikit-image numpy

```

That's everything. Your setup is ready for launching the project.

***

## How to Use

1. Put the video with the frames you want to reorder, in the folder called "input_video/".

2. Go ahead and execute the frame grabbing code:

```

python extract.py

```

It is all the frames (photos) of the video that have been saved in the folder called "frames/".

3. Frame reordering and video recreation:

```

python reorder.py

```

Frame recreation from reordered photos will be saved in the "ordered_frames/" directory, and thus the fixed video will be saved in the "output/" directory (in the form of an mp4 file named"unjumbledvideo.mp4").

***

## Folder Structure

```

FrameOrder/

│

├── input_video/ # Where you put the videos that need fixing

├── frames/ # Frames extracted from a jumbled video

├── ordered_frames/ # Frames are in the correct order

├── output/ # Video after being reconstructed

├── main.py # Frame extraction code

├── reorder.py # Frame reordering and video creating code

└── README.md # This ​‍​‌‍​‍‌​‍​‌‍​‍‌file

```
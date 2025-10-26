## What This Project Does

A video whose frames are out of order looks like the motion disappears. This project goes through the extracted frames of the disordered video, analyzes how similar or related they are in terms of motion, and then reconstructs them in the correct order. At last, it glues the frames together to a normal video that is in the right order.

It is a camera movement kind of heavy motion work kind of thing.

***

## Why I Used Optical Flow and Then Came Back to SSIM

At first, things seemed simple. I decided to start with  Optical Flow method to track how pixels move from one frame to the next, thought it would help me piece the frames back together in the right order. It gave me an output with few frames out of order.

But real-world videos aren’t always that perfect. Sometimes the camera shakes, or there’s barely any motion at all. In those situations, Optical Flow struggled to find the right sequence because the movement wasn’t clear enough to follow.

That’s when I turned to SSIM (Structural Similarity Index Measure). Unlike Optical Flow, SSIM doesn’t depend on motion; it compares frames based on how similar they look in terms of brightness, contrast, and structure. By combining both methods, I managed to get results that were smoother and more natural — the reconstructed videos looked far closer to the original sequence, even in tricky situations.

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

Your setup is ready for launching the project.

***

## How to Use

1. Put the video with the frames you want to reorder, in the folder called "input_video/"(as input.mp4).

2. Go ahead and execute the frame grabbing code(extract.py):

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

├── input_video/ # place the input video here

├── frames/ # Frames that are extracted from input video

├── ordered_frames/ # Ordered frames are placed here

├── output/ # Output is given here

├── extract.py # Frame extraction code

├── reorder.py # Frames are ordered and stitched here

└── README.md # This ​‍​‌‍​‍‌​‍​‌‍​‍‌file

```
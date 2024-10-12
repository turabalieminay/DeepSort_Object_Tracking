# Object Tracking using OpenCV

This project demonstrates how to implement object tracking in videos using OpenCV. Object tracking is a key task in computer vision that allows you to follow a specific object over time across multiple video frames. In this project, a single object is tracked based on user input or automatic detection, and the object is followed across the video with a bounding box drawn around it.

## Project Overview

In this project, I implemented object tracking using OpenCV in Python. The user can either manually select an object in a video or provide pre-defined regions for tracking. The object is then tracked throughout the video, with its movements being continuously updated and displayed in real-time. This technique is commonly used in surveillance, autonomous vehicles, and robotics.

## Features

- **Single Object Tracking**: Tracks one object across multiple frames in a video.
- **Manual Object Selection**: Allows users to select the object they want to track by drawing a bounding box around it.
- **Bounding Box Display**: A bounding box is drawn around the object in each frame, visually highlighting the object as it moves.
- **Multiple Tracking Algorithms**: Supports various tracking algorithms, including:
  - **BOOSTING**
  - **MIL**
  - **KCF**
  - **CSRT**
  - **MOSSE**

## How It Works

1. **Tracker Selection**:
   - The project uses OpenCV's tracking algorithms, such as BOOSTING, MIL, KCF, and CSRT. The user can choose which tracker to use for object tracking.

2. **Object Selection**:
   - The user can manually select the object to be tracked by drawing a bounding box around it using OpenCV's `cv2.selectROI()` function.

3. **Real-time Object Tracking**:
   - Once the object is selected, the tracking algorithm follows it across subsequent frames of the video. The object's position is continuously updated, and a bounding box is drawn around it.

4. **Stopping the Process**:
   - The tracking process can be stopped by pressing the 'q' key.

## How to Run

### Dependencies

To run this project, you need to install the following libraries:
- `opencv-python`
- `numpy`

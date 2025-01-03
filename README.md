# Assistive Communication Tools: Blink Matrix Encoding and Morse Code Typing

This repository contains two innovative assistive communication tools designed for individuals with limited mobility or speech impairments. These tools provide intuitive methods for communication using eye blinks detected via webcam.

## Overview

### Blink Matrix Encoding
Blink Matrix Encoding utilizes a 6x5 character grid to allow users to select characters through controlled eye blinks. The process involves navigating rows and columns to form sentences with real-time feedback.

### Morse Code Typing
Morse Code Typing enables users to communicate by inputting Morse code through eye blinks. The duration of each blink determines whether a dot (.) or a dash (-) is recorded, and these sequences are automatically decoded into text.

---

## Key Features

### Blink Matrix Encoding
- **Blink Detection with GazeTracking**: Tracks and interprets blinks in real-time using a webcam.
- **6x5 Blink Matrix**: Users navigate a grid of characters by blinking to select rows and columns sequentially.
- **Dynamic Feedback**:
  - Active rows are highlighted in green.
  - Active columns are highlighted in blue.
- **Smooth Interaction**:
  - Minimal blink time: 0.3 seconds.
  - Confirmation delay: 2 seconds.
- **Use Case**: Ideal for beginners or users prioritizing ease of use and accuracy.

#### Demo:
![Demo Video](https://github.com/Codrix1/Gaze-Tracking-Assignment/blob/main/morse%20demo.gif)


![Full Video](https://github.com/Codrix1/Gaze-Tracking-Assignment/blob/main/gaze_tracking/matrix.mp4)

---

### Morse Code Typing
- **Blink Detection**: Differentiates between short (< 0.5s) and long (≥ 0.5s) blinks.
- **Morse Code Input**:
  - Short Blink: Represents a dot (.).
  - Long Blink: Represents a dash (-).
- **Automatic Decoding**:
  - After 2 seconds of inactivity, the system decodes the Morse sequence into text.
- **Real-Time Feedback**:
  - Displays the current Morse sequence and decoded text.
- **Use Case**: Ideal for users willing to invest time in learning Morse code for higher proficiency over time.

#### Demo:

![Full Video](https://github.com/Codrix1/Gaze-Tracking-Assignment/blob/main/gaze_tracking/morse%20code.mp4)

---

## Comparative Analysis

### Time to Enter a Sentence
- Blink Matrix Encoding: ~1 minute 30 seconds .
- Morse Code Typing: ~2 minutes 14 seconds.

### Learning Curve and Accuracy
- **Blink Matrix Encoding**:
  - Faster and more accurate for beginners due to guided row/column selection.
- **Morse Code Typing**:
  - Slower initially but allows for faster input with practice.
  - Proficiency increases accuracy over time.

---
 


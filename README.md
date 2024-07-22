# Matrix-Vision and Digital-Rain

## Introduction

This project consists of two main components: Matrix Vision and Matrix Fall. Both are visual effects inspired by the iconic "Matrix Fall Animation" from the Matrix movie, implemented using Python and Pygame. The project showcases advanced use of Pygame for graphics rendering, NumPy for efficient array operations, and CustomTkinter for creating a modern GUI.

## Matrix Vision

Matrix Vision is an advanced implementation that goes beyond the basic rain effect. It uses NumPy for efficient array operations and Pygame for rendering.

### Technical Overview

- **NumPy Usage**: 
  - Efficient Multi-dimensional array operations for managing the matrix of characters
  - Array masking and rolling operations for dynamic updates

- **Core Logic**:
  - Pre-rendering of characters for performance optimization
  - Dynamic color adjustment based on input image or webcam feed
  - Efficient column shifting and character changing algorithms

## Matrix Fall

Matrix Fall is a more straightforward implementation focusing on recreating the classic digital rain effect

### Technical Highlights

- Custom color themes with dynamic color generation
- Efficient symbol management using Pygame's rendering capabilities
- Smooth alpha blending for a gradual fade-in effect

## Installation
__IMPORTANT:__
_You have to install __MS Mincho__ Font in your computer for this to work, you can find it in the Font Folder of the repository_

### Required Libraries

```
pygame
numpy
customtkinter
```

To install the required libraries, run:

```bash
pip install pygame numpy customtkinter
```

## Usage Instructions

__**Note:** For "Matrix to Image" its is better to use silhoutte images for good output__

1. Clone the repository:
   ```bash
   git clone https://github.com/Yashwanth-Kumar-Kurakula/Matrix-Vision---Digital-Rain.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Matrix-Vision-Digital-Rain
   ```

3. Run the main script:
   ```bash
   python matrix_vision.py
   ```

   or

    ```bash
   python matrix_digital_rain.py
   ```

4. In the GUI, select your desired option:
   - Matrix Fall
   - Image to Matrix Vision
   - Webcam to Matrix Vision

   or

   - Select your desired theme for Matrix Fall

5. Follow on-screen instructions for each mode.

## Screenshots

### Matrix Vision

**Matrix Fall**
![Matrix Fall](Screenshots/Matrix%20Fall.png)

**Image to Matrix Vision 1**
![Image to Matrix Vision 1](Screenshots/Image%20to%20Matrix%20Vision%201.png)

**Image to Matrix Vision 2**
![Image to Matrix Vision 2](Screenshots/Image%20to%20Matrix%20Vision%202.png)

**Webcam to Matrix Vision**
![Webcam to Matrix Vision](Screenshots/Webcam%20to%20Matrix%20Vision.png)

### Matrix Fall

**Crimson Fury**
![Crimson Fury](Screenshots/Crimson%20Fury.png)

**Neon Jungle**
![Neon Jungle](Screenshots/Neon%20Jungle.png)

**Cosmic Blue**
![Cosmic Blue](Screenshots/Cosmic%20Blue.png)

**Aqua Blaze**
![Aqua Blaze](Screenshots/Aqua%20Blaze.png)

**Misty Meadow**
![Misty Meadow](Screenshots/Misty%20Meadow.png)

**Starlit Twilight**
![Starlit Twilight](Screenshots/Starlit%20Twilight.png)

**Saturated Nebula**
![Saturated Nebula](Screenshots/Saturated%20Nebula.png)

**Solar Flare**
![Solar Flare](Screenshots/Solar%20Flare.png)

**Ember Mystic**
![Ember Mystic](Screenshots/Ember%20Mystic.png)

**Bubblegum Storm**
![Bubblegum Storm](Screenshots/Bubblegum%20Storm.png)

**Nebula Storm**
![Nebula Storm](Screenshots/Nebula%20Storm.png)

## Contributing

Contributions to improve the project are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

**MIT License**

Copyright (c) 2024 Yashwanth Kumar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Acknowledgments

- This repository is highly inspired from CoderSpace's Matrix Fall and Vision, for comprehensive understanding of the code click [here](https://youtu.be/fNoQr3q3RVc?si=BvwTxHJp7LYjSfgD)

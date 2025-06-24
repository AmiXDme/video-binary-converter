# Video to Binary Converter & Binary to Video Converter

> 📺 **Check out my YouTube channel for more cool projects and tutorials:**  
> 👉 [AmiXDme on YouTube](https://www.youtube.com/@AmiXDme)

This project provides two simple GUI tools:
- **video_to_binary.py**: Convert any video file into a text file containing the binary representation of its bytes.
- **binary_to_video.py**: Convert a binary text file back to its original binary file (e.g., video).

## 🚀 Features

- Easy-to-use graphical interface (Tkinter)
- Progress reporting during conversion
- Error handling and user notifications

## 🛠️ Installation & Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/AmiXDme/video-binary-converter.git
   cd video-binary-converter
   ```

2. **Create and Activate a Virtual Environment (Recommended):**

   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Required Dependencies:**

   No extra packages are needed; this project uses only Python's built-in libraries.

## 🖥️ Usage

- **Convert Video to Binary Text:**
  1. Run `video_to_binary.py`
  2. Select your video file (e.g., `.mp4`) and choose an output text file.
  3. Click **Convert**.

- **Convert Binary Text to Video:**
  1. Run `binary_to_video.py`
  2. Select your binary text file and choose an output file (e.g., `.mp4`).
  3. Click **Convert**.

## ▶️ Run

You can run each tool directly from the command line:

- **Video to Binary Converter:**
  ```bash
  python video_to_binary.py
  ```

- **Binary to Video Converter:**
  ```bash
  python binary_to_video.py
  ```

## ⚠️ Notes

- The output text files can be extremely large for big videos.
- The conversion is byte-for-byte; no compression or encoding is performed.
- The restored file will be identical to the original only if the binary text was not modified.
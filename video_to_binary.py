import os
import tkinter as tk
from tkinter import filedialog, messagebox
import time

def convert_video_to_binary_text(video_path, output_path):
    """
    Reads a video file's raw bytes and writes their 8-bit binary representation
    to a text file.

    Args:
        video_path (str): The absolute path to the input video file.
        output_path (str): The absolute path for the output text file.
    """
    if not os.path.exists(video_path):
        print(f"Error: Video file not found at {video_path}")
        messagebox.showerror("Conversion Error", f"Video file not found at {video_path}")
        return

    try:
        total_size = os.path.getsize(video_path)
        bytes_read = 0
        start_time = time.time()
        last_print_percentage = -1

        with open(video_path, 'rb') as video_file, open(output_path, 'w') as output_file:
            byte = video_file.read(1)
            while byte:
                bytes_read += 1
                binary_string = bin(ord(byte))[2:].zfill(8)
                output_file.write(binary_string + '\n')
                byte = video_file.read(1)

                # Print progress every 1% or every 10MB, whichever comes first
                current_percentage = (bytes_read / total_size) * 100
                if current_percentage >= last_print_percentage + 1 or bytes_read % (10 * 1024 * 1024) == 0:
                    elapsed_time = time.time() - start_time
                    if bytes_read > 0 and elapsed_time > 0:
                        bytes_per_second = bytes_read / elapsed_time
                        remaining_bytes = total_size - bytes_read
                        estimated_time_remaining = remaining_bytes / bytes_per_second
                        estimated_end_time = time.ctime(time.time() + estimated_time_remaining)
                        print(f"Progress: {current_percentage:.2f}% | Estimated End Time: {estimated_end_time}")
                    else:
                         print(f"Progress: {current_percentage:.2f}%")
                    last_print_percentage = current_percentage

        print(f"\nSuccessfully converted {video_path} to {output_path}")
        print("Note: The output file contains the raw binary data of the video as text and is likely very large and not usable for standard video playback.")
        messagebox.showinfo("Conversion Complete", "Video successfully converted to binary text.")

    except Exception as e:
        print(f"\nAn error occurred: {e}")
        messagebox.showerror("Conversion Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Video to Binary Converter")

    # Input File Selection
    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)

    input_label = tk.Label(input_frame, text="Input Video File:")
    input_label.pack(side=tk.LEFT)

    input_entry = tk.Entry(input_frame, width=50)
    input_entry.pack(side=tk.LEFT, padx=5)

    def browse_input_file():
        filename = filedialog.askopenfilename(
            title="Select Video File",
            filetypes=(("Video files", "*.mp4 *.avi *.mov *.mkv"), ("All files", "*.*"))
        )
        if filename:
            input_entry.delete(0, tk.END)
            input_entry.insert(0, filename)

    input_button = tk.Button(input_frame, text="Browse", command=browse_input_file)
    input_button.pack(side=tk.LEFT)

    # Output File Selection
    output_frame = tk.Frame(root)
    output_frame.pack(pady=10)

    output_label = tk.Label(output_frame, text="Output Text File:")
    output_label.pack(side=tk.LEFT)

    output_entry = tk.Entry(output_frame, width=50)
    output_entry.pack(side=tk.LEFT, padx=5)

    def browse_output_file():
        filename = filedialog.asksaveasfilename(
            title="Save Binary Text File",
            defaultextension=".txt",
            filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
        )
        if filename:
            output_entry.delete(0, tk.END)
            output_entry.insert(0, filename)

    output_button = tk.Button(output_frame, text="Browse", command=browse_output_file)
    output_button.pack(side=tk.LEFT)

    # Convert Button
    def start_conversion():
        input_path = input_entry.get()
        output_path = output_entry.get()
        if input_path and output_path:
            root.destroy() # Close the GUI window
            convert_video_to_binary_text(input_path, output_path)
        else:
            messagebox.showwarning("Missing Information", "Please select both input and output files.")

    convert_button = tk.Button(root, text="Convert", command=start_conversion)
    convert_button.pack(pady=20)

    root.mainloop()

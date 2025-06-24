import os
import time
import tkinter as tk
from tkinter import filedialog, messagebox

def convert_binary_text_to_video(binary_text_path, output_video_path):
    """
    Reads an 8-bit binary text file and writes the corresponding bytes
    to a new file.

    Args:
        binary_text_path (str): The absolute path to the input binary text file.
        output_video_path (str): The absolute path for the output file (e.g., with original video extension).
    """
    if not os.path.exists(binary_text_path):
        print(f"Error: Binary text file not found at {binary_text_path}")
        messagebox.showerror("Conversion Error", f"Binary text file not found at {binary_text_path}")
        return

    try:
        print(f"Starting conversion from {binary_text_path} to {output_video_path}...")
        total_size_text = os.path.getsize(binary_text_path)
        bytes_written = 0
        start_time = time.time()
        last_print_percentage = -1

        with open(binary_text_path, 'r') as input_file, open(output_video_path, 'wb') as output_file:
            for line in input_file:
                line = line.strip() # Remove newline characters
                if line:
                    try:
                        # Convert binary string to integer, then to byte
                        byte_value = int(line, 2)
                        output_file.write(bytes([byte_value]))
                        bytes_written += 1

                        # Print progress every 1% or every 10MB of output, whichever comes first
                        # Assuming each line is roughly 9 bytes in the text file (8 digits + newline)
                        # Progress based on bytes written to output file vs estimated total output size
                        # A more accurate progress would require counting lines first, which can be slow.
                        # Using bytes written / total text file size is a reasonable approximation.
                        current_percentage = (bytes_written / (total_size_text / 9)) * 100 if total_size_text > 0 else 0

                        if current_percentage >= last_print_percentage + 1 or bytes_written % (10 * 1024 * 1024) == 0:
                            elapsed_time = time.time() - start_time
                            if bytes_written > 0 and elapsed_time > 0:
                                bytes_per_second = bytes_written / elapsed_time
                                # Estimate remaining bytes based on total lines (total_size_text / 9)
                                estimated_total_output_bytes = total_size_text / 9
                                remaining_bytes = estimated_total_output_bytes - bytes_written
                                estimated_time_remaining = remaining_bytes / bytes_per_second
                                estimated_end_time = time.ctime(time.time() + estimated_time_remaining)
                                print(f"Progress: {current_percentage:.2f}% | Estimated End Time: {estimated_end_time}")
                            else:
                                 print(f"Progress: {current_percentage:.2f}%")
                            last_print_percentage = current_percentage

                    except ValueError:
                        print(f"\nWarning: Could not convert line to byte: {line}")
                        # Optionally skip or handle invalid lines

        print(f"\nSuccessfully wrote binary data to {output_video_path}")
        print("Note: This file contains the raw binary data. It is likely NOT a playable video file.")
        messagebox.showinfo("Conversion Complete", "Binary text successfully converted to file.")

    except Exception as e:
        print(f"\nAn error occurred during conversion: {e}")
        messagebox.showerror("Conversion Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Binary to File Converter")

    # Input File Selection
    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)

    input_label = tk.Label(input_frame, text="Input Binary Text File:")
    input_label.pack(side=tk.LEFT)

    input_entry = tk.Entry(input_frame, width=50)
    input_entry.pack(side=tk.LEFT, padx=5)

    def browse_input_file():
        filename = filedialog.askopenfilename(
            title="Select Binary Text File",
            filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
        )
        if filename:
            input_entry.delete(0, tk.END)
            input_entry.insert(0, filename)

    input_button = tk.Button(input_frame, text="Browse", command=browse_input_file)
    input_button.pack(side=tk.LEFT)

    # Output File Selection
    output_frame = tk.Frame(root)
    output_frame.pack(pady=10)

    output_label = tk.Label(output_frame, text="Output File:")
    output_label.pack(side=tk.LEFT)

    output_entry = tk.Entry(output_frame, width=50)
    output_entry.pack(side=tk.LEFT, padx=5)

    def browse_output_file():
        filename = filedialog.asksaveasfilename(
            title="Save Output File",
            defaultextension=".mp4", # Default to .mp4
            filetypes=(("MP4 files", "*.mp4"), ("All files", "*.*")) # Prioritize MP4
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
            convert_binary_text_to_video(input_path, output_path)
        else:
            messagebox.showwarning("Missing Information", "Please select both input and output files.")

    convert_button = tk.Button(root, text="Convert", command=start_conversion)
    convert_button.pack(pady=20)

    root.mainloop()

import io

import imageio
import numpy as np


def numpy_to_mp4_blob(images: np.ndarray, fps: float = 30.0) -> bytes:
    # Create an in-memory binary stream
    binary_stream = io.BytesIO()

    # Get the writer for MP4 format using the stream
    with imageio.get_writer(
        binary_stream, format="mp4", mode="I", fps=fps, macro_block_size=1
    ) as writer:
        for img in images:
            writer.append_data(img)

    # Get the binary blob
    binary_blob = binary_stream.getvalue()
    binary_stream.close()

    return binary_blob


def mp4_blob_to_numpy(binary_blob: bytes) -> np.ndarray:
    # Create an in-memory binary stream from the MP4 binary blob
    binary_stream = io.BytesIO(binary_blob)

    # Open the video file from the binary stream
    reader = imageio.get_reader(binary_stream, format="mp4")

    # Read all frames and convert them to a list of NumPy arrays
    frames = []
    for frame in reader:
        frames.append(frame)

    reader.close()
    return np.array(frames)

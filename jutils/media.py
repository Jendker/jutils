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

from typing import List

from PIL import Image


class GifCreator:
    @staticmethod
    def execute(
        output_filename: str, input_filenames: List[str], extension: str = "png"
    ):
        img, *imgs = [Image.open(f) for f in input_filenames if extension in f]
        img.save(
            fp=output_filename,
            format="GIF",
            append_images=imgs,
            save_all=True,
            duration=1500,
        )

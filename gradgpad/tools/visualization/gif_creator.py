from typing import List

from PIL import Image


class GifCreator:
    @staticmethod
    def execute(output_filename: str, input_filenames: List[str]):
        img, *imgs = [Image.open(f) for f in input_filenames]
        img.save(
            fp=output_filename,
            format="GIF",
            append_images=imgs,
            save_all=True,
            duration=1500,
        )

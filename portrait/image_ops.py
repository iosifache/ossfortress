from PIL import Image
from dataclasses import dataclass
from tempfile import NamedTemporaryFile


@dataclass
class ImageFormat:
    name: str
    pillow_format: str


PngImageFormat = ImageFormat("PNG", "png")
WebPImageFormat = ImageFormat("WebP", "webp")


SUPPORTED_FORMATS = [PngImageFormat, WebPImageFormat]


def convert_format_to_class(format: str) -> ImageFormat:
    for supported_format in SUPPORTED_FORMATS:
        if supported_format.pillow_format == format:
            return supported_format

    return None


def convert_format(image_path: str, output_format: ImageFormat) -> str:
    image = Image.open(image_path)

    output = NamedTemporaryFile(delete=False)

    image.save(output.name, format=output_format.pillow_format)

    return output.name

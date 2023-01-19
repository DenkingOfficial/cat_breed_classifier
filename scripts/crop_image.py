import smartcrop
from PIL import Image


def crop_image(image, width=224, height=224):
    new_image = Image.new('RGB', image.size)
    new_image.paste(image)
    image = new_image

    sc = smartcrop.SmartCrop()

    result = sc.crop(image, width=100, height=int(width / height * 100))

    box = (
        result['top_crop']['x'],
        result['top_crop']['y'],
        result['top_crop']['width'] + result['top_crop']['x'],
        result['top_crop']['height'] + result['top_crop']['y']
    )

    cropped_image = image.crop(box)
    cropped_image.thumbnail((width, height), Image.ANTIALIAS)
    return cropped_image
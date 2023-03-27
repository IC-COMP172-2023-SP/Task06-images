from image import ImageWin, FileImage, Pixel, EmptyImage
from random import randint


def create_only_red_image(old_image):
    """
    :return: a new image based on old_image with pixels only showing the red channel of rgb
    """
    new_image = EmptyImage(old_image.get_width(), old_image.get_height())
    for row in range(old_image.get_height()):
        for col in range(old_image.get_width()):
            old_pixel = old_image.get_pixel(col, row)
            # TODO: use the old pixel to make the new pixel, rather than just making a random pixel
            new_pixel = Pixel(randint(0, 255), randint(0, 255),randint(0, 255))
            new_image.set_pixel(col, row, new_pixel)
    return new_image


def create_grey_scale_image(pixel_to_change):
    """
    :return: a new image based on old_image with pixels representing gray-scale
    """
    raise RuntimeError("Not implemented")


def create_thumbnail_image(my_image):
    """
    :return: a new copy of the original image but 1/10th the size
    """
    raise RuntimeError("Not implemented")


def create_hopeify_image(old_image):
    """
    :return: a new image based on old_image with only 4 solid colors, as was done for the Obama "Hope" poster
    """
    raise RuntimeError("Not implemented")


def main():
    original_image = FileImage("yellowTree.jpg")
    width = original_image.get_width()
    height = original_image.get_height()
    win = ImageWin(width, height, "Image Processing")
    original_image.draw(win)

    new_image = create_only_red_image(original_image)
    new_image.draw(win)

    win.exit_on_click()


if __name__ == "__main__":
    main()


from image import ImageWin, FileImage, Pixel, EmptyImage


def only_red_pixel(old_pixel):
    """:return: a new pixel based on pixel_to_change, but only red (without the blue or green)"""
    raise RuntimeError("Not implemented")


# TODO: write functions for gray-scale and hopeify that take a single pixel and return a single pixel


def new_image_by_pixel(old_image, pixel_changer):
    """
    :param pixel_changer: a function that takes a Pixel as a parameter and returns a changed pixel for replacing the original
    :return: a new image with all pixels changed using the pixel_changer function
    """
    new_image = EmptyImage(old_image.get_width(), old_image.get_height())
    for row in range(old_image.get_height()):
        for col in range(old_image.get_width()):
            old_pixel = old_image.get_pixel(col, row)
            new_pixel = pixel_changer(old_pixel)
            new_image.set_pixel(col, row, new_pixel)
    return new_image


def main():
    original_image = FileImage("yellowTree.jpg")
    width = original_image.get_width()
    height = original_image.get_height()
    win = ImageWin(width, height, "Image Processing")
    original_image.draw(win)

    new_image = new_image_by_pixel(original_image, only_red_pixel)
    new_image.draw(win)

    #TODO: write code that calls new_image_by_pixel to apply your grayscale and hopeify pixel functions
    win.exit_on_click()


if __name__ == "__main__":
    main()

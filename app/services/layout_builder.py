
from PIL import Image, ImageDraw, ImageFont


def create_comic_page(
    panel_images,
    output_path="comic_page.png",
    columns=2,
    padding=20,
):
    """Arrange generated panel images into a comic page."""

    if not panel_images:
        raise ValueError("No panel images provided")

    images = [Image.open(image).convert("RGB") for image in panel_images]

    panel_width = max(image.width for image in images)
    panel_height = max(image.height for image in images)

    rows = (len(images) + columns - 1) // columns

    page_width = columns * panel_width + (columns + 1) * padding
    page_height = rows * panel_height + (rows + 1) * padding

    page = Image.new("RGB", (page_width, page_height), "white")

    for index, image in enumerate(images):
        row = index // columns
        column = index % columns

        x = padding + column * (panel_width + padding)
        y = padding + row * (panel_height + padding)

        image.thumbnail((panel_width, panel_height))
        page.paste(image, (x, y))

    page.save(output_path)

    return output_path
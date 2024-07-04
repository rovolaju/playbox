from PIL import Image, ImageChops, ImageDraw


def file_reader(file_location):
    file = open(file_location, "rt")
    content = file.readlines()
    file.close()
    return content


def capture_screens(driver, save_location, url):
    filename: str = "_screen_" + url + ".png"
    driver.save_screenshot(save_location + filename)
    return save_location + filename


def image_compare(source1, source2, location):
    img1 = Image.open(source1)
    img2 = Image.open(source2)

    diff = ImageChops.difference(img1, img2)
    if diff.getbbox():
        print("images are different")
        analyze(img1, img2, location)
    else:
        print("images are the same")


def analyze(source1, source2, location):
    screenshot_staging = Image.open(source1)
    screenshot_production = Image.open(source2)
    columns = 60
    rows = 80
    screen_width, screen_height = screenshot_staging.size

    block_width = ((screen_width - 1) // columns) + 1  # this is just a division ceiling
    block_height = ((screen_height - 1) // rows) + 1

    for y in range(0, screen_height, block_height + 1):
        for x in range(0, screen_width, block_width + 1):
            region_staging = process_region(screenshot_staging, x, y, block_width, block_height)
            region_production = process_region(screenshot_production, x, y, block_width, block_height)

            if region_staging is not None and region_production is not None and region_production != region_staging:
                draw = ImageDraw.Draw(screenshot_staging)
                draw.rectangle((x, y, x + block_width, y + block_height), outline="red")

    screenshot_staging.save(location + "result.png")


def process_region(image, x, y, width, height):
    region_total = 0
    # This can be used as the sensitivity factor, the larger it is the less sensitive the comparison
    factor = 100

    for coordinateY in range(y, y + height):
        for coordinateX in range(x, x + width):
            try:
                pixel = image.getpixel((coordinateX, coordinateY))
                region_total += sum(pixel) / 4
            except:
                return

    return region_total / factor

# create_simple_wave_divider.py
from PIL import Image, ImageDraw
import math


def create_simple_wave():
    frames = []
    width, height = 1000, 5
    num_frames = 50

    # Your orange colors
    colors = {"dark": (13, 17, 23), "mid": (123, 55, 14), "bright": (232, 93, 4)}

    for frame in range(num_frames):
        img = Image.new("RGB", (width, height), color=(20, 20, 20))
        draw = ImageDraw.Draw(img)

        # Calculate offset for continuous scrolling
        offset = (frame / num_frames) * width

        for x in range(width):
            # Create repeating gradient pattern
            position = ((x + offset) % width) / width

            # Three-color gradient cycle
            if position < 0.33:
                t = position / 0.33
                color = tuple(
                    int(colors["dark"][i] + (colors["mid"][i] - colors["dark"][i]) * t)
                    for i in range(3)
                )
            elif position < 0.66:
                t = (position - 0.33) / 0.33
                color = tuple(
                    int(colors["mid"][i] + (colors["bright"][i] - colors["mid"][i]) * t)
                    for i in range(3)
                )
            else:
                t = (position - 0.66) / 0.34
                color = tuple(
                    int(
                        colors["bright"][i]
                        + (colors["dark"][i] - colors["bright"][i]) * t
                    )
                    for i in range(3)
                )

            draw.line([(x, 0), (x, height)], fill=color)

        frames.append(img)

    frames[0].save(
        "orange_wave_divider.gif",
        save_all=True,
        append_images=frames[1:],
        duration=50,
        loop=0,
    )

    print("✓ Wave divider created!")


if __name__ == "__main__":
    create_simple_wave()

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

            # Adjusted thresholds to make the dark color larger
            first_cut = 0.5  # dark -> mid spans 50% of cycle
            second_cut = 0.6  # mid -> bright spans 10% of cycle
            # bright -> dark spans remaining 40%

            # Three-color gradient cycle with updated cuts
            if position < first_cut:
                t = position / first_cut
                color = tuple(
                    int(colors["dark"][i] + (colors["mid"][i] - colors["dark"][i]) * t)
                    for i in range(3)
                )
            elif position < second_cut:
                t = (position - first_cut) / (second_cut - first_cut)
                color = tuple(
                    int(colors["mid"][i] + (colors["bright"][i] - colors["mid"][i]) * t)
                    for i in range(3)
                )
            else:
                t = (position - second_cut) / (1 - second_cut)
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

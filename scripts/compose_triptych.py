#!/usr/bin/env python3
"""Assemble generated top/bottom panels around an untouched source-photo crop."""

import argparse
from pathlib import Path
from PIL import Image


def parse_csv(value, count, cast, label):
    parts = [cast(part.strip()) for part in value.split(",")]
    if len(parts) != count:
        raise argparse.ArgumentTypeError(f"{label} needs {count} comma-separated values")
    return parts


def cover_crop(image, width, height, crop=None):
    if crop:
        x, y, w, h = crop
        if w <= 0 or h <= 0 or x < 0 or y < 0 or x + w > image.width or y + h > image.height:
            raise ValueError("crop is outside the source image")
        image = image.crop((x, y, x + w, y + h))
    target_ratio = width / height
    ratio = image.width / image.height
    if ratio > target_ratio:
        new_w = round(image.height * target_ratio)
        left = (image.width - new_w) // 2
        image = image.crop((left, 0, left + new_w, image.height))
    elif ratio < target_ratio:
        new_h = round(image.width / target_ratio)
        top = (image.height - new_h) // 2
        image = image.crop((0, top, image.width, top + new_h))
    return image.resize((width, height), Image.Resampling.LANCZOS)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--top", required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--bottom", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--width", type=int, default=1536)
    parser.add_argument("--height", type=int, default=2304)
    parser.add_argument("--ratios", default="34,24,42")
    parser.add_argument("--crop", help="source-pixel crop: x,y,w,h")
    args = parser.parse_args()

    ratios = parse_csv(args.ratios, 3, float, "ratios")
    if min(ratios) <= 0:
        raise ValueError("ratios must be positive")
    total = sum(ratios)
    top_h = round(args.height * ratios[0] / total)
    middle_h = round(args.height * ratios[1] / total)
    bottom_h = args.height - top_h - middle_h
    crop = parse_csv(args.crop, 4, int, "crop") if args.crop else None

    with Image.open(args.top) as im:
        top = cover_crop(im.convert("RGB"), args.width, top_h)
    with Image.open(args.source) as im:
        middle = cover_crop(im.convert("RGB"), args.width, middle_h, crop)
    with Image.open(args.bottom) as im:
        bottom = cover_crop(im.convert("RGB"), args.width, bottom_h)

    canvas = Image.new("RGB", (args.width, args.height))
    canvas.paste(top, (0, 0))
    canvas.paste(middle, (0, top_h))
    canvas.paste(bottom, (0, top_h + middle_h))
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output, format="PNG", optimize=True)


if __name__ == "__main__":
    main()

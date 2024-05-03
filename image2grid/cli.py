from argparse import ArgumentParser
from argparse import Namespace

from .cropper import crop


def main():
    parser: ArgumentParser = ArgumentParser(description='Generate a grid-like images from an image')
    parser.add_argument('path', type=str, help='Path to the input image/gif file')
    parser.add_argument('-t', '--github-token', type=str, help='GitHub Token')
    args: Namespace = parser.parse_args()

    crop(args.path, args.github_token)

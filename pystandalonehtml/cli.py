"""
Usage:
    toStandalone (<input_file.html> <output_file.html>)
    toStandalone -h|--help
    toStandalone -v|--version
Options:
    <input_file.html>  File with refercences to images.
    <output_file.html>  File with images as base64.
    -h --help  Show this screen.
    -v --version  Show version.
"""
from docopt import docopt
from .converter import make_html_images_inline


def main():
    arguments = docopt(__doc__, version='0.0.1')
    input = arguments['<input_file.html>']
    output = arguments['<output_file.html>']
    make_html_images_inline(input, output)

import os
import urllib.request
import base64
import mimetypes
from bs4 import BeautifulSoup


def guess_type(filepath):
    """
    Return the mimetype of a file, given it's path.
    :type filepath: str
    :return: Mimetype string.
    :rtype: str
    """
    return mimetypes.guess_type(filepath)[0]


def file_to_base64(filepath):
    """
    Returns the content of a file as a Base64 encoded string.
    :param filepath: Path to the file.
    :type filepath: str
    :return: The file content, Base64 encoded.
    :rtype: str
    """
    with open(filepath, 'rb') as f:
        encoded_str = base64.b64encode(f.read())
    return encoded_str.decode()

def url_to_base64(url):
    """
    Returns the content of a file as a Base64 encoded string.
    :param url: URL to the file.
    :type url: str
    :return: The file content, Base64 encoded.
    :rtype: str
    """
    file = urllib.request.urlopen(url)
    encoded_str = base64.b64encode(file.read())
    return encoded_str.decode()


def splitme(s):
    if (s[0] == "\\"):
        return s[1:]
    else: 
        return(s)


def make_html_images_inline(in_filepath, out_filepath):
    """
    Takes an HTML file and writes a new version with inline Base64 encoded
    images.
    :param in_filepath: Input file path (HTML)
    :type in_filepath: str
    :param out_filepath: Output file path (HTML)
    :type out_filepath: str
    """
    basepath = os.path.split(in_filepath.rstrip(os.path.sep))[0]
    soup = BeautifulSoup(open(in_filepath, 'r'), 'html.parser')
    for img in soup.find_all('img'):
        img_path = os.path.join(basepath, img.attrs['src'])
        mimetype = guess_type(img_path)
        src = splitme(img.attrs['src'])
        if src.startswith('http') or src.startswith('file:'):
            img.attrs['src'] = "data:%s;base64,%s" % (mimetype, url_to_base64(src))
        elif not src.startswith('data'):
            print(src)
            img.attrs['src'] = "data:%s;base64,%s" % (mimetype, file_to_base64(src))
        

    with open(out_filepath, 'w') as of:
        of.write(str(soup))

import io
import os
import shutil
import zipfile
import re

import unicodedata
from PIL import Image

MAX_FILESIZE = 20 * 1024 ** 3  # 20MB


def set_dir(filepath):
    """
    Create a folder if the given path does not exist.
    Otherwise remove and recreate the folder.
    :param filepath: path
    :return:
    """
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    else:
        shutil.rmtree(filepath)
        os.mkdir(filepath)


def ensure_dir(dir_path):
    """
    Create a folder if the given path does not exist.
    :param dir_path:
    :return:
    """
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        pass


def slugify(value, allow_unicode=False):
    """
    Convert to ASCII if 'allow_unicode' is False. Convert spaces to hyphens.
    Remove characters that aren't alphanumerics, underscores, or hyphens.
    Convert to lowercase. Also strip leading and trailing whitespace.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return re.sub(r'[-\s]+', '-', value)


def zip_file(src_dir):
    """
    Compress the given folder
    :param src_dir:
    :return:
    """
    zip_name = slugify(src_dir) + '.zip'
    z = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(src_dir):
        fpath = dirpath.replace(src_dir, '')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            z.write(os.path.join(dirpath, filename), fpath + filename)
    z.close()


def secure_filetype(file):
    """
    Secure the uploaded file is an image
    :param file:
    :return: bool
    """
    ext_list = ['png', 'jpg', 'jpeg']
    ext_valid = file.filename.split('.')[-1] in ext_list

    mimetype_list = ["image/jpeg", "image/jpg", "image/png"]
    mimetype_valid = file.mimetype in mimetype_list

    return ext_valid and mimetype_valid


def secure_filesize(filepath):
    """
    Secure the size of the uploaded file is smaller than MAX_FILESIZE
    :param filepath:
    :return: bool
    """
    return os.path.getsize(filepath) <= MAX_FILESIZE


def check_and_save_img(file, path):
    """
    save file as an image if valid
    :param file:
    :param path:
    :return:
    """
    img_bytes = file.read()
    if not secure_filetype(file):
        return "Not an image. "
    input_image = Image.open(io.BytesIO(img_bytes))
    input_image.save(path)
    if not secure_filesize(path):
        return "Too large given file. "
    return ''

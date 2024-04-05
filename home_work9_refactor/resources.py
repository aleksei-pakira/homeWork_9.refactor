import os.path
from tests.conftest import resource_dir


def image_file_path(upload_image_file):
    file_path_image = os.path.join(resource_dir, upload_image_file)
    return file_path_image

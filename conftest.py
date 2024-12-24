import pytest
import os
from zipfile import ZipFile
from script_os import TMP_DIR


@pytest.fixture(scope="session", autouse=True)
def create_zip_file(zip_name="zip_file.zip"):
    if not os.path.exists(TMP_DIR):
        os.mkdir(TMP_DIR)
    zip_path = os.path.join(TMP_DIR, zip_name)

    with ZipFile(zip_path, 'w') as zip_file:
        for file in os.listdir(TMP_DIR):
            add_file = os.path.join(TMP_DIR, file)
            if os.path.isfile(add_file) and add_file != zip_path:
                zip_file.write(add_file, os.path.basename(add_file))
    yield

    if os.path.exists(zip_path):
        os.remove(zip_path)

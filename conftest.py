import pytest
import os
from zipfile import ZipFile
from script_os import TMP_DIR


@pytest.fixture(scope="session", autouse=True)
def create_zip_file(zip_name="zip_file.zip", directory=TMP_DIR):
    if not os.path.exists(TMP_DIR):
        os.mkdir(TMP_DIR)

    with ZipFile(zip_name, 'w') as zip_file:
        for file in os.listdir(TMP_DIR):
            add_file = os.path.join(TMP_DIR, file)
            zip_file.write(add_file, os.path.basename(add_file))
    yield

    if os.path.exists('zip_file.zip'):
        os.remove('zip_file.zip')

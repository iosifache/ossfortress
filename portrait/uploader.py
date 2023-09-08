import os
import tarfile
import tempfile

from portrait.os_ops import get_home_dir


def get_upload_dir(username: str, destination_folder: str) -> str:
    return os.path.join(get_home_dir(username), destination_folder)


def extract_archive_in_user_home(
    file: str, username: str, destination_folder: str
) -> bool:
    extract_dir = get_upload_dir(username, destination_folder)

    return extract_archive(file, extract_dir)


def extract_archive(file: str, extract_dir: str) -> bool:
    tmp = tempfile.gettempdir()
    path = os.path.join(tmp, file.filename)
    file.save(path)

    if tarfile.is_tarfile(path):
        tar = tarfile.open(path, "r:gz")
        tar.extractall(tmp)

        os.makedirs(extract_dir, exist_ok=True)
        for tarinfo in tar:
            name = tarinfo.name
            if tarinfo.isreg():
                try:
                    filename = f"{extract_dir}/{name}"
                    os.rename(os.path.join(tmp, name), filename)

                    continue
                except Exception:
                    pass

            os.makedirs(f"{extract_dir}/{name}", exist_ok=True)
        tar.close()

        return True

    return False

"""Constants, enums, and code used by most other files."""

from enum import Enum
from pathlib import Path


class GramType(Enum):
    SPECTROGRAMS = "spectrograms"
    SCALEOGRAMS = "scaleograms"


class TrainOrTest(Enum):
    TRAIN = "train"
    TEST = "test"


DATA_COMPRESSED_DIR = "data_compressed"
DATA_ORIGINAL_DIR = "data_original"
DATA_PROCESSED_DIR = "data_processed"


def get_absolute_dir(dir_name: str, create_dir: bool = True) -> Path:
    """Creates a directory with the specified name in a location relative to
    the code file, and returns the absolute path to that directory.

    This way, the behavior of our code will be the same, regardless of the
    location from where we run the project.
    """
    parent_path = Path(__file__).parent.parent
    path = Path(parent_path, dir_name).resolve()
    if create_dir:
        path.mkdir(exist_ok=True, parents=True)
    return path

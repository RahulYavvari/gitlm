import yaml, pathlib

__config_file = "../../config.yaml"

config_file = pathlib.Path(__file__).parents[2] / "config.yaml"

config = yaml.safe_load(config_file.read_text())

_MODEL_REPO_ID = config["MODEL"]["REPO_ID"]
_MODEL_URL = config["MODEL"]["URL"]
_MODEL_FILENAME = config["MODEL"]["FILENAME"]
__VERSION__ = config["VERSION"]
__AUTHOR__ = config["AUTHOR"]

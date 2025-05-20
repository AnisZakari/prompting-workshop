from importlib.resources import files
from pathlib import Path


def load_json(path: str) -> dict:
    import json

    with open(path, "r") as f:
        return json.load(f)


def load_yaml(path: str) -> dict:
    import yaml

    with open(path, "r") as f:
        return yaml.safe_load(f)


def get_root_dir() -> Path:
    return files("prompting_workshop").parent


def load_rag_data() -> list[str]:
    data = load_yaml(get_root_dir() / "data" / "rag" / "faq_the_spoon.yml")
    return data["faq"]

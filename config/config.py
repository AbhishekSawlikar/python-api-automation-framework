import json
import os
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent / "environments.json"


class Config:
    ENV = os.getenv("TEST_ENV", "qa").lower()

    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        _envs = json.load(f)

    BASE_URL = _envs.get(ENV, _envs["qa"])["base_url"]
    TIMEOUT = _envs.get(ENV, _envs["qa"])["timeout"]
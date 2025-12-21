from pathlib import Path

# Get project root directory (KidneyScan)
ROOT_DIR = Path(__file__).resolve().parents[3]

CONFIG_FILE_PATH = ROOT_DIR / "config" / "config.yaml"
PARAMS_FILE_PATH = ROOT_DIR / "params.yaml"

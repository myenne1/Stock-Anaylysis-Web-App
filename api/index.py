import importlib.util
import os
import sys

from mangum import Mangum


CURRENT_DIR = os.path.dirname(__file__)
BACKEND_DIR = os.path.join(CURRENT_DIR, "..", "backend")
BACKEND_API_DIR = os.path.join(BACKEND_DIR, "api")

# Make backend modules importable (analyze.py depends on backend/*.py)
sys.path.insert(0, BACKEND_API_DIR)
sys.path.insert(0, BACKEND_DIR)

api_path = os.path.join(BACKEND_API_DIR, "api.py")
spec = importlib.util.spec_from_file_location("backend_api", api_path)
backend_api = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
assert spec and spec.loader
spec.loader.exec_module(backend_api)

handler = Mangum(backend_api.app)

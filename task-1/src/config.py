"""Configuration loader.

Read INPUT_PATH and OUTPUT_PATH from a .env file (see .env.example for the
expected variable names) and expose them as named imports.

Tasks (see chapter Task 1):
  1. Use python-dotenv's load_dotenv() to read the .env file.
  2. Read INPUT_PATH and OUTPUT_PATH from os.environ.
  3. Raise ValueError if either is missing — do NOT let None silently propagate.
"""
import os
from dotenv import load_dotenv
#print("dotenv works!")

# Load .env values into os.environ before they're read by _required().
# (Step 1 from the docstring above; already wired up so the rest of the
# module can rely on os.environ being populated.)
load_dotenv()


def _required(name: str) -> str:
    """Read an env var; fail loudly if missing."""
    path = os.environ.get(name)
    if path is None:
      raise ValueError(f"Missing required environment path: {name},See .env.example for details.")
    return path



# TODO 3: Replace the placeholder lines below by calling _required(...) for
# each variable. INPUT_PATH and OUTPUT_PATH must be importable from this
# module by the rest of the pipeline as a relative import
# (`from .config import INPUT_PATH, ...`), since the pipeline runs as
# `python -m src.pipeline`.
INPUT_PATH: str = _required("INPUT_PATH")
OUTPUT_PATH: str = _required("OUTPUT_PATH") 
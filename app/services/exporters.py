from pathlib import Path
import shutil


def export_file(source_path: str, output_path: str) -> str:
    """Copy a generated comic file to the requested output location."""

    source = Path(source_path)
    destination = Path(output_path)

    if not source.exists():
        raise FileNotFoundError(f"Source file not found: {source}")

    destination.parent.mkdir(parents=True, exist_ok=True)

    shutil.copy2(source, destination)

    return str(destination)
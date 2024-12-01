import os
import shutil
from datetime import datetime
import uuid
import time 
from config_loader import load_config

# Load configuration
config = load_config()

# Core Feature 1: Directory Setup
def create_project_dirs(base_path):
    """Creates a directory structure based on YAML configuration."""
    structure = config["directories"]
    for folder, subfolders in structure.items():
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)
        for sub in subfolders:
            os.makedirs(os.path.join(base_path, folder, sub), exist_ok=True)
    print(f"Project directories created at {base_path}")

# Core Feature 2: Backup Utility
def backup_project(base_path, archive_name=None):
    """Compresses the project directory into a zip file."""
    archive_name = archive_name or config["backup"]["default_archive_name"]
    shutil.make_archive(archive_name, "zip", base_path)
    print(f"Project backed up as {archive_name}.zip")

def generate_filename(prefix=None, ext=None):
    """Generates a unique filename."""
    prefix = prefix or "_"
    ext = ext or "txt"
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    unique_id = uuid.uuid4().hex[:6]  # Generate 6-character unique ID
    return f"{prefix}_{timestamp}-{unique_id}.{ext}"

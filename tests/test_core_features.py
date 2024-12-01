import os
from datetime import datetime
from src.core_features import create_project_dirs, generate_filename
import pytest

# Helper function to validate directory structure
def check_directory_structure(base_path, structure):
    for folder, subfolders in structure.items():
        assert (base_path / folder).exists(), f"Missing directory: {folder}"
        for sub in subfolders:
            assert (base_path / folder / subfolder).exists(), f"Missing subdirectory: {subfolder}"

def test_create_project_dirs(tmp_path):
    base_path = tmp_path / "test_project"
    create_project_dirs(base_path)

    # Check directory structure
    expected_structure = {
        "input": [],
        "output": ["plots", "tables"],
        "logs": [],
        "temp": []
    }
    check_directory_structure(base_path, expected_structure)

    # Ensure no unexpected directories
    unexpected_dirs = list(base_path.glob("*"))
    assert len(unexpected_dirs) == len(expected_structure), "Unexpected directories created."

def test_create_project_dirs_existing(tmp_path):
    base_path = tmp_path / "test_project"
    os.makedirs(base_path / "input")  # Pre-create a directory
    create_project_dirs(base_path)

    # Ensure it doesn't overwrite existing directories
    assert (base_path / "input").exists(), "Existing directory 'input' was overwritten."
    assert (base_path / "output" / "plots").exists(), "Subdirectory 'plots' under 'output' was not created."

def test_generate_filename():
    filename = generate_filename("test", "txt")

    # Check prefix and extension
    assert filename.startswith("test_"), "Filename prefix does not match."
    assert filename.endswith(".txt"), "Filename extension does not match."

    # Check timestamp format
    timestamp_str = filename.split("_")[1].split(".")[0]
    try:
        datetime.strptime(timestamp_str, "%Y%m%d-%H%M%S")
    except ValueError:
        pytest.fail("Timestamp format is invalid")

    # Check uniqueness
    filename2 = generate_filename("test", "txt")
    assert filename != filename2, "Generated filenames are not unique."

def test_generate_filename_edge_cases():
    # Empty prefix and unusual extension
    filename = generate_filename("", "log")
    assert filename.startswith("_"), "Filename does not start with an underscore for an empty prefix."
    assert filename.endswith(".log"), "Filename extension does not match."

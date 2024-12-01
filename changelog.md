# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/), and this project adheres to [Semantic Versioning](https://semver.org/).

---

## [v0.1.0] - 2024-11-30
### Added
- **Initial release** of StructPy, a Python-based tool for managing academic data projects.
- Directory Creation:
  - Automatically generate project directory structures based on customizable YAML configurations.
- File Naming:
  - Generate unique, timestamped filenames with user-defined prefixes and extensions.
- Dataset Validation:
  - Validate datasets for:
    - Missing values, with configurable thresholds.
    - Duplicate column names.
    - Numeric outliers based on IQR.
- Backup Utility:
  - Compress project directories into `.zip` archives for safekeeping and sharing.
- Configurable Settings:
  - Support for YAML configuration files to customize tool behavior.
- Command-Line Interface:
  - Easy-to-use CLI for all core functionalities:
    - `create_dirs`: Create project directories.
    - `generate_filename`: Generate unique filenames.
    - `validate`: Validate datasets.
    - `backup`: Backup projects into `.zip` files.
- Unit Tests:
  - Test coverage for core features (`create_dirs`, `generate_filename`, `validate`, `backup`).

---




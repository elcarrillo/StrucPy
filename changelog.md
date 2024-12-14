# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/), and this project adheres to [Semantic Versioning](https://semver.org/).

---

## [Unreleased]
### Added
- None
---

## [v0.1.0] - 2024-11-30
### Added
- **Initial release** of StructPy, a Python-based tool for managing academic data projects, aimed at simplifying workflows for researchers and data practitioners.
- **Directory Creation**:
  - Automatically generate project directory structures based on customizable YAML configurations.
- **File Naming**:
  - Generate unique, timestamped filenames with user-defined prefixes and extensions.
- **Dataset Validation**:
  - Validate datasets for:
    - Missing values, with configurable thresholds.
    - Duplicate column names.
    - Numeric outliers based on IQR (Interquartile Range).
- **Backup Utility**:
  - Compress project directories into `.zip` archives for safekeeping and sharing.
- **Configurable Settings**:
  - Support for YAML configuration files to customize tool behavior.
- **Command-Line Interface (CLI)**:
  - Easy-to-use CLI for all core functionalities:
    - `create_dirs`: Automatically create nested project directories.
    - `generate_filename`: Create unique, descriptive filenames for files.
    - `validate`: Analyze datasets for structural issues or anomalies.
    - `backup`: Archive project files into `.zip` for easy sharing.
- **Unit Tests**:
  - Comprehensive test coverage for core features:
    - Directory creation (`create_dirs`).
    - Filename generation (`generate_filename`).

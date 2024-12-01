from setuptools import setup, find_packages

setup(
    name="StructPy",                           # Updated package name
    version="0.1.0",                           # Version number
    description="A Python-based tool for managing academic data projects.",  # Short description
    long_description=open("README.md").read(), # Use README.md as the long description
    long_description_content_type="text/markdown",
    author="Edgar L Carrillo",                 
    author_email="edgarc.ec@gmail.com",        
    url="https://github.com/elcarrillo/StructPy",  
    license="MIT",                             # Specify your license
    packages=find_packages(where="src"),       # Look for packages in the 'src/' folder
    package_dir={"": "src"},                   # Root package is in 'src'
    py_modules=["main"],                       # Include the main CLI script
    include_package_data=True,                 # Include config.yaml and other files
    install_requires=[
        "pandas>=1.3.0",
        "pyyaml>=6.0",
        "pytest>=7.0.0",                       # Remove if not needed in production
        "setuptools>=65.0.0"
    ],
    entry_points={
        "console_scripts": [
            "structpy=main:main"              # Creates a CLI command `structpy`
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",  
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    python_requires=">=3.8",                   # Minimum Python version
)

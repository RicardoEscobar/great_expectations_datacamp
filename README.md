# Great Expectations DataCamp

This repository is dedicated to learning and experimenting with the [Great Expectations](https://greatexpectations.io/) Python package, a powerful tool for data validation, documentation, and profiling.

## What is Great Expectations?
Great Expectations helps you maintain data quality and improve pipeline reliability by providing:
- Data validation and testing
- Automated documentation
- Data profiling

## Getting Started

### (Optional) Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies and avoid conflicts. You can use either `venv` (built-in) or `virtualenv`.

#### Using venv (Python 3.3+)
```powershell
python -m venv .venv
.venv\Scripts\activate

> **Troubleshooting (Windows PowerShell):**
> If you see an error about script execution being disabled when activating the environment, run the following command in PowerShell to allow local scripts:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
> Then try activating the environment again.
```

#### Using virtualenv
First, install virtualenv if you don't have it:
```powershell
pip install virtualenv
```
Then create and activate the environment:
```powershell
virtualenv .venv
.venv\Scripts\activate
```

### Installation
To install Great Expectations, run the following command in your terminal:

```powershell
pip install great_expectations
```

> **Troubleshooting (Windows: C/C++ Compiler Required)**
> If you see errors like the following when installing numpy or other packages:
> ```
> ERROR: Unknown compiler(s): [['icl'], ['cl'], ['cc'], ['gcc'], ['clang'], ['clang-cl'], ['pgcc']]
> Running `cl /?` gave "[WinError 2] The system cannot find the file specified"
> error: metadata-generation-failed
> × Encountered error while generating package metadata.
> ```
> This means your system is missing the required C/C++ compilers to build some Python packages from source.

> **How to fix:**
> 1. Go to https://visualstudio.microsoft.com/visual-cpp-build-tools/
> 2. Download and run the installer.
> 3. Select "C++ build tools" and make sure "Windows 10 SDK" (or newer) is checked.
> 4. Click "Install" and wait for the installation to complete.
> 5. Restart your terminal and try installing the package again.

> Most users can avoid this by using a supported Python version (e.g., 3.11 or 3.12) with pre-built binary wheels.

### Usage
After installation, you can start using Great Expectations in your Python scripts or notebooks. Refer to the [official documentation](https://docs.greatexpectations.io/docs/) for tutorials and examples.

## Repository Structure
This repository contains code samples, notes, and exercises related to learning Great Expectations.

## Resources
- [Great Expectations Documentation](https://docs.greatexpectations.io/docs/)
- [DataCamp Course](https://www.datacamp.com/)

## License
This project is for educational purposes.

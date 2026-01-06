
# Great Expectations Project Setup

This repository is dedicated to learning and experimenting with the [Great Expectations](https://greatexpectations.io/) Python package, a powerful tool for data validation, documentation, and profiling. It uses **Great Expectations 1.5.9** and requires **Python 3.12**.

---

## What is Great Expectations?
Great Expectations helps you maintain data quality and improve pipeline reliability by providing:
- Data validation and testing
- Automated documentation
- Data profiling

---

## 1. Install Python 3.12

1. Download Python 3.12 from the official site:
	[https://www.python.org/downloads/release/python-3120/](https://www.python.org/downloads/release/python-3120/)

2. During installation:
	- Check **"Add Python 3.12 to PATH"**.
	- Select **"Customize installation"** if you want to change the installation path (default is recommended).

3. Verify the installed version:
	```bash
	python --version
	```
	You should see something like:
	```
	Python 3.12.10
	```
	> ⚠️ You can keep other Python versions installed. Windows allows multiple versions in parallel.

---

## 2. Create a Virtual Environment
You can use either `venv` (included with Python) or `virtualenv`.

### Option A: Using venv
From your project folder:

```bash
# Remove old venv if it exists
rm -rf .venv

# Create new virtual environment with Python 3.12
python -m venv .venv

# Activate the environment
# On Git Bash:
source .venv/Scripts/activate
# On PowerShell:
.\.venv\Scripts\Activate
```

### Option B: Using virtualenv
If you prefer `virtualenv`, first install it:

```bash
pip install virtualenv
```
Then create the virtual environment, making sure to use Python 3.12:

```bash
# Remove old venv if it exists
rm -rf .venv

# Create new virtual environment with Python 3.12
# On Bash (macOS/Linux/Git Bash):
virtualenv -p python3.12 .venv
# Or, if python3.12 is not in your PATH, use the full path:
virtualenv -p "/path/to/python3.12" .venv
# On Windows PowerShell (if python3.12 is in your PATH):
virtualenv -p python3.12 .venv
# Or, use the full path to python.exe:
virtualenv -p "C:/Users/<YourUser>/AppData/Local/Programs/Python/Python312/python.exe" .venv

# Activate the environment
# On Bash (macOS/Linux/Git Bash):
source .venv/Scripts/activate
# On PowerShell:
.\.venv\Scripts\Activate
```

**Tip:** Always verify your Python version before creating the environment:
```bash
python3.12 --version
```

---

## 3. Install Great Expectations 1.5.9
With the virtual environment active:

```bash
pip install --upgrade pip
pip install great_expectations==1.5.9
```

Verify the installation:

```bash
python -c "import great_expectations as ge; print(ge.__version__)"
```
You should see:
```
1.5.9
```

---

## Troubleshooting

### Windows PowerShell Script Execution
If you see an error about script execution being disabled when activating the environment, run the following command in PowerShell to allow local scripts:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then try activating the environment again.

### C/C++ Compiler Required (Windows)
If you see errors like the following when installing numpy or other packages:
```
ERROR: Unknown compiler(s): [['icl'], ['cl'], ['cc'], ['gcc'], ['clang'], ['clang-cl'], ['pgcc']]
Running `cl /?` gave "[WinError 2] The system cannot find the file specified"
error: metadata-generation-failed
× Encountered error while generating package metadata.
```
This means your system is missing the required C/C++ compilers to build some Python packages from source.

**How to fix:**
1. Go to https://visualstudio.microsoft.com/visual-cpp-build-tools/
2. Download and run the installer.
3. Select "C++ build tools" and make sure "Windows 10 SDK" (or newer) is checked.
4. Click "Install" and wait for the installation to complete.
5. Restart your terminal and try installing the package again.

Most users can avoid this by using a supported Python version (e.g., 3.11 or 3.12) with pre-built binary wheels.

---

## Usage
After installation, you can start using Great Expectations in your Python scripts or notebooks. Refer to the [official documentation](https://docs.greatexpectations.io/docs/) for tutorials and examples.

## Repository Structure
This repository contains code samples, notes, and exercises related to learning Great Expectations.

## Resources
- [Great Expectations Documentation](https://docs.greatexpectations.io/docs/)
- [DataCamp Course](https://www.datacamp.com/)

## License
This project is for educational purposes.

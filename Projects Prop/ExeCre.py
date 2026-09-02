import os
import sys
import subprocess
import shutil

def create_exe(py_file_path, one_file=True, console=True):
    """
    Converts a Python script into a Windows executable using PyInstaller.

    :param py_file_path: Path to the Python script (.py) to convert.
    :param one_file: If True, bundle into a single .exe file.
    :param console: If True, keep console window; if False, hide it (GUI apps).
    """
    # Validate file path
    if not os.path.isfile(py_file_path):
        print(f"Error: File '{py_file_path}' not found.")
        return

    # Ensure PyInstaller is installed
    try:
        import PyInstaller  # noqa: F401
    except ImportError:
        print("PyInstaller not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

    # Build PyInstaller command
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--noconfirm"
    ]
    if one_file:
        cmd.append("--onefile")
    if not console:
        cmd.append("--noconsole")
    cmd.append(py_file_path)

    print("Running:", " ".join(cmd))
    subprocess.run(cmd, check=True)

    # Move the .exe to current directory for convenience
    dist_path = os.path.join("dist", os.path.splitext(os.path.basename(py_file_path))[0] + ".exe")
    if os.path.exists(dist_path):
        shutil.move(dist_path, os.path.basename(dist_path))
        print(f"Executable created: {os.path.basename(dist_path)}")
    else:
        print("Error: Executable not found in dist/ folder.")

if __name__ == "__main__":
    # Example usage: change 'script.py' to your Python file
    target_script = "Start.py"  # Replace with your file
    create_exe(target_script, one_file=True, console=True)

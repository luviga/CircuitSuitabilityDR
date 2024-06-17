import subprocess
import sys

def install_packages_from_requirements(file_path):
    with open(file_path, 'r') as file:
        packages = file.readlines()
        packages = [package.strip() for package in packages if package.strip()]

    for package in packages:
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            print(f"Successfully installed {package}")
        except subprocess.CalledProcessError:
            print(f"Failed to install {package}")

# Path to your requirements.txt file
requirements_path = 'requirements.txt'
install_packages_from_requirements(requirements_path)


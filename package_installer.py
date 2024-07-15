import sys
import subprocess
import os

def install_packages():
    plugin_path = os.path.dirname(__file__)
    # req_path = os.path.join(plugin_path,"requirements.txt").replace("\\","/")
    target_path = os.path.join(plugin_path,"ext-libs").replace("\\","/")
    # Find the full path to the pip executable
    py_version = sys.version.split(".")
    py_folder = "Python"+py_version[0]+py_version[1]
    pip_executable =""
    if os.name == "nt":
        pip_executable = os.path.join(os.path.dirname(os.path.dirname(sys.executable)), 'apps',py_folder,"Scripts", 'pip3.exe')
    elif os.name == "posix":
        pip_executable = os.path.join(os.path.dirname(os.path.dirname(sys.executable)), 'bin','pip3')
    ext_libs_path = os.path.join(os.path.dirname(__file__), 'site-packages')
    packages_to_install = ['PyCRS','folium', 'rasterio', 'rtree', 'pandas', 'geopandas', 'geemap', 'mapclassify', 'contextily', 'matplotlib_scalebar', 'opencv-python', 'natsort', 'scikit-learn']
    try:
        upgrade_pip_command = [pip_executable,'install','--upgrade','pip']
        subprocess.run(upgrade_pip_command, check=True)
    except subprocess.CalledProcessError as e:
            print(f"Error upgrading pip: {e}")
    for package in packages_to_install:
        try:
            
            command = [pip_executable,"install","--upgrade",package,"--target",target_path]
            subprocess.run(command, check=True)
            print(f"{package} installed Successfully")
        except subprocess.CalledProcessError as e:
            print(f"Error installing the dependencies: {e}")
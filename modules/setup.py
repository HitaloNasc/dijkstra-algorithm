
import subprocess


def install_dependencies():
    subprocess.run(['pip', 'install', 'csv'])
    subprocess.run(['pip', 'install', 'typing'])
    subprocess.run(['pip', 'install', 'networkx'])
    subprocess.run(['pip', 'install', 'matplotlib'])
    subprocess.run(['pip', 'install', 'Pillow'])

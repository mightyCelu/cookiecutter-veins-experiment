import pathlib
import subprocess

# Veins
pathlib.Path('{{ cookiecutter.veins.path }}').mkdir(parents=True)
subprocess.call(['git', 'init'], cwd='{{ cookiecutter.veins.path }}')
subprocess.call(['git', 'remote', 'add', 'origin', '{{ cookiecutter.veins.repository }}'], cwd='{{ cookiecutter.veins.path }}')
subprocess.call(['git', 'fetch'], cwd='{{ cookiecutter.veins.path }}')
subprocess.call(['git', 'checkout', '{{ cookiecutter.veins.version }}'], cwd='{{ cookiecutter.veins.path }}')

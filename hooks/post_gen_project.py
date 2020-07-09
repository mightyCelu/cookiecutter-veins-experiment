import pathlib
import subprocess

# Veins
pathlib.Path('{{ cookiecutter.veins.path }}').mkdir(parents=True)
subprocess.call(['git', 'init'], cwd='{{ cookiecutter.veins.path }}')
subprocess.call(['git', 'remote', 'add', 'origin', '{{ cookiecutter.veins.repository }}'], cwd='{{ cookiecutter.veins.path }}')
subprocess.call(['git', 'fetch'], cwd='{{ cookiecutter.veins.path }}')
subprocess.call(['git', 'checkout', '{{ cookiecutter.veins.version }}'], cwd='{{ cookiecutter.veins.path }}')

# Veins-VLC
pathlib.Path('{{ cookiecutter.vlc.path }}').mkdir(parents=True)
subprocess.call(['git', 'init'], cwd='{{ cookiecutter.vlc.path }}')
subprocess.call(['git', 'remote', 'add', 'origin', '{{ cookiecutter.vlc.repository }}'], cwd='{{ cookiecutter.vlc.path }}')
subprocess.call(['git', 'fetch'], cwd='{{ cookiecutter.vlc.path }}')
subprocess.call(['git', 'checkout', '{{ cookiecutter.vlc.version }}'], cwd='{{ cookiecutter.vlc.path }}')

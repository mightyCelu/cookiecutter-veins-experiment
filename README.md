# Cookiecutter generator for a Veins experiment
Creates a [Veins](https://veins.car2x.org) experiment. Veins is cloned into a subdirectory and configured as a dependency of the experiment.

## Usage:

    cookiecutter cookiecutter-veins-experiment

This repository supports different experiment types, at the moment 'Veins' (default) and 'Plexe'.
These can be used by specifying the corresponding branches, e.g.:

    cookiecutter cookiecutter-veins-experiment -c plexe

After this, the directory is set up, you only need to add experiment configuration to `scenario`. Then, run:

    ./configure
    make

And execute your experiment from within `scenario` with:

    ./run -u Cmdenv -c <config>


## Notes:
- You might want to consider versioning your experiment directory.
- The branches for different experiment types in this repository are rewritten regularly to include changes on the master branch.

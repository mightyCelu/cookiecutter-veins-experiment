# Cookiecutter generator for a Veins experiment
Creates a [Veins](https://veins.car2x.org) experiment. Veins is cloned into a subdirectory and configured as a dependency of the experiment.

## Usage:

    cookiecutter cookiecutter-veins-experiment

After this, the directory is set up, you only need to add experiment configuration to `scenario`. Then, run:

    ./configure
    make

And execute your experiment from within `scenario` with:

    ./run -u Cmdenv -c <config>

You might want to consider versioning your experiment directory.

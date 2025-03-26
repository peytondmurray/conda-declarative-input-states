# conda-declarative-input-states

A conda plugin which automatically writes the current state of the environment
to `<prefix>/conda-meta/env.yml`.

## Installation

This package needs to be installed into the base conda environment:

```
conda activate base
pip install git+https://github.com/peytondmurray/conda-declarative-input-states
```

Or, clone the repository and install from source:

```bash
git clone https://github.com/peytondmurray/conda-declarative-input-states
cd conda-declarative-input-states
conda activate base
pip install .  # Use -e for "editable" mode
```

## Usage

When any of the following conda subcommands are run, the `env.yml` will be
updated with the current environment spec:

- create
- install
- remove
- uninstall
- update
- upgrade
- env create
- env remove
- env update

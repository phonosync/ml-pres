# Machine Learning Presentations
## index.html
relative links to all presentations (has to be updated manually)

## Local development environment

### Python Environment Setup and Management
**Install** conda environment:
```sh
$ conda env create -f conda.yml
```
**Update** the environment with new packages/versions:
1. modify template.yml
2. run `conda env update`:
```sh
$ conda env update --name ml_pres --file conda.yml --prune
```
`prune` uninstalls dependencies which were removed from vdss.yml

**Use** environment:
before working on the project always make sure you have the environment activated:
```sh
$ conda activate mld_pres
```

**Check the version** of a specific package (e.g. `html5lib`) in the environment:
```sh
$ conda list html5lib
```

**Export** an environment file across platforms:
Include only the packages that were specifically installed. Dependencies will be resolved upon installation
```sh
$ conda env export --from-history > conda.yml
```

**List** all installed environments:
From the base environment run
```sh
$ conda info --envs
```

**Remove** environment:
```sh
$ conda env remove -n vdss
```

See the complete documentation on [managing conda-environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

### Runtime Configuration with Environment Variables
The environment variables are specified in a .env-file, which is never commited into version control, as it may contain secrets. The repo just contains the file `.env.template` to demonstrate how environment variables are specified.

You have to create a local copy of `.env.template` in the project root folder and the easiest is to just name it `.env`.

The content of the .env-file is then read by the pypi-dependency: `python-dotenv`. Usage:
```python
import os
from dotenv import load_dotenv
```

`load_dotenv` reads the .env-file and sets the environment variables:

```python
load_dotenv()
```
which can then be accessed:

```python
os.environ['SAMPLE_VAR']
```

### Quarto
[https://quarto.org/docs/download/](https://quarto.org/docs/download/)

Optional: VS Code quarto extension  
If you want to use VS code, which has very convenient editing and preview features 

## presentations in subfolders
global configurations in `_quarto.yml`

`conda activate ml_pres`

`quarto preview recommender_systems/assoc_rules/assoc_rules.qmd`

```quarto render recommender_systems/assoc_rules/assoc_rules.qmd```produces the revealjs-presentations in html format.


## pdf converstion
### Installation Decktape

Instructions: https://docs.npmjs.com/downloading-and-installing-node-js-and-npm

1. install nvm: https://github.com/nvm-sh/nvm
    * curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
2. install node: `nvm install node`
3. `npm install -g decktape`

### Usage Decktape
`decktape <input>.html <output>.pdf`

Step through fragments: `decktape generic --key=ArrowRight <input>.html <output>.pdf`

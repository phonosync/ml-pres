# Machine Learning Presentations
## index.html
relative links to all presentations (has to be updated manually)

## Local development environment

### Python Environment Setup and Management
**Install** uv (if not already installed):
```sh
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Install** dependencies and create virtual environment:
```sh
$ uv sync
```

**Add** new packages:
```sh
$ uv add package_name
```

**Add** development dependencies:
```sh
$ uv add --dev package_name
```

**Use** environment:
uv automatically manages the virtual environment. To run commands in the environment:
```sh
$ uv run python your_script.py
```

Or activate the environment manually:
```sh
$ source .venv/bin/activate
```

**Check the version** of a specific package (e.g. `html5lib`) in the environment:
```sh
$ uv list | grep html5lib
```

**Update** dependencies:
```sh
$ uv sync --upgrade
```

**Remove** a package:
```sh
$ uv remove package_name
```

**Lock** dependencies (creates uv.lock file):
```sh
$ uv lock
```

See the complete documentation on [uv](https://docs.astral.sh/uv/).

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

Activate environment and run quarto:

In preview mode: `uv run quarto preview recommender_systems/assoc_rules/assoc_rules.qmd`

Complete Render: ```uv run quarto render recommender_systems/assoc_rules/assoc_rules.qmd``` produces the revealjs-presentations in html format.


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

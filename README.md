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

### Quarto
[https://quarto.org/docs/download/](https://quarto.org/docs/download/)

Optional: VS Code quarto extension  
If you want to use VS code, which has very convenient editing and preview features 

## presentations in subfolders
global configurations in `_quarto.yml`

Activate Python environment and run quarto:

In preview mode: `preview recommender_systems/assoc_rules/assoc_rules.qmd`

Complete Render: ```quarto render recommender_systems/assoc_rules/assoc_rules.qmd``` produces the revealjs-presentations in html format.


## Pdf conversion
### Decktape
#### Installation
Instructions: https://docs.npmjs.com/downloading-and-installing-node-js-and-npm

1. install nvm: https://github.com/nvm-sh/nvm
    * curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
2. install node: `nvm install node`
3. `npm install -g decktape`

#### Usage
`decktape <input>.html <output>.pdf`

Step through fragments: `decktape generic --key=ArrowRight <input>.html <output>.pdf`

### Alternative: revealjs pdf export

* Open presentation in browser
* Press `E` for export mode
* Open Browser print dialog (cmd+p/ctrl+p) -> print to pdf
* take a screenshot of the title slide
* open screenshot in preview and export as pdf, A4 in landscape mode
* replace the title slide in the presentation export pdf in Preview 
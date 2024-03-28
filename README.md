# Poetry C Extension Example

Example for developing C extension on [Poetry](https://python-poetry.org/)  
This repository show example [spam module (in official document)](https://docs.python.org/ja/3/extending/extending.html) and simple math module.

## Build

1. Clone this repository.
2. If you use VSCode, use _Remote-Containers extension_, and _Reopen in Container_.
3. Otherwise, install [`poetry`](https://python-poetry.org/) by running in a terminal:
```bash
pip install poetry
```

## Installation

1. To install the module in the poetry environment, run:
```bash
poetry install
```
2. If you want to install the module system-wide, you could run:
```bash
poetry build
pip install dist/spam*whl
```

## Test

Run:
```bash
poetry run pytest -s
```

## Usage

Run a Python interpreter:
```bash
poetry run python
```
Then, run the following commands:
```python
from spam.math import add
assert add(3, 2) == 5
```

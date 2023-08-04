![PyPI Downloads](https://img.shields.io/pypi/dm/polylang)
![CI](https://github.com/TheNewThinkTank/polylang/actions/workflows/wf.yml/badge.svg)
[![GitHub repo size](https://img.shields.io/github/repo-size/TheNewThinkTank/polylang?style=flat&logo=github&logoColor=whitesmoke&label=Repo%20Size)](https://github.com/TheNewThinkTank/polylang/archive/refs/heads/main.zip)
# polylang
Multi language learning app

# How to use
After installing the package,<br>
start the main GUI application using one of the following commands:

```Python
python3 app/polylang/src/gui.py -l english
python3 app/polylang/src/gui.py --language english
python3 app/polylang/src/gui.py -l german
python3 app/polylang/src/gui.py --language german
python3 app/polylang/src/gui.py -l spanish
python3 app/polylang/src/gui.py --language spanish
```

or use the following import:

```Python
import polylang
```

<!--
pypi packaging commands:

python3 setup.py bdist_wheel sdist
pip install .
twine check dist/*
twine upload dist/*
-->

![test](https://github.com/argvsucks/argvsucks/workflows/test/badge.svg)
[![codecov](https://codecov.io/gh/argvsucks/argvsucks/branch/main/graph/badge.svg)](https://codecov.io/gh/argvsucks/argvsucks)
<a href="https://pypi.org/project/argvsucks">
<img src="https://img.shields.io/pypi/v/argvsucks.svg?label=release&color=blue&style=flat-square" alt="pypi">
</a>
![Python version](https://img.shields.io/badge/python-3.7+-blue.svg)
[![license: GPL v3](https://img.shields.io/badge/License-MIT-blue.svg)](https://en.wikipedia.org/wiki/MIT_License)

[![API documentation](https://img.shields.io/badge/API-autogenerated-a030a0.svg)](https://argvsucks.github.io/argvsucks)
[![Downloads](https://static.pepy.tech/badge/argvsucks)](https://pepy.tech/project/argvsucks)
![PyPI - Downloads](https://img.shields.io/pypi/dm/argvsucks)

# argvsucks { argv to dict }
[Latest Release](https://pypi.org/project/argvsucks) |
[Current Code](https://github.com/argvsucks/argvsucks) |
[API Documentation](https://argvsucks.github.io/argvsucks)

## Installation
### ...as a standalone lib
```bash
# Set up a virtualenv. 
python3 -m venv venv
source venv/bin/activate

# Install from PyPI...
pip install --upgrade pip
pip install -U argvsucks

# ...or, install from updated source code.
pip install git+https://github.com/argvsucks/argvsucks
```

### ...from source
```bash
git clone https://github.com/argvsucks/argvsucks
cd argvsucks
poetry install
```

## Examples

**Usage**
<details>
<p>

```python3
from argvsucks import handle_command_line

dct = handle_command_line(["program ···", "start", "end=0", "finish", "n=5", "name=Foo", "lst=a,b,c"], n=int, start=False, end=bool, lst=list)
print(dct)
"""
{'start': True, 'end': False, 'finish': True, 'n': 5, 'name': 'Foo', 'lst': ['a', 'b', 'c']}
"""
```


</p>
</details>


### Versioning
While the version scheme has a meaningful calendar component (`minor=yymmdd`), it is still compatible with semantic versioning.
For instance, the version `0.230215.1` means `major=0`, `minor=230215`, `micro/patch=1`. Notes:
 * While `major=0`, some compatibility-breaking changes may occur.
 * From `major=1` onwards, compatibility-breaking changes increment it, and update the minor version to reflect the release date.
 * New (non breaking) features update only the minor version to reflect the release date.
 * Bug fixes (including compatibility-breaking ones) increment only the micro version.

### Contributing
#### Donation
Currently there are no established forms of donation.
Expenses:
  * Programming hours
  * Support
  * Custom features
  * Domain name maintenance yearly costs

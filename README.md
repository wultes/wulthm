# Wulthm

![Downloads from PiPy](https://img.shields.io/pypi/dm/wulthm) ![Version on Pipy](https://img.shields.io/pypi/v/wulthm) ![License by module](https://img.shields.io/github/license/wultes/wulthm)

Π‘ollection of algorithms in Python module π

This module was created to view the work and implementation of popular methods in Python.

π©βπ» The module is development, so over time it will be supplemented with new algorithms π¨βπ»

## π¦ Requirements

- Python 3.7+

## πΎ Install

From **Git**:

- Clone repository in any place convenient for you.
  `git clone https://github.com/wultes/wulthm`

- Go to repository and install by **Python**.

  `cd wulthm & python3 setup.py install`

From **Pip**:

- Install by **pip**:

  `python3 -m pip install wulthm` or  `pip install wulthm`

## π Usage

For example:
```python
from wulthm import wulthm

wulthm.bubble_sort([1, 4, 2, 10, 12])
```

You can run tests by function:
```python
from wulthm import wulthm

wulthm.test_function_with_list(
    function_name="bubble_sort",
  	max_degree=2
)
```

Also, you can see docs and code of function:

```python
from wulthm import wulthm

#Print docs of function
wulthm.get_doc(
    function_name="bubble_sort"
)

#Print code of function
wulthm.get_source_code(
    function_name="bubble_sort"
)
```

For see all function in module:

```python
from wulthm import wulthm

wulthm.get_functions()
```

## π§ Pull requests
If you want to add any new algorithm, then I will be happy to this! π€

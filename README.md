# change_colab_python

Supports installing alternative Python versions in Colab. These versions are not officially supported, but are nice for workshops.

The main part of this code was adapted from a post submitted by [PavelGorbanj](https://github.com/PavelGorbanj) to [Google Colab Issue #2165](https://github.com/googlecolab/colabtools/issues/2165).

## Example:
To install Python 3.11 run the following in Colab:
```
!git clone https://github.com/mcstroh/change_colab_python.git
!bash ./change_colab_python/change_version.sh 3.11
```
Restart the runtime under **Runtime** -> **Restart runtime**.

You can check the current version of Python by typing the following:
```
import sys
print(sys.version)
```

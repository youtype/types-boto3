# types-boto3

[![PyPI - types-boto3](https://img.shields.io/pypi/v/types-boto3.svg?color=blue&label=types-boto3)](https://pypi.org/project/types-boto3)
[![PyPI - boto3](https://img.shields.io/pypi/v/boto3.svg?color=blue&label=boto3)](https://pypi.org/project/boto3)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/types-boto3.svg?color=blue)](https://pypi.org/project/types-boto3)
[![PyPI - Downloads](https://static.pepy.tech/badge/types-boto3)](https://pepy.tech/project/types-boto3)

![boto3.typed](https://github.com/youtype/mypy_boto3_builder/raw/main/logo.png)

Type annotations and code completion for [boto3](https://pypi.org/project/boto3/) package.
This package is a part of [mypy_boto3_builder](https://github.com/youtype/mypy_boto3_builder) project.

`types-boto3` is a successor of [boto3-stubs](https://pypi.org/project/types-boto3).

[![Publish types-boto3](https://github.com/youtype/types-boto3/actions/workflows/publish_on_update.yml/badge.svg)](https://github.com/youtype/types-boto3/actions/workflows/publish_on_update.yml)

- [types-boto3](#types-boto3)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Versioning](#versioning)
  - [Support and contributing](#support-and-contributing)

## Installation

```bash
python -m pip install 'types-boto3[essential]'
```

## Migrate from boto3-stubs

1. Replace `boto3-stubs` dependency with `types-boto3`, leave extras as is
1. In your codebase replace `mypy_boto3_<service>` imports with `types_boto3_<service>`

```bash
# before migration
from mypy_boto3_ec2.client import EC2Client

# after migration
from types_boto3_ec2.client import EC2Client
```

## Usage

Use [mypy](https://github.com/python/mypy) or [pyright](https://github.com/microsoft/pyright) for type checking.

## Versioning

`types-boto3` and `types-boto3-lite` versions are the same as related `boto3` version and follows
[PEP 440](https://www.python.org/dev/peps/pep-0440/) format.

## Support and contributing

Please reports any bugs or request new features in
[mypy_boto3_builder](https://github.com/youtype/mypy_boto3_builder/issues) repository.

# YNAB_MonthEnd

[![PyPI - Version](https://img.shields.io/pypi/v/ynab-monthend.svg)](https://pypi.org/project/ynab-monthend)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ynab-monthend.svg)](https://pypi.org/project/ynab-monthend)

Some things are annoying to do ... month ... after month ... after month.

So let the robots deal with it.

This project will [TBD: orchestration] jobs on [TBD: compute] to check at [TBD: define end of month] and perform the following actions:
* Ensure transactions for the new month are coming in
* Ensure there have been transactions from certain payees in the previous month
* Find the transactions from those payees
* Call Todoist API to set a reminder to move [TBD: x%] of the transactions to a configured category

Unfortunately, there are not any APIs that allow for moving money between categories.

-----

## Table of Contents

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install ynab-monthend
```

## License

`ynab-monthend` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

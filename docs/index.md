:::{toctree}
:hidden:
tutorial
contributing
changelog
apidocs/index
references
:::

# C-Therm TCi instrument usage and data process

Process data exported from the C-Therm TCi thermal conductivity analyzer. See below for processing data exported from the instrument, or <project:#tutorial> to learn how to use the instrument.

## Usage

First install Python 3.11 and `pipx`. See the [quick setup guide](#windows-quick-setup) for details on Windows machine setup. The `c_therm_tci.py` script processes the TCi C-Therm instrument's XML data exports into CSV files. For instance, to process the [example data](#example-data) locally, download [`c_therm_tci.py`](../src/c_therm_tci.py), [`data.xml`](../example/data.xml) and [`data.xlsx`](../example/data.xlsx) to your Desktop. Then, right-click on your Desktop, click "Open in Terminal", and run

```Shell
py -3.11 -m pipx run c_therm_tci.py
```

which processes `data.xml` into `data.csv`. Now, open `data.xlsx`, click to enable data connections, then click `Refresh all` in the `Data` ribbon *twice* to refresh the Power Queries and PivotTable. This example data and the Excel workbook illustrates how to process arbitrary data exports from the C-Therm TCi instrument.

## Example data

The example data folder in this repo has `data.xml`, a simplified representation of the shape of data exported from the C-Therm TCi instrument and `data.csv` represents the result of processing with `c_therm_tci.py`.

The `data.xlsx` workbook ingests and post-processes `data.csv`. The `setup` sheet programmatically finds `data.csv` for Power Query, `raw_data` shows CSV data, `grouped_averages` groups and averages results by test run, and `results` further digests the data. `grouped_averages` also allows overriding the "validity" of a test result and to provide a comment about each test.

## Windows quick setup

This is the quickest way to get set up on Windows for running this Python script, and for Python scripts in general. Install [App Installer (`winget`)](https://apps.microsoft.com/detail/9nblggh4nns1). If this fails you may need to go to the Microsoft Store app, click `Library`, then `Get Updates`, then `Update all`, then try installing `winget` again. Also install [Windows Terminal](https://apps.microsoft.com/detail/9mz1snwt0n5d), then open Windows Terminal from the Start menu. Run

```Shell
winget install --id 'Python.Python.3.11' --override '/quiet PrependPath=0'
py -3.11 -m pip install pipx
py -3.11 -m pipx ensurepath
```

which will install Python 3.11 and `pipx`, and configure `pipx`.

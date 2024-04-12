# c_therm_tci

Process data exported from the C-Therm TCi thermal conductivity analyzer.

## Project information

- [Changes](<https://blakeNaccarato.github.io/c-therm-tci/changelog.html>)
- [Docs](<https://blakeNaccarato.github.io/c-therm-tci>)
- [Contributing](<https://blakeNaccarato.github.io/c-therm-tci/contributing.html>)

## Getting started

Open a terminal (e.g. PowerShell on Windows) or VSCode window to a local folder, e.g. your Desktop. Create a Python virtual environment:

```PowerShell
py -m venv .venv
```

Please don't create Python virtual environment folders in Google Drive as they don't play nicely with syncing. Activate that environment. If on Windows using PowerShell:

```PowerShell
.venv/Scripts/Activate.ps1
```

Install our custom data processing script for the C-Therm TCi thermal conductivity analyzer `data.xml` exports:

```PowerShell
python -m 'pip install c_therm_tci @ git+https://github.com/blakeNaccarato/c-therm-tci'
```

In the working directory, have a folder naned `data` with `data.xml` that you exported from the instrument. To process the data, run:

```PowerShell
python -m c_therm_tci
```

The `data` folder will now have a `data.csv` with extracted thermal conductivity measurements (and other data) from the instrument. Copy `data.xlsx` from our Google Drive into the `data` folder, click to enable data connections, click "Refresh all" twice in the Data ribon menu, and it will process your local `data.csv`. Additional tables and a pivot table in the Excel spreadsheet further summarize your data, reporting thermal conductivities per material, project, and sample (or "lot" in the instrument's parlance).

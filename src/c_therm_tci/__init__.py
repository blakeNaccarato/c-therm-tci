"""Process data exported from the C-Therm TCi thermal conductivity analyzer."""

from csv import DictWriter
from pathlib import Path

from parsel import Selector

INPUT = Path("data.xml")
"""Test results data exported from the C-Therm TCi instrument."""

OUTPUT = Path("data.csv")
"""Output file."""

# Shorthand for ID fields used frequently in XPath expressions
MAT_ID = "Material_id"
MATGRP_ID = "Material_Group_id"
POOL_ID = "DataPool_id"
INT_ID = "DataInterval_id"


def main():
    root = Selector(text=INPUT.read_text(encoding="utf-8"), type="xml")
    data = root.xpath("/NewDataSet")
    records: list[dict[str, str]] = []
    for test in data.xpath("UserTest"):
        mat = data.xpath(f"Material[ {MAT_ID} = {cval(test, MAT_ID)} ]")
        mat_grp = data.xpath(f"Material_Group[ {MATGRP_ID} = {cval(mat, MATGRP_ID)} ]")  # pyright: ignore[reportArgumentType]  # parsel 1.8.1  # pyright: 1.354
        test_record = {
            "User": cval(test, "User_nm"),
            "Method": cval(test, "TestMethod_nm"),
            "Project": cval(test, "Product_nm"),
            "Material Group": cval(mat_grp, "Material_Group_nm"),  # pyright: ignore[reportArgumentType]  # parsel 1.8.1  # pyright: 1.354
            "Material": cval(test, "Material_nm"),
            "Lot": cval(test, "Material_Batch_nm"),
        }
        for interv in data.xpath(f"DataInterval[ {POOL_ID} = {cval(test, POOL_ID)} ]"):
            sample = data.xpath(f"DataSample[ {INT_ID} = {cval(interv, INT_ID)} ]")
            records.append(
                test_record
                | {
                    "Time": cval(sample, "Sample_Start_dt"),  # pyright: ignore[reportArgumentType]  # parsel 1.8.1  # pyright: 1.354
                    "Valid": (
                        "true"
                        if all(
                            cval(elem, "Valid_yn").casefold() == "y"  # pyright: ignore[reportArgumentType]  # parsel 1.8.1  # pyright: 1.354
                            for elem in (interv, sample)
                        )
                        else "false"
                    ),
                    "Ambient temperature (°C)": cval(sample, "AmbientTemp_nb"),  # pyright: ignore[reportArgumentType]  # parsel 1.8.1  # pyright: 1.354
                    "Effusivity (W-s^(1/2)/m^2-K)": cval(sample, "Result_nb"),  # pyright: ignore[reportArgumentType]  # parsel 1.8.1  # pyright: 1.354
                    "Thermal conductivity (W/m-k)": cval(sample, "K_Result_nb"),  # pyright: ignore[reportArgumentType]  # parsel 1.8.1  # pyright: 1.354
                }
            )
    with OUTPUT.open("w", encoding="utf-8", newline="") as file:
        writer = DictWriter(file, fieldnames=records[0].keys())
        writer.writeheader()
        writer.writerows(records)


def cval(elem: Selector, child: str) -> str:
    """Value of an element's child."""
    return elem.xpath(f"{child}/text()").get() or ""


if __name__ == "__main__":
    main()
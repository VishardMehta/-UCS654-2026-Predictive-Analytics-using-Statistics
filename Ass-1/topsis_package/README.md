## Topsis-Hitesh-102317248

A Python package implementing the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) for Multi-Criteria Decision Making (MCDM).
This package works as a **Command Line Tool** and generates an output CSV file containing the **TOPSIS Score** and **Rank**.

## Installation

Install the package from PyPI using:

```bash
pip install Topsis-Hitesh-102317248
```

## Quick Start

### Command Syntax

Once installed, you can use the `topsis` command directly from your terminal, following the syntax given below.

```bash
topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>
```

### Parameters

The command accepts exactly 4 parameters:
| Parameter | Format | Example | Description |
|------------|-------------------------|--------------|---------------------------------|
| Input file | Path string | `"data.csv"` | Path to your CSV file |
| Weights | Comma-separated string | `"1,1,1,1,2"` | Weight for each criterion |
| Impacts | Comma-separated string | `"+,+,+,-,+"` | `+` for benefit, `-` for cost |
| Output file| Path string | `"result.csv"` | Where to save results |

### Example Execution

Grab an input csv or excel file strictly adheres to the following structure:

1. The file must have at least 3 columns- Candidate Identifier column followed by min. 2 criteria.
2. The first column must contain the names/IDs of the alternatives.
3. Criteria columns must contain only numeric values.

A sample dataset file (`data.csv`) is shown below:

| Fund Name | P1   | P2   | P3  | P4   | P5    |
| --------- | ---- | ---- | --- | ---- | ----- |
| M1        | 0.94 | 0.88 | 6.5 | 38.8 | 11.78 |
| M2        | 0.69 | 0.48 | 4.4 | 59.8 | 16.34 |
| M3        | 0.62 | 0.38 | 3.8 | 41.3 | 11.53 |
| M4        | 0.63 | 0.40 | 6.1 | 50.5 | 14.41 |
| M5        | 0.78 | 0.61 | 5.2 | 67.8 | 18.60 |
| M6        | 0.61 | 0.37 | 5.6 | 34.6 | 10.30 |
| M7        | 0.69 | 0.48 | 4.8 | 57.8 | 15.94 |
| M8        | 0.75 | 0.56 | 6.1 | 62.4 | 17.45 |

Run the following command through the terminal.

```bash
topsis data.csv "1,1,1,1,2" "+,+,+,-,+" result.csv
```

The output file (`result.csv`) generated will look like this:
| Fund Name | P1 | P2 | P3 | P4 | P5 | Topsis Score | Rank |
| --------- | ---- | ---- | --- | ---- | ----- | ------------ | ---- |
| M1 | 0.94 | 0.88 | 6.5 | 38.8 | 11.78 | 0.4740098823 | 5 |
| M2 | 0.69 | 0.48 | 4.4 | 59.8 | 16.34 | 0.5408838381 | 3 |
| M3 | 0.62 | 0.38 | 3.8 | 41.3 | 11.53 | 0.2680107006 | 7 |
| M4 | 0.63 | 0.4 | 6.1 | 50.5 | 14.41 | 0.3371798261 | 6 |
| M5 | 0.78 | 0.61 | 5.2 | 67.8 | 18.6 | 0.6988032678 | 1 |
| M6 | 0.61 | 0.37 | 5.6 | 34.6 | 10.3 | 0.0900806607 | 8 |
| M7 | 0.69 | 0.48 | 4.8 | 57.8 | 15.94 | 0.5089134079 | 4 |
| M8 | 0.75 | 0.56 | 6.1 | 62.4 | 17.45 | 0.5955525554 | 2 |

Sample input file is available in the `sample_data/` folder.
Sample output file is available in the `results/` folder.

## Important Notes

- The command accepts exactly four parameters.
- Number of weights and impacts must match number of criteria columns.
- Impacts must be only `+` or `-`.
- Make sure the criteria columns must be numeric as mentioned earlier.
- No cell should be empty.

## License

This project is licensed under the **MIT License**. See [LICENSE](https://opensource.org/license/MIT) for more information.

## Author

Hitesh Yadav<br>
Penultimate-Year Student, BE-CSE<br>
Thapar Institute of Engineering and Technology, Patiala

#### Let's Connect: **<a href="https://github.com/HiteshhYadav"> GitHub | <a href="https://www.linkedin.com/in/hitesh-yadav-61a18125a/?profileId=ACoAAD-9vjYB1kJAb307oQZ9xhmEW4ck2wDomDM"> LinkedIn | [Email](mailto:hyadav1_be23@thapar.edu)**

<br>

_If you find this package useful, please ⭐ star it on GitHub!_

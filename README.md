# Social Network Graph Analysis

This repository contains Python code for preprocessing and transforming social-network interaction data into graph-based analytical datasets.

The project is shared as a **code-focused portfolio sample**. The broader research context, thesis document, and unpublished findings are intentionally not included.

## What the Code Does

The workflow works with multiple types of network relationships, including:

- retweet interactions
- mention interactions
- reply interactions
- follower relationships

The scripts filter network data to a manageable node range and then use graph representations to combine interaction information into a structured output dataset.

## Repository Structure

```text
Social-Network-Graph-Analysis/
├── filter_network_data.py
├── build_network_dataset.py
├── README.md
└── .gitignore
```

### `filter_network_data.py`

Filters the original network edge-list files to retain interactions where both node IDs fall within a selected range.

Expected source files:

- `higgsRT.txt`
- `higgsRP.txt`
- `higgsMT.txt`
- `higgsFL.txt`

It creates filtered files:

- `higgs_RT.txt`
- `higgs_RP.txt`
- `higgs_MT.txt`
- `higgs_FL.txt`

### `build_network_dataset.py`

Loads the filtered edge lists as directed NetworkX graphs, gathers nodes appearing across the interaction networks, combines relationship information, calculates follower counts, and exports the resulting table as a compressed CSV.

## Technologies

- Python
- Pandas
- NetworkX
- NumPy

## Data

Raw and generated data files are intentionally excluded from this repository. The scripts expect compatible edge-list files to be placed locally before execution.

## Portfolio Note

This repository demonstrates data preprocessing, graph construction, network-data transformation, and tabular feature generation. It does not reproduce the complete thesis or disclose the full research analysis.

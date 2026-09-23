"""Filter social-network edge lists to a selected node-ID range.

This script preserves the original project logic while giving the workflow a
clearer portfolio-friendly structure.
"""

import re

MAX_NODE_ID = 5000


def filter_interaction_file(source_path, output_path, has_weight=True):
    """Keep rows where both endpoint node IDs are below MAX_NODE_ID."""
    filtered_lines = []

    with open(source_path, "r", encoding="utf-8") as source_file:
        for line in source_file:
            values = re.findall(r"\d+", line.strip())
            if len(values) < 2:
                continue

            source_node = int(values[0])
            target_node = int(values[1])

            if has_weight and len(values) >= 3:
                _weight = int(values[2])

            if source_node < MAX_NODE_ID and target_node < MAX_NODE_ID:
                filtered_lines.append(line)

    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.writelines(filtered_lines)


def main():
    filter_interaction_file("higgsRT.txt", "higgs_RT.txt")
    filter_interaction_file("higgsRP.txt", "higgs_RP.txt")
    filter_interaction_file("higgsMT.txt", "higgs_MT.txt")
    filter_interaction_file("higgsFL.txt", "higgs_FL.txt", has_weight=False)


if __name__ == "__main__":
    main()

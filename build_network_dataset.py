"""Build a combined tabular dataset from multiple social-network graphs.

The script loads filtered retweet, mention, reply, and follower edge lists,
combines interaction information for all observed nodes, derives follower
counts, and exports the result as a compressed CSV.
"""

import networkx as nx
import pandas as pd


def adjacency_frame(graph):
    """Return a pandas adjacency matrix for a NetworkX graph."""
    return pd.DataFrame(nx.to_pandas_adjacency(graph))


def add_interaction_columns(output_df, graph, prefix):
    """Populate prefixed interaction columns from a graph adjacency matrix."""
    adjacency = adjacency_frame(graph)

    for node_i in graph.nodes():
        row_index = output_df.loc[output_df["Node"] == str(node_i)].index[0]

        for node_j in graph.nodes():
            value = int(adjacency.loc[str(node_i), str(node_j)])
            output_df.at[row_index, f"{prefix}{node_j}"] = "" if value == 0 else value


def main():
    retweet_graph = nx.read_weighted_edgelist(
        "higgs_RT.txt", create_using=nx.DiGraph()
    )
    mention_graph = nx.read_weighted_edgelist(
        "higgs_MT.txt", create_using=nx.DiGraph()
    )
    reply_graph = nx.read_weighted_edgelist(
        "higgs_RP.txt", create_using=nx.DiGraph()
    )
    follower_graph = nx.read_weighted_edgelist(
        "higgs_FL.txt", create_using=nx.DiGraph()
    )

    all_nodes = set(retweet_graph.nodes())
    all_nodes.update(mention_graph.nodes())
    all_nodes.update(reply_graph.nodes())
    all_nodes = sorted(all_nodes)

    columns = ["Node", "Follower"]
    for node in all_nodes:
        columns.extend([f"RT{node}", f"RP{node}", f"MT{node}"])

    output_df = pd.DataFrame({"Node": all_nodes}, columns=columns)

    add_interaction_columns(output_df, retweet_graph, "RT")
    add_interaction_columns(output_df, mention_graph, "MT")
    add_interaction_columns(output_df, reply_graph, "RP")

    follower_adjacency = adjacency_frame(follower_graph)
    for node in all_nodes:
        row_index = output_df.loc[output_df["Node"] == str(node)].index[0]
        if node in follower_adjacency.columns:
            output_df.at[row_index, "Follower"] = follower_adjacency[node].sum()
        else:
            output_df.at[row_index, "Follower"] = 0

    compression_options = {
        "method": "zip",
        "archive_name": "out.csv",
    }
    output_df.to_csv(
        "out.zip",
        index=False,
        compression=compression_options,
    )


if __name__ == "__main__":
    main()

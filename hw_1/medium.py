import ast
import inspect
import astunparse
from easy import fibonacci
import networkx as nx
import matplotlib.pyplot as plt

# Convert code my function in text
code_function = inspect.getsource(fibonacci)

# Parse code in graph(Model)
tree = ast.parse(code_function)

# # Print the AST
print(ast.dump(tree, indent=4))
# print(astunparse.dump(tree))


# Create an empty graph object
# graph = nx.Graph()
#
# # Traverse the AST and add nodes and edges to the graph
# for node in ast.walk(tree):
#     if isinstance(node, ast.FunctionDef):
#         graph.add_node(node.name)
#     elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
#         graph.add_edge(node.func, node.args[0])
#
# # Visualize the graph
# nx.draw(graph, with_labels=True)
# plt.show()

def create_ast_graph(func):
    """Create AST graph of a function"""
    # Parse the function source code into an AST
    tree = ast.parse(inspect.getsource(func))
    # Create a new graph
    graph = nx.DiGraph()
    # Traverse the AST and add nodes and edges to the graph
    traverse_ast(tree, graph)
    return graph

def traverse_ast(node, graph, parent=None):
    """Traverse the AST and add nodes and edges to the graph"""
    # Add the node to the graph
    graph.add_node(node)
    # Add an edge from the parent to the node
    if parent is not None:
        graph.add_edge(parent, node)
    # Traverse the children of the node
    for child in ast.iter_child_nodes(node):
        traverse_ast(child, graph, node)


def fibonacci(quantity):
    seq = [1, 1]
    if quantity < 2:
        return seq[:quantity]

    for _ in range(quantity - 2):
        new_el = seq[-1] + seq[-2]
        seq.append(new_el)

    return seq

# Create the AST graph of the function
graph = create_ast_graph(fibonacci)

# Visualize the AST graph
pos = nx.spring_layout(graph, seed=42)
nx.draw_networkx(graph, pos, with_labels=False)
plt.show()
import os, subprocess

from rdflib import Graph
from pyshacl import validate

shape_paths = list()
example_graph_paths = dict()

labels = ["node", "property"]
for label in labels:
    directory = f"../shapes/{label}-shapes"
    for node_shape in os.listdir(directory):
        node_shape_path = os.path.join(directory, node_shape)
        shape_paths += [node_shape_path]
        filename = node_shape.replace("Constraint", "-ExampleGraph")
        example_graph_path = os.path.join("./example-graphs", filename)
        example_graph_paths[node_shape_path] = example_graph_path

for shape_path in shape_paths:
    if shape_path != "../shapes/node-shapes/ObservationConstraint.ttl":
        continue

    # Load the data to validate
    shape = Graph()
    shape.parse(shape_path, format="ttl")

    # Get the shape to test
    example_graph = Graph()
    example_graph_path = example_graph_paths[shape_path]
    example_graph.parse(example_graph_path, format='ttl')

    # Validate
    r = validate(
        data_graph=example_graph,
        shacl_graph=shape,
        abort_on_first=False,
        allow_warnings=False,
        meta_shacl=True,
        advanced=False,
        js=False,
        inference='rdfs',
        serialize_report_graph=True)
    conforms, results_graph, results_text = r

    shape_name = shape_path.split("/")[-1]
    print (f"Processing: {shape_name}!")
    print (f"Result Text: {results_text}")
    print (("#"*130 +"\n")*2)
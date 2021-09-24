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
            example_graph_path = os.path.join("./example_graphs", filename)
            example_graph_paths[node_shape_path] = example_graph_path

for shape_path in shape_paths:
      if shape_path != "../shapes/property-shapes/observedPropertyConstraint.ttl":
            continue

      # Load the data to validate
      shape = Graph()
      shape.parse(shape_path, format="ttl")

      # Get the shape to test
      example_graph = Graph()
      example_graph.parse('test_example.ttl', format='ttl')

      # Validate
      r = validate(data_graph = example_graph,
            shacl_graph=  shape,
            abort_on_first=False,
            allow_warnings=False,
            meta_shacl=False,
            advanced=False,
            js=False,
            debug=False)
      conforms, results_graph, results_text = r

      print (conforms)
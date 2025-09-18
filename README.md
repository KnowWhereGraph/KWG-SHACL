# KWG-SHACL

This is the repository of SHACL shapes development/research for KWG. 

* The [SHACL Standard](https://www.w3.org/TR/vocab-ssn/)
* The combined file is [shacl_sosa.ttl](./shacl-sosa.ttl)
* An example is [sosa:Observation](./shapes/node-shapes/ObservationConstraint.ttl)
* [Task Assignment](https://docs.google.com/spreadsheets/d/1-U-1QQjv7cG-_aEzhlqcahGDOvi3PsKjP5k-2OFVm1g/edit#gid=0)

## Example usage in pySHACL 

You can try the shacl validation on your knowledge graph using for example [pySHACL](https://pypi.org/project/pyshacl/).

```bash
pip install pyshacl
pyshacl -s https://github.com/KnowWhereGraph/KWG-SHACL/raw/refs/heads/main/shacl_sosa.ttl -m -i rdfs -a -f human data.ttl
```

Read more about pySHACL in [pypi](https://pypi.org/project/pyshacl/), short about the options used above:

```bash
-s is the path to the shapes graph to use
-m enable the meta-shacl feature
-i is the pre-inferencing option
-a enable SHACL Advanced Features
-f is the ValidationReport output format (human = human-readable validation report)
```

pySHACL returns a report to stdout with the validation result.
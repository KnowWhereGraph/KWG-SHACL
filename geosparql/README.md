# GeoSPARQL Shapes

SHACL for data with GeoSPARQL relations

## Overview

The OGC provides shapes for third parties who choose to model their data with GeoSPARQL. GraphDB 10.2.x currently doesn't support all the shapes present. There's also regex that isn't supported by the regex parser that GraphDB uses, so these shapes shouldn't be inserted into GraphDB

The suggested use for these shapes is to validate _outside_ of GraphDB, using [pySHACL](https://github.com/RDFLib/pySHACL).

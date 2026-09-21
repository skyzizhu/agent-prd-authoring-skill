# Data / Analytics Agent Product Rules

## Required modules

- user question / metric definition
- data source and schema discovery
- permission and sensitivity check
- query/analysis plan
- read/write classification
- query/code execution
- result validation
- arithmetic/aggregation sanity check
- visualization/report generation
- export/action approval when sensitive
- final answer with reproducibility metadata

## Product rules

### Grounding
The agent must inspect actual schema/metadata before referencing fields or tables that are not already confirmed.

### Read vs write
Treat data mutation separately from analysis.
Default:
- read-only queries can execute within authorized scope
- writes/updates/deletes require explicit approval unless the product is explicitly designed for autonomous mutation

### Validation
Before final answer:
- verify row counts/units/time ranges when material
- check null/duplicate effects when relevant
- sanity-check aggregates against source totals when available
- do not silently mix incompatible date grains or currencies

### Sensitive data
Define:
- which data classes are restricted
- what may be shown in final output
- what may be exported
- when aggregation/redaction is required

### Failure handling
Query failures should distinguish:
- syntax/schema mismatch
- permission/auth
- timeout/resource limit
- empty result
- data quality issue

Do not treat an empty result as a system error unless expected data should exist.

## Evaluation
Use correctness, reproducibility, sensitive-data safety, write-safety, and material arithmetic-error rate.

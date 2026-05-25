# Benchmark coverage map

The main resource table is stored at [`../resources/benchmark_coverage.csv`](../resources/benchmark_coverage.csv).

## Columns

| Column | Meaning |
|---|---|
| P/C | prompt and compositional faithfulness |
| S/E | structural control and edit preservation |
| ID | subject/identity persistence |
| V/T | multi-view, temporal, or narrative coherence |
| N/S | preference, safety, or value alignment |
| P/W | physical, causal, or world-grounded plausibility |

Values:

- `H`: direct evaluation with dedicated tasks, annotations, or metrics
- `M`: partial support or adaptable evidence
- `L`: only indirect relevance

The ratings describe relevance to each consistency claim rather than overall dataset quality.

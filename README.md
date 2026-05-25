# Awesome Consistency in Diffusion-Based Visual Generation

This repository accompanies the survey:

**Consistency in Diffusion-Based Visual Generation: A Survey**

The goal is to organize papers, benchmarks, datasets, evaluators, and diagnostic protocols around **consistency relations** rather than only task names.

## Consistency taxonomy

| Relation | Agreement target | Typical failures |
|---|---|---|
| External consistency | Agreement with user- or task-provided conditions | prompt omission, attribute misbinding, relation/counting error, control mismatch, over-editing |
| Internal consistency | Agreement among generated parts, instances, views, frames, or story states | identity drift, cross-view disagreement, flicker, narrative/state forgetting |
| Normative consistency | Agreement with evaluative criteria | low preference, unsafe content, physical implausibility, causal/world-state violations |

## Repository contents

```text
docs/
  taxonomy.md              # concise taxonomy description
  benchmark_coverage.md    # explanation of the resource table
  related_surveys.md       # related survey categories
  contribution_guide.md    # how to contribute resources
resources/
  benchmark_coverage.csv   # benchmark/dataset/evaluator coverage map
  related_surveys.csv      # related survey positioning
  taxonomy_methods.csv     # method taxonomy map
  selected_bibtex.bib      # selected BibTeX entries
scripts/
  check_resource_table.py  # CSV consistency checker
paper/
  README.md                # where to place paper source/PDF
```

## Coverage labels

The benchmark table uses six diagnostic dimensions.

| Label | Meaning |
|---|---|
| P/C | prompt and compositional faithfulness |
| S/E | structural control and edit preservation |
| ID | subject/identity persistence |
| V/T | multi-view, temporal, or narrative coherence |
| N/S | preference, safety, or value alignment |
| P/W | physical, causal, or world-grounded plausibility |

Coverage scores: `H` = direct/dedicated coverage, `M` = partial/adaptable coverage, `L` = indirect/low coverage.

## Citation

If this survey or resource list is useful, please cite:

```bibtex
@misc{consistency_diffusion_survey,
  title  = {Consistency in Diffusion-Based Visual Generation: A Survey},
  author = {Yan, Song and Zhai, Wei and Li, Ruixuan and Yang, Zhangping and Wang, Chenfeng and Cai, Yancheng and Zhang, Tao and Wang, Ling and Lan, Yunwei and He, Yujie and Li, Min and Zha, Zheng-Jun},
  year   = {2026},
  note   = {Manuscript}
}
```

## Contributions

Issues and pull requests are welcome. Please include a BibTeX key, official project/code link when available, resource type, modality, primary consistency relation, and one-sentence diagnostic use/blind spot.

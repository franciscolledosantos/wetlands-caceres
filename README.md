# wetlands-caceres

Code and result tables for the manuscript *From bench to field: constructed wetlands at three experimental scales for domestic sewage treatment on the edge of the Brazilian Pantanal* (submitted to *RBRH – Revista Brasileira de Recursos Hídricos*, 2026).

Three consecutive experimental scales built for the same wastewater treatment plant in Cáceres (Mato Grosso), on the edge of the Pantanal, are compared: bench units with synthetic sewage and *Cyperus alternifolius*, bench units with raw sewage and *Heliconia psittacorum*, and a 5.8 m² horizontal subsurface-flow pilot monitored in February–April 2025 during start-up. Bench efficiencies (70–72% COD, 88–89% total P, 90–94% suspended solids) were not reproduced by the pilot, which operated at about 19 times its design flow; a first-order sensitivity analysis of the design equation to flow explains the loss of removal.

## Layout

| Folder | Content |
|---|---|
| `scripts/` | Sensitivity of the first-order design equation to flow, the two result figures and the manuscript builder |
| `resultados/` | Sensitivity table of Eq. 1 to flow (HLR, nominal HRT, expected BOD removal, organic load) |
| `figuras/` | Figures 3 and 4 of the manuscript (removal efficiencies by scale; inlet–outlet parameters of the pilot) |

## Pipeline

1. `scripts/sensibilidade_eq1_vazao.py` — first-order plug-flow design equation (K = 0.36 d⁻¹, built geometry 3.4 × 1.7 × 0.60 m, porosity 0.35) evaluated from 0.25 to 9.59 m³ d⁻¹ → `resultados/sensibilidade_eq1_vazao.csv` (Supplementary Material).
2. `scripts/figs.py` — Figures 3 and 4 from the summary statistics reported in the manuscript (values embedded in the script).
3. `scripts/build_docx.py <manuscript.md> <out.docx>` — manuscript in the journal format (source not included).

Run the scripts from any working directory: every path is resolved relative to the script's own location (`os.path.dirname(__file__)`).

## Data

Monitoring data of the bench units and of the pilot (six sampling dates, duplicate inlet–outlet samples, weekly flow measurements) belong to the master's dissertation of T. C. C. Hurtado (ProfÁgua/UNEMAT, 2025) and will be deposited in SciELO Data by the authors; the spreadsheet is **not** included here. The scripts use only the summary statistics published in the manuscript.

Raw input files are **not** redistributed in this repository; they are large and/or belong to third parties. Download them from the sources above and place them as described, or start from the derived tables in `resultados/`.

## Citation

See `CITATION.cff` (co-authors to be added). Licence: MIT.

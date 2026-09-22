# Human verification for the Stata case

- [ ] `isid unit_id year` passes: each unit-year is unique.
- [ ] `count` returns 20.
- [ ] Years run from 2022 through 2025 and there are five units.
- [ ] `treatment=1` occurs only for units 4 and 5 in 2024–2025.
- [ ] No missing observations were silently removed.
- [ ] `output/analysis.log` was opened and preserved.
- [ ] The regression includes `size` and year indicators.
- [ ] Five clusters are insufficient for reliable clustered inference.
- [ ] Association or a coefficient was not automatically described as a real causal effect.
- [ ] Any prose or slides clearly say “synthetic data, teaching demonstration.”

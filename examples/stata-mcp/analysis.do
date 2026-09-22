version 18
clear all
set more off

capture log close
capture mkdir "output"
log using "output/analysis.log", replace text

import delimited using "synthetic_panel.csv", clear

describe
isid unit_id year
count
assert r(N) == 20
assert inrange(year, 2022, 2025)
assert inlist(treatment, 0, 1)

misstable summarize
summarize outcome treatment size
tabulate year treatment

xtset unit_id year
regress outcome treatment size i.year, vce(cluster unit_id)
estimates store illustrative_model

display as text "Illustration only: five clusters are insufficient for reliable inference."
log close

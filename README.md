# EEG evidence for acoustic cue weights in speech perception

Analysis code for an EEG study of how a primary acoustic cue (voice onset time,
VOT) and a secondary cue (fundamental frequency, f0) contribute to neural
responses during phonological categorization. Thirty native English speakers
completed an auditory oddball task with stimuli varying in VOT and f0 while EEG
was recorded.

All analyses live in a single notebook, **`AcousticCuesEEG_github.ipynb`**, and
reproduce the behavioral results, ERP amplitude analyses, time-resolved
decoding, and cue-weight comparisons reported in the manuscript.

## Repository structure

```
AcousticCuesEEG_github.ipynb   # all analyses (run top to bottom)
behavior/                      # per-participant behavioral CSVs (*_ob.csv)
epochs/                        # preprocessed, epoched EEG (*-epo.fif) — download from OSF 
logs/                          # preprocessing logs (used for bad-channel counts)
decoding/                      # decoding outputs (per-participant *.p caches + .png)
figures/                       # manuscript figures written here
```

The notebook reads the epoched EEG from `epochs/`, the behavioral responses from
`behavior/`, and the preprocessing logs from `logs/`, and writes figures to
`figures/` and decoding results to `decoding/`. Reference stimulus information is
embedded directly in the notebook, so no external reference file is required.

Because the EEG epoch files are large, they are **not** stored in this
repository. Download them from OSF and place them in an
`epochs/` folder at the repository root before running the notebook.

## Requirements

The notebook is written for **Python 3.10+** and depends on:

```
numpy
pandas
matplotlib
scipy
scikit-learn
statsmodels
mne
pingouin
tqdm
pymer4
```

**Important:** the behavioral analysis uses a generalized linear mixed-effects
model fit through `pymer4`, which calls R's `lme4` package under the hood. You
must therefore also have **R installed** with the `lme4` package available.
If you do not need the behavioral GLMM, the rest of the notebook (ERP
amplitude, decoding, and cue-weight analyses) runs without R.

## Data availability

The EEG epoch files are too large for GitHub and are openly available on OSF.

Download the epoch files from the OSF record above and place them in an
`epochs/` folder at the repository root to reproduce the analyses.

## Project DOI
10.17605/OSF.IO/JF3B6



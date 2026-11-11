# EEG evidence for acoustic cue weights in speech perception

Data, experimental materials, and analysis code for:

> [Authors masked for review]. *EEG evidence for acoustic cue weights in speech perception.* Manuscript submitted to *Journal of Experimental Psychology: General*.

Thirty English-speaking adults completed an auditory oddball task with *beach–peach* and *dear–tear* stimuli that varied in voice onset time (VOT; 5 steps) and onset f0 (3 steps) while 32-channel EEG was recorded. The analyses ask how a primary cue (VOT) and a secondary cue (f0) shape P3 amplitude, decoding time course, and responses to cue combinations.

- **OSF project (data, materials, code):** [masked for review]
- **GitHub (code and small files):** [masked for review]

The EEG epoch files are too large for GitHub and are stored only on OSF. Everything else is in both places. OSF mirrors the GitHub repository through its GitHub add-on.

---

## Quick start

1. **Get the files.** Clone this repository, or download it from the OSF *GitHub* tab.
2. **Add the EEG data.** Download the 40 files in `epochs/` from OSF Storage. Put them in an `epochs/` folder at the repository root.
3. **Create the environment.** This installs Python, R, `lme4`, and every package at the version used for the paper:
   ```bash
   conda env create -f environment.yml
   conda activate acousticcueseeg
   ```
   For a pip-only setup, use `pip install -r requirements.txt`. You then need to install R and the R package `lme4` yourself, at the versions listed at the top of that file.
4. **Run the analyses.** Open `AcousticCuesEEG_github.ipynb` and run all cells from top to bottom (*Kernel → Restart & Run All*). Figures are written to `figures/` and decoding results to `decoding/`.

**Run time:** the per-participant decoding takes the longest. The `decoding/*.p` files hold the saved results, so the notebook skips that step for any participant whose file already exists. To recompute decoding from scratch, delete those files first.

---

## Where each result is produced

| Paper | Notebook section | Output file(s) in `figures/` |
|---|---|---|
| Table 1, Figure 1 | Analysis 0: Behavioral data | `behavior_tile.png` |
| Table 2, Figure 2 | Analysis 1: Amplitude differences | `VOT_steps_comparison.png`, `F0_steps_comparison.png` |
| Figure 3 | Analysis 2: Time-course differences | `VOT_decoding_oleson.png`, `F0_decoding_oleson.png` |
| Table 3, Figure 4 (right) | Analysis 3: Acoustic cue weights | `cue_weights_anova.png` |
| Figure 4 (left) | Schematic drawn by hand; not produced by code | – |
| Supplement S5, Figure S1 | S5: Categorization function | `behavior_categorization_prop.png` |
| Supplement S6, Table S1, Figure S2 | S6: P3 amplitude, on-target responses only | `VOT_steps_nresponses.png`, `f0_steps_nresponses.png` |
| Supplement S7, Table S2, Figure S3 | S7: Effects within cue levels | `vot_atf0.png, f0_atvot.png` |
| Supplement S8, Figures S4–S5 | S8: Individual differences | `supp_behavior_distributions.png`, `supp_p3_behavior_scatter.png` |

---

## Repository contents

```
AcousticCuesEEG_github.ipynb   all analyses, in manuscript order
environment.yml                conda environment (Python + R + lme4, exact versions)
requirements.txt               the same Python packages for pip
LICENSE                        license for the code (data/materials: see License below)
behavior/                      oddball responses, one CSV per participant   (GitHub + OSF)
epochs/                        preprocessed EEG epochs, one .fif per participant (OSF only)
logs/                          preprocessing logs: final bad-channel list per participant
decoding/                      saved per-participant decoding results (*.p)
figures/                       figures written by the notebook
materials/
  AcousticCueExperiment_Oddball_eeg.py   PsychoPy experiment script (PsychoPy 2022.2.4)
  LanguageQuestionnaire.pdf              participant language-background questionnaire
  stimuli/BP/, stimuli/DT/               stimulus .wav files (see naming below)
preprocessing/
  individual_preproc.ipynb      raw BioSemi .bdf -> epochs/ and logs/ (run once per participant)
  experiment_params.py          channel names, filter settings, raw-data path
  functions.py                  trigger clean-up helper (filter_short_bursts)
```

The raw continuous EEG recordings (`.bdf`) are not shared. The preprocessing notebook documents every step from the raw recordings to the shared epochs. To re-run it, you would need the raw files in a `raw/` folder at the repository root.

---

## Participants

Data from 40 participants who completed the EEG session are shared (IDs 105–147). Of the 43 participants recruited, 3 did not complete the EEG portion. Their data are not included, and their IDs do not appear in any folder.

The exclusion cell in the notebook applies the two criteria from the manuscript and prints the reason for each excluded participant:

- **Behavioral accuracy:** below 50% "target" responses to the prototypical tokens.
- **Too many bad channels:** more than 3 (10%) EEG channels dropped.

| Status | IDs |
|---|---|
| Excluded: accuracy | 108, 117, 119, 121, 133 |
| Excluded: bad channels | 109, 114, 115, 138, 144 |
| Included in all analyses (*n* = 30) | 105, 106, 107, 110, 111, 112, 113, 116, 120, 123, 124, 125, 127, 128, 129, 130, 131, 132, 134, 135, 136, 137, 139, 140, 141, 142, 143, 145, 146, 147 |

Excluded participants' files are shared so the exclusions can be checked.

---

## Data dictionary

### `behavior/<ID>_ob.csv` (PsychoPy output, one row per trial)

| Column | Meaning |
|---|---|
| `participant` | Participant ID |
| `target` | Target word for the block: `beach`, `peach`, `dear`, `tear` |
| `audio_clip` | Stimulus file played (see stimulus naming below) |
| `oddball_response.keys` | Key pressed: `n` = matches the target, `m` = does not match; empty = no response (timed out after 4000 ms) |
| `oddball_response.rt` | Response time (s) |
| `trialBlock.*`, `trialOddball.*`, `trialBreak.*` | PsychoPy loop counters |
| `psychopyVersion`, `frameRate`, `expName`, `session` | Session information recorded by PsychoPy |

The session date and time recorded by PsychoPy have been removed to protect participant privacy.

### `epochs/<ID>-epo.fif` (MNE-Python epochs)

- **Time window:** −100 to 800 ms around stimulus onset.
- **Sampling rate:** 2048 Hz (not downsampled; the decoding analysis resamples to 1000 Hz).
- **Channels:** 30 scalp EEG channels from a 32-channel BioSemi cap (10–20 positions), re-referenced to the average of the two mastoids. Fp1 and Fp2 were used as EOG channels for ICA and are not included.
- **Preprocessing:** 0.1–40 Hz zero-phase Butterworth filter; bad channels interpolated (spherical spline); ICA for ocular artifacts; spurious trigger pulses removed; baseline-corrected to −100–0 ms; epochs with peak-to-peak amplitude > 150 µV on any channel rejected. Details are in Supplement S3 and `preprocessing/`.
- **Trial information:** each epoch carries a row of metadata (`epochs.metadata`).

| Metadata column | Meaning |
|---|---|
| `target` | Target word of the block |
| `Continuum` | Continuum of the stimulus played: `beach - peach` or `dear - tear` |
| `task-relevant` | `yes` if the stimulus is on the target's continuum, `no` otherwise |
| `VOT` | VOT step of the stimulus, 1–5 (1 = 0 ms, most voiced; 5 = 40 ms, most voiceless) |
| `F0` | f0 step of the stimulus: 1, 3, 5 (= 250, 270, 290 Hz) |
| `vot-stepsfromtarget` | VOT distance from the target, coded 1–5 (1 = target); the notebook recodes this to 0–4 |
| `f0-stepsfromtarget` | f0 distance from the target, coded 1/3/5 (1 = target); the notebook recodes this to 0–2 |
| `VOT_step`, `F0_step` | Distance from the continuum midpoint, used for the Analysis 3 cue configurations. VOT_step: 0 = VOT step 3, 1 = steps 2/4, 2 = endpoints 1/5. F0_step: 0 = 270 Hz, 1 = 250 or 290 Hz. |
| `oddball_response.keys` | `n` = target response, `m` = non-target response |
| *(other columns)* | Stop and Step are constant (yes / na) and left over from the stimulus reference file; they are not used. The other columns are PsychoPy loop counters and response timings. |

### `logs/<ID>.log`

One line per participant, written during preprocessing: the final list of bad channels, which were interpolated. The analysis notebook counts these channels to apply the bad-channel exclusion criterion (more than 3).

### Stimulus naming (`materials/stimuli/`)

- `bpV_F.wav` and `dtV_F.wav`: *beach–peach* and *dear–tear* stimuli. **V** is the VOT step (1–5); **F** is the f0 step (1–5).
- Only f0 steps 1, 3 and 5 (250, 270, 290 Hz) were used in the experiment.

---

## Software

Analyses were run in Python 3.14.2 with:
- MNE-Python, scikit-learn, statsmodels, pingouin, NumPy, SciPy, pandas, matplotlib;
- pymer4, which calls R 4.5.2 and `lme4` 2.0.1 for the behavioral GLMM.

Exact versions are listed in `environment.yml` and `requirements.txt`, and are printed by the *Session info* cell near the top of the notebook. Stimuli were created in Praat 6.2.22 and presented with PsychoPy 2022.2.4.

---

## How to cite

Please cite the article (reference to be added on publication) and the data set:

> [Authors]. (2026). *EEG evidence for acoustic cue weights in speech perception: Data, materials, and analysis code* [Data set]. OSF. [masked for review]

## License

- **Code:** [MIT License](LICENSE).
- **Data and materials:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Contact

[Masked for review]

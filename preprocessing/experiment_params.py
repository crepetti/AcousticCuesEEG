"""Preprocessing settings used by individual_preproc.ipynb."""

params = dict(
    # Raw BioSemi .bdf files, relative to this folder. The raw files are not shared;
    # the preprocessed epochs are on OSF.
    data_dir="../raw",

    # Band-pass filter: MNE builds a Butterworth band-pass from order=1 per edge and
    # applies it forward and backward (zero phase), giving an effective order of 4.
    l_freq=0.1,
    h_freq=40,
    iir_params=dict(order=1, ftype="butter"),

    # BioSemi electrode labels -> 10-20 names
    rename_dict={
        'A1': 'Fp1', 'A2': 'Fp2',
        'A3': 'F3', 'A4': 'F4', 'A5': 'F7', 'A6': 'F8',
        'A7': 'Fz', 'A8': 'C3', 'A9': 'C4', 'A10': 'Cz',
        'A11': 'P3', 'A12': 'P4', 'A13': 'Pz', 'A14': 'O1',
        'A15': 'O2', 'A16': 'T7', 'A17': 'T8', 'A18': 'P7',
        'A19': 'P8', 'A20': 'AF3', 'A21': 'AF4', 'A22': 'FC1',
        'A23': 'FC2', 'A24': 'CP1', 'A25': 'CP2', 'A26': 'PO3',
        'A27': 'PO4', 'A28': 'Oz', 'A29': 'FC5', 'A30': 'FC6',
        'A31': 'CP5', 'A32': 'CP6',
    },

    parietal_channels=['Pz', 'P3', 'P4'],

    # Unused external and auxiliary channels (EXG1/EXG2 = mastoids are kept for referencing)
    drop_channels=['EXG3', 'EXG4', 'EXG5', 'EXG6', 'EXG7', 'EXG8',
                   'GSR1', 'GSR2', 'Erg1', 'Erg2', 'Resp', 'Plet', 'Temp'],
)

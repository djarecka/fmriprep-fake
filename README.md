Repository with Dockerfile for creating a Docker with "fake" fmriprep:
`docker build  -t fmriprep_fake .`

The image takes three positional arguments: `bids_dir`, `output_dir` and `analysis_level` (that has to be 'participant').

It also takes two optional named arguments: `--participant-label` (e.g. 'sub-111') 
and `--bids-filter-file`. `bids-filter-file` is used to extract sessions if available 
under "bold" item (e.g. `{"bold": {"datatype": "func", "suffix": "bold", "session": "baseline"}}`).

### Example of usage and output

#### when run without sessions (without bids-filter-file)
`docker run --rm -v <local_path_for_output>:/out_tmp 
fake_fmriprep_image inp /out_tmp participant --participant-label=sub-1`

```bash
out_tmp/ 
├── dataset_description.json
├── desc-aparcaseg_dseg.tsv
├── desc-aseg_dseg.tsv
├── logs
│   ├── CITATION.bib
│   ├── CITATION.html
│   ├── CITATION.md
│   └── CITATION.tex
├── sourcedata
│   └── freesurfer
│       ├── fsaverage
│       │   └── mri
│       │       └── brain.mgz
│       └── sub-1
│           └── mri
│               └── orig.mgz
├── sub-1
│   ├── anat
│   │   └── sub-1_desc-brain_mask.nii.gz
│   ├── figures
│   │   └── sub-1_desc-sdc_bold.svg
│   ├── fmap
│   │   └── sub-1_acq-task_run-1_fmapid-auto00000_desc-coeff_fieldmap.nii.gz
│   └── func
│       └── sub-1_task-nback_space-T1w_desc-brain_mask.nii.gz
└── sub-1.html
```

#### when run without sessions (without bids-filter-file)
`docker run --rm -v <local_path_for_output>:/out_tmp -v <local_path_to_directory_with_filterfile>:/code
fake_fmriprep_image inp /out_tmp participant --participant-label=sub-1 
--bids-filter-file=/code/<filter_file>`

```bash
out_tmp/
├── dataset_description.json
├── desc-aparcaseg_dseg.tsv
├── desc-aseg_dseg.tsv
├── logs
│   ├── CITATION.bib
│   ├── CITATION.html
│   ├── CITATION.md
│   └── CITATION.tex
├── sourcedata
│   └── freesurfer
│       ├── fsaverage
│       │   └── mri
│       │       └── brain.mgz
│       └── sub-1
│           └── mri
│               └── orig.mgz
├── sub-1
│   ├── figures
│   │   └── sub-1_ses-baseline_desc-sdc_bold.svg
│   └── ses-baseline
│       ├── anat
│       │   └── sub-1_ses-baseline_desc-brain_mask.nii.gz
│       ├── fmap
│       │   └── sub-1_ses-baseline_acq-task_run-1_fmapid-auto00000_desc-coeff_fieldmap.nii.gz
│       └── func
│           └── sub-1_ses-baseline_task-nback_space-T1w_desc-brain_mask.nii.gz
└── sub-1.html
```


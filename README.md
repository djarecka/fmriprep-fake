This repository is used to build a BIDS App called `fmriprep-fake`. This BIDS App can generate derivatives that mimic the derivatives from fMRIPrep. 

The built Docker image can be found in DockerHub: [djarecka/fmriprep_fake](https://hub.docker.com/r/djarecka/fmriprep_fake).

This BIDS App takes three positional arguments: `bids_dir`, `output_dir` and `analysis_level` (that has to be 'participant').

It also takes several optional named arguments:
* `--participant-label`: e.g. 'sub-111'
* `--bids-filter-file`:
    * This is used to extract sessions if available under "bold" item;
    * e.g., `{"bold": {"datatype": "func", "suffix": "bold", "session": "baseline"}}`
* `--output-layout`: choices are:
    * `bids` (default): latest fMRIPrep output layout, for fMRIPrep `21.0+`
    * `legacy`: previous fMRIPrep output layout, for fMRIPrep `< 21.0`

More arguments can be added too, however, currently `fmriprep-fake` does not consider them and won't change output files based on them.

## Example of usage and output

### when run without sessions (without `--bids-filter-file`)
`docker run --rm -v <local_path_for_output>:/out_tmp 
djarecka/fmriprep_fake:0.1.0 inp /out_tmp participant --participant-label=sub-1`

<details>
<summary>Output layout:</summary>

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
</details>


### when run with sessions (with `--bids-filter-file`)
`docker run --rm -v <local_path_for_output>:/out_tmp -v <local_path_to_directory_with_filterfile>:/code
djarecka/fmriprep_fake:0.1.0 inp /out_tmp participant --participant-label=sub-1 
--bids-filter-file=/code/<filter_file>`

<details>
<summary>Output layout:</summary>

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

</details>

### when generating legacy output layout (using `--output-layout legacy`)
With legacy output layout, we expect two folders will be generated: `fmriprep` and `freesurfer`.

Here, we use updated version `0.1.2`:

`docker run --rm -v <local_path_for_output>:/out_tmp -v <local_path_to_directory_with_filterfile>:/code
chenyingzhao/fmriprep_fake:0.1.2 inp /out_tmp participant --participant-label=sub-01 --output-layout legacy`

<details>
<summary>Output layout:</summary>

```
out_tmp/
├── fmriprep
│   ├── dataset_description.json
│   ├── desc-aparcaseg_dseg.tsv
│   ├── desc-aseg_dseg.tsv
│   ├── logs
│   │   ├── CITATION.bib
│   │   ├── CITATION.html
│   │   ├── CITATION.md
│   │   └── CITATION.tex
│   ├── sub-01
│   │   ├── anat
│   │   │   └── sub-01_desc-brain_mask.nii.gz
│   │   ├── figures
│   │   │   └── sub-01_desc-sdc_bold.svg
│   │   ├── fmap
│   │   │   └── sub-01_acq-task_run-1_fmapid-auto00000_desc-coeff_fieldmap.nii.gz
│   │   ├── func
│   │   │   └── sub-01_task-nback_space-T1w_desc-brain_mask.nii.gz
│   │   └── log
│   │       └── 20230713_154731
│   │           └── fmriprep.toml
│   └── sub-01.html
└── freesurfer
    ├── fsaverage
    │   └── mri
    │       └── brain.mgz
    └── sub-01
        └── mri
            └── orig.mgz
```

</details>

## For developers
* [prep_docker.sh](prep_docker.sh): Build the Docker image
    * Please increment `version_tag` number;
    * Please change `dockerhub_username` to the appropriate user account.
    * Note that currently we use multi-architecture build, so that the built Docker image can be run on both Mac M1 system and Linux system. For more details, please see comments in this file.
* [Dockerfile](Dockerfile)
    * The Dockerfile used for building the Docker image.
* [test.sh](test.sh): Used for testing out the key python script of this BIDS App, [fake_script.py](fake_script.py)
    * Please change the variables under `[FIX ME]`.
    * Example usage can be found in the beginning of this file.


## Docker image version history
* 0.1.1 (available at [`chenyingzhao/fmriprep_fake`](https://hub.docker.com/r/chenyingzhao/fmriprep_fake)):
    * added another folder layer in output directory: `fmriprepfake`
    * changed Dockerfile base image from `python:3.8` to `python:3.8.16-bullseye`
        as seems the former one is not directly available anymore/currently shares tag with the latter one.
    * Above version is deprecated as it does not follow any fMRIPrep's output layout.
* 0.1.2 (available at [`chenyingzhao/fmriprep_fake`](https://hub.docker.com/r/chenyingzhao/fmriprep_fake)):
    * added `--output-layout` argument, which accepts `bids` and `legacy` output layouts.
    * see [PR #3](https://github.com/djarecka/fmriprep-fake/pull/3) for more.

import click
import json

@click.command(help="fake fmriprep", context_settings=dict(
    ignore_unknown_options=True,
    allow_extra_args=True,
))
@click.argument('bids_dir')
@click.argument('output_dir')
@click.argument('analysis_level', type=click.Choice(['participant']))
@click.option(
    "--participant-label",
    required=True,
    help="participant label, e.g. sub-111"
)
@click.option(
    "--bids-filter-file",
    help="bids filter file with sessions, optional"
)
def main(bids_dir, output_dir, analysis_level, participant_label, bids_filter_file):
    from pathlib import Path
    # files will be saved to this directory:
    out_dir = Path(output_dir) / "fmriprepfake"
    print("FAKE script: out_dir", out_dir.resolve())
    print("bids_dir: ", bids_dir)
    print("output_dir: ", output_dir)
    print("analysis_level: ", analysis_level)
    print("participant-label", participant_label)
    session = None
    if bids_filter_file:
        with open(bids_filter_file) as f:
            data_filter = json.load(f)
            if "session" in data_filter["bold"]:
                session = data_filter["bold"]["session"]
    print("session", session)

    print("Creating out_dir")
    out_dir.mkdir(parents=True, exist_ok=True)
    print("Creating tsv and json files")
    for filename in ["dataset_description.json", "desc-aparcaseg_dseg.tsv", "desc-aseg_dseg.tsv"]:
        (out_dir / filename).open('w').write(f'i am a fake file: {filename}')
    print("Creating an html file")
    (out_dir / f"{participant_label}.html").open('w').write('it is a fake html report')
    print("Creating logs directory with some files")
    (out_dir / "logs").mkdir(parents=True, exist_ok=True)
    for ext in ["bib", "html", "md", "tex"]:
        (out_dir / "logs" / f"CITATION.{ext}").open("w").write(f'i am a fake file: CITATION.{ext}')

    print("Creating sub directory")
    (out_dir / participant_label).mkdir(parents=True, exist_ok=True)
    print("Creating figures directory with an example of a file")
    (out_dir / participant_label / "figures").mkdir(parents=True, exist_ok=True)
    if session:
        (out_dir / participant_label / "figures" / f"{participant_label}_ses-{session}_desc-sdc_bold.svg").open("w").write("a fake file")
    else:
        (out_dir / participant_label / "figures" / f"{participant_label}_desc-sdc_bold.svg").open("w").write("a fake file")
    if session:
        print("Creating a session directory")
        (out_dir / participant_label / f"ses-{session}").mkdir(parents=True, exist_ok=True)
        sub_ses_dir = out_dir / participant_label / f"ses-{session}"
    else:
        sub_ses_dir = out_dir / participant_label
    print("Creating anat, func and fmap inside with an example of files")
    for dirname in ["anat", "func", "fmap"]:
        (sub_ses_dir / dirname).mkdir(parents=True, exist_ok=True)
    if session:
        (sub_ses_dir / "anat" / f"{participant_label}_ses-{session}_desc-brain_mask.nii.gz").open("w").write("an example of anat file: {participant_label}, {session}")
        (sub_ses_dir / "func" / f"{participant_label}_ses-{session}_task-nback_space-T1w_desc-brain_mask.nii.gz").open("w").write(f"an example of func file {participant_label}, {session}")
        (sub_ses_dir / "fmap" / f"{participant_label}_ses-{session}_acq-task_run-1_fmapid-auto00000_desc-coeff_fieldmap.nii.gz").open("w").write(f"an example of fmap file {participant_label}, {session}")
    else:
        (sub_ses_dir / "anat" / f"{participant_label}_desc-brain_mask.nii.gz").open("w").write(f"an example of anat file {participant_label}")
        (sub_ses_dir / "func" / f"{participant_label}_task-nback_space-T1w_desc-brain_mask.nii.gz").open("w").write(f"an example of func file {participant_label}")
        (sub_ses_dir / "fmap" / f"{participant_label}_acq-task_run-1_fmapid-auto00000_desc-coeff_fieldmap.nii.gz").open("w").write(f"an example of fmap file {participant_label}")

    print("Creating freesurfer/fsaverage and freesurfer/participant-label with some example of subdirectories and files")
    (out_dir / f"sourcedata/freesurfer/{participant_label}/mri").mkdir(parents=True, exist_ok=True)
    (out_dir / f"sourcedata/freesurfer/{participant_label}/mri" / "orig.mgz").open("w").write(f"example for freesurfer/{participant_label}/mri")
    (out_dir / "sourcedata/freesurfer/fsaverage/mri").mkdir(parents=True, exist_ok=True)
    (out_dir / "sourcedata/freesurfer/fsaverage/mri" / "brain.mgz").open("w").write(f"example for freesurfer/fsaverage/mri")

    print(f"all fake directories and files created for participant: {participant_label} and session: {session}")


if __name__ == "__main__":
    main()
 

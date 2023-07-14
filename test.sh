# conda activate mydatalad

# example usage:
#  $ bash test.sh legacy   # for legacy output layout
#  $ bash test.sh bids   # for BIDS output layout

output_layout=$1    # "legacy" or "bids" (default)

# ++++++++++++++++++++++ [FIX ME] ++++++++++++++++++++++++++
main_folder="/Users/chenyzh/Desktop/Research/Satterthwaite_Lab/datalad_wrapper/data"
input_dir="${main_folder}/t8urc"   # single-ses toy data
output_main_dir="${main_folder}/test_fmriprepfake"
subid="sub-01" 
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

output_dir=${output_main_dir}/"fmriprep-"${output_layout}"-layout"
# check if the output_dir exists:
if [[ -d ${output_dir} ]]; then
    echo "test.sh: removing the existing output folder..."
    rm -r ${output_dir}
fi

cmd="python fake_script.py"
cmd+=" ${input_dir}"
cmd+=" ${output_dir}"
cmd+=" participant"
cmd+=" --participant-label=${subid}"
if [[ $output_layout == "legacy"  ]]; then
    cmd+=" --output-layout ${output_layout}"   # if it's "bids", no need to add.
fi

echo $cmd
$cmd

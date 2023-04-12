# conda activate mydatalad

main_folder="/Users/chenyzh/Desktop/Research/Satterthwaite_Lab/datalad_wrapper/data"
input_dir="${main_folder}/t8urc"   # single-ses toy data
output_dir="${main_folder}/test_fmriprepfake"
subid="sub-01"

cmd="python fake_script.py"
cmd+=" ${input_dir}"
cmd+=" ${output_dir}"
cmd+=" participant"
cmd+=" --participant-label=${subid}"

echo $cmd
$cmd

# cpac-utils
Utility functions to fetch and organize time-series derivatives after data has been preprocessed using C-PAC


## Requirements

Uses python 3 as well as the following python packages

- awscli 
- numpy
- scipy
- pandas

```
pip install -r requirements.txt
```

## Usage

### Download Data
Preprocessed data is expected to be located at in `data/cpac`

```
|--data
  |--cpac
    |--derivatives
|--src
|--requirements.txt
|--README

```
For example data preprocessed at OpenNeuro.org can be downloaded as follows

```
./src/download_data.sh
```

### Fetch and Organize ROI Time-Series

Given a textfile `path_roi_timeseries_mask_<ATLASNAME>.txt` containing the list of paths to all outputs from C-PAC such as  `roi_stats.csv`, the function `collect_timeseries.py` will load, clean and reorganize into `.mat` and `.pickle` data structures by participant and task.	

```
python3 collect_timeseries.py path_roi_timeseries_mask_$ATLASNAME.txt

```

The example script `src/organize_timeseries.sh` creates a textfile of pathnames and then calls the above command. 


After downloading and organizing the timeseries, the outputs look as follows: 

```
data/cpac/derivatives/pipeline_analysis/compcor_ncomponents_5_selector_pc10.linear1.wm0.global0.motion1.quadratic1.gm0.compcor1.csf1/sub-01_ses-post:
sub-01_ses-post_task-rest_run-01_CC200.mat     sub-01_ses-post_task-rest_run-02_CC200.pickle
sub-01_ses-post_task-rest_run-01_CC200.pickle  sub-01_ses-post_task-rest_run-03_CC200.mat
sub-01_ses-post_task-rest_run-02_CC200.mat     sub-01_ses-post_task-rest_run-03_CC200.pickle

data/cpac/derivatives/pipeline_analysis/compcor_ncomponents_5_selector_pc10.linear1.wm0.global0.motion1.quadratic1.gm0.compcor1.csf1/sub-01_ses-pre:
sub-01_ses-pre_task-rest_run-01_CC200.mat     sub-01_ses-pre_task-rest_run-02_CC200.pickle
sub-01_ses-pre_task-rest_run-01_CC200.pickle  sub-01_ses-pre_task-rest_run-03_CC200.mat
sub-01_ses-pre_task-rest_run-02_CC200.mat     sub-01_ses-pre_task-rest_run-03_CC200.pickle

```

#!/bin/sh

DATADIR=data/cpac
PIPELINE=pipeline_analysis
ATLAS=CC200
ATLASNAME=CC200

# output only
ls data/cpac/output/pipeline_analysis/*/roi_timeseries/*/*/*/*/*.csv | grep $ATLAS > path_roi_timeseries_mask_$ATLASNAME.txt

python3 collect_timeseries.py path_roi_timeseries_mask_$ATLASNAME.txt



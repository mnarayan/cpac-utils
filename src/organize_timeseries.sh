#!/bin/sh

DATADIR=data/cpac
SRCDIR=src
PIPELINE=pipeline_analysis
ATLAS=CC200
ATLASNAME=CC200

# output with nuisance info directory
# ls ${DATADIR}/output/pipeline_analysis/*/roi_timeseries/*/*/*/*/*.csv | grep $ATLAS > path_roi_timeseries_mask_$ATLASNAME.txt

# output without nuisance info directory
ls ${DATADIR}/output/pipeline_analysis/*/roi_timeseries/*/*/*/*.csv | grep $ATLAS > path_roi_timeseries_mask_$ATLASNAME.txt

python3 ${SRCDIR}/collect_timeseries.py path_roi_timeseries_mask_$ATLASNAME.txt



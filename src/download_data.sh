#!/bin/sh

DATADIR=data/cpac

# ds001032
aws --no-sign-request s3 sync s3://openneuro.outputs/42975a576827105878073aac3f12457a/49e67dd4-1ead-48b0-996f-ab81c6ef898c ${DATADIR}


#!/bin/bash

READ_DIR=$1
OUT=$2
READ_LIST=""

mkdir -p "${OUT}"
mkdir -p tmp

for read in "${READ_DIR}"/*.fastq.gz
do
  READ_LIST="${READ_LIST} ${read}"
done

gzip -dc ${READ_LIST}\
| awk '/^@/ {seq=""; inseq=1; next} /^\+/ {print seq; inseq=0; next} inseq {seq = seq $0}' \
| sort -S 50% -T ./tmp \
| tr NT TN \
| ropebwt2 -LR \
| tr NT TN \
| msbwt3 convert ${OUT}

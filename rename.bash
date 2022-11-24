#!/bin/bash

#remove the unnecessary middle of the file name- remove 'echo' before execution

for f in *.gz; do echo mv "$f" "${f/220329_2022_03_29_Miseq_Run8_Nikola_Manon_Naina.220415.MiSeq.FCB.lane1.gcap_20_01../_}"; done

#remove GC121272_ from the beginning of the file name- remove 'echo'before execution

for f in *.fastq; do echo mv "$f" "${f/GC121272_/}"; done

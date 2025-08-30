#! /usr/bin/env bash
#
#  87 zenodos,  30 are found, 22 of those have a concept DOI


for doi in $(awk -F. '{print $NF}' ZenodoDOIsNeedingConceptDOIs.csv); do
  echo $doi
  ./zenodo1.py $doi
done 

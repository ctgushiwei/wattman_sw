#!/bin/bash
dir_list=$1
echo $dir_list
fcount= ls $dir_list -lR|grep "_gt.json"|wc -l
echo  $fcount


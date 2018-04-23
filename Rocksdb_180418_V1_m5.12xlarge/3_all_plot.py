#!/bin/bash

bufflist="64 16384"

function stat_plot(){
	factors="
		memtable.hit 
		memtable.miss
		l0.hit
		l1.hit
		block.cache.hit
		block.cache.miss
	"
	for buff in $bufflist; do
		for factor in $factors; do
			fname=$factor.$buff.dat
			echo "$fname ...."
			python2.7 ./stat_plot.py $fname
		done
	done
}

function perf_plot(){
	factors="
		fillseq
		fillrandom
		readseq
		readrandom
	"
	for buff in $bufflist;do
	
	done	




	for buff in $bufflist; do
		for factor in $factors; do
			fname=$factor.$buff.dat
			echo "$fname ...."
			python2.7 ./perf_plot.py $fname
		done
	done
}

perf_plot



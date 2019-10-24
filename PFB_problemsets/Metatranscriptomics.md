# Programming for biology 2019 

## Group project idea: Metagenomics pipeline for unidentified RNAseq reads

### Members: Marina Mann, Alissa Lance-Byrne, Brooke  _ etc. (and TA!)

Input: filtered, adapter-removed, soft clipped RNAseq 150-300bp PE reads, whcih have not been aligned yet

Input style: curated bacterial RNA from well annotated respository of diverse bacteria

### Background:

When dealing with RNAseq from organisms containing obligate, facultative, opportunistic and pathogenic symbionts, read alignments are never 100%. Usually, a large proportion of total reads will align to the host organism, while the rest remain unmapped, and unknown. What to do with these reads?

There are currently a fair number of metatranscriptomic microbiome pipelines. We're going to reinvent the wheel to better understand the process involved in identifying unidentified reads. In the process, we'll learn to code the topics outlined below, using the listed subskills. 

Script Goals: 

1. make human friendly, including adding paragraphs """ """ and Error messages at each key step, so an idiot can figure it out. :) 

2. keep project applicable to each member

   ### To Do List

- choose RNA data set - should be small, alignments run quickly and blast won't take too long
  - Make script to find and download them from the web repository, and save in specified `directory`

- need to implement BLAST from python script
  - tBLASTn all reads? Which matrix? multiple matrixes, compare results? Use methods from Bill Pearson's lectures/workshop
- Need to collect BLAST reports and parse out necessary information into data file
  - We want IDs of organisms that reads aligned to, alignment stats. 
  - Use `if` and `else` statements to determine `which` blast values are appropriate. `for` loop through table of BLAST result lines, `append` to a `dictionary()` where the `key` is the appropriate blast result (i.e BLSM50 vs BLSM62) and the `value` is a `list` of information, including the e-value, organism name, %_id 
  - from each of the organisms identified as being present in the sample set, search blast and download the most appropriate genome to use for read alignment.
- 
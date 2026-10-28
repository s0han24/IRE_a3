# Benchmarking ANN Search

## IMPORTANT
One-command reproduction: running `bash run_all.sh` inside src/ must regenerate every number, figure and table in the report from the data files. Running `bash run_all.sh --quick` must do the same on a small subset of the data (for example the first 100,000 vectors) in under 15 minutes on a laptop. The README must explain how to run both. For this purpose, make a bash file to which any run commands can be appended which tracks the full pipeline, additionally, the README needs to have a description of the pipeline.

## Datasets:
- grab SIFT and GloVe-100 from https://github.com/erikbern/ann-benchmarks
- Split queries in both benchmarks into 2 parts the first 5000 are for tuning parameters, experimentation, etc and the last 5000 are for reporting numbers. The datasets have 10000 queries each
- Normalize GloVe vectors and use euclidean distance throughout, even for GloVe-100

## Baseline:
- Build exact search with FAISS which will be the reference throughout
- Write a recall@10 function from scratch that deals with ties at 10th place so that ties at neighbour 10 are not counted as mistakes. Check that this works with unit tests
- The exact search should agree with the neighbours stored in the data file exactly. Write a check. Here, exact matches mean that the nearest neighbours with tie handling should match but the lists themselves need not match to allow for arbitrary tie-breaking.
- Time the exact search both one query at a time and all queries in a batch

## Benchmarks:
- All "recall" mentions are recall@10
- The objective is to benchmark HNSW, IVF-Flat and IVF-PQ on both datasets.
- Try various settings and do a parameter sweep for a comprehensive benchmark
- At least one parameter config in each sweep should get a recall of 95% or higher. If such a config is elusive, flag it.
- The following need to be reported:
    1. a plot of per dataset recall@10 against qps showing the tradeoff for each index and the exact baseline from before
    2. A table of queries per second each index achieves at recall 0.9 and 0.95 (need not be programmatic, can be inferred manually, make sure the data is there though)
    3. a table of build time, index size, bytes per vector for each index at recall 95%(best config)

## Experiments on standard data:
Before implementing and running the following, commit the following hypothesis to the README:
```
### Hypothesis
1. exact search should have the worst scaling of the 3, the qps increases linearly with number of vectors but the recall saturates giving a exponential-looking increase in qps against the recall
2. HNSW and IVF-Flat should have better scaling than exact search, HNSW should perform better than IVF-Flat given the right hyperparameters, though it may perform worse on certain configs. 
```

On SIFT, repeat the benchmark at 100k, 300k, 1M vectors and see how the cost of reaching recall 0.95 grows for HNSW, IVF-Flat and exact search for the best few hyperparameter configs from the previous section.

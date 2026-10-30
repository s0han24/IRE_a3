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
- Repeat each timing a few times and take the median
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

On SIFT, repeat the benchmark at 100k, 300k, 1M vectors and see how the cost of reaching recall 0.95 grows for HNSW, IVF-Flat and exact search for all the hyperparameter configs from the previous section.

## Experiments on drifted data:
Before implementing and running the following, commit the following hypothesis to the README:
```
### Hypothesis
1. Two metrics are calculated, one is recall against the ground truth and recall against exact search. All indexes are expected to show some degradation against the ground truth but still show similar recall against the exact search.
2. QPS is measured too, this is expected to show no changes at all.
3. IVF-PQ is expected to show the greatest degradation and IVF-Flat the least because for well separated clusters, the drift may not affect step 1 which decides the cluster in which a query lands. Step 2 however will be affected by drift because of the brittle quantization. IVF-Flat for well separated clusters should show similar degradation behaviour to exact search.
```

Simulate a change in preprocessing that the index was not rebuilt for, and see which index degrades first and whether rebuilding recovers it.
- SIFT only, both query halves used as before (tune / report)
- Two kinds of drift, each a separate experiment. Never apply both together. Check this out for the 3 separate configurations mentioned for each drift:
    1. Mean shift: add the constant c = 5, 10, 15 to every coordinate of every vector. No scaling, no normalisation
    2. Rotation: pair up the dimensions (0,1), (2,3), ... and rotate each pair by 2,3,5 degrees, similar to RoPE
- For each kind of drift, run two conditions:
    1. stale: index built on the original base vectors, queries transformed
    2. rebuilt: base vectors and queries transformed the same way, index rebuilt from scratch
- For every condition run the full hyperparameter sweep from the Benchmarks section (HNSW, IVF-Flat, IVF-PQ, plus exact search)
- For every config report two recalls:
    1. recall against the exact neighbours of the transformed query in the base the index was built on
    2. recall against the exact neighbours of the original query in the original base
- Also report QPS (median of repeats), build time, index size and bytes per vector for every config, as in the Benchmarks section
- Report for each kind of drift:
    1. a recall@10 vs qps plot with the clean, stale and rebuilt curves for each index
    2. a table of every config with all the numbers above
    3. a table of the recall drop per config (stale minus clean, rebuilt minus clean) and which index loses its 0.95 config first
- Add to run_all.sh, including the --quick mode

- run_all.sh should be in code/

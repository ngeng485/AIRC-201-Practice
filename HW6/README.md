# HW6 - Experiment Reproducibility

In this assignment, you will debug experiment reproducibility issues. You will explore the concept of the "Power of Two Choices" in load balancing. The problem setup is an experiment where we investigate the maximum load when randomly placing balls into bins using different strategies.

## Problem Setup: The Power of Two Choices

Suppose we have `M` bins and `N` balls. In our experiment, we will set `M = 100` bins and `N = 10000` balls. You will simulate placing each of the `N` balls sequentially into the bins using three different strategies:

- **Strategy 1:** For every ball, choose 1 bin uniformly at random and place the ball there.
- **Strategy 2:** For every ball, choose 2 distinct bins uniformly at random and place the ball into the bin with fewer balls. If both bins have the same number of balls, place it into the one with the smaller index in the array of bins.
- **Strategy 3:** For every ball, choose 3 distinct bins uniformly at random and place the ball into the bin with the least number of balls among the choices. If there is a tie, place it into the bin with the smallest index among those tied bins.

For each strategy over the 10,000 timesteps (each ball placement is one timestep), you will track the maximum number of balls in any single bin. You will run 10 independent trials for each strategy to observe confidence intervals.

## Experiment Implementation Details

The experiment is to be implemented deterministically to match our expectations using `numpy`. 
- **Trials & Random Seed**: You must run exactly 10 trials (0 to 9). Be sure to set `np.random.seed(42 + trial)` at the start of each trial (for that specific trial index). Wait until inside the trial loop to do this.
- **Bin tie-breaking rule:** Always pick the chosen bin with the absolute smallest index out of the tied bins with the minimum count based on the random sample choices (`choice` should be called with `replace=False`).

## Student Task

While `HW6/problems.py` looks like it implements the above logic, the `run_experiments()` method has been purposefully injected with a few small reproducibility bugs.

**Your task is to review the code in `run_experiments()`, trace its execution against the specs, find the inserted bugs, and fix them!**

You can run `python HW6/problems.py` to generate the plots (which will be saved in `HW6/results/plot.png`) to help debug the output of the experiment, but to truly verify your implementation, you **must run `python HW6/tests.py`**. The test script will check the exact final values of your 10 trials against the reference implementation's target outputs.

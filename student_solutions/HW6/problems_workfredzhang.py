import numpy as np
import os
import matplotlib.pyplot as plt

def run_experiments():
    N = 10000
    M = 100
    trials = 10
    
    results = {1: np.zeros((trials, N)), 2: np.zeros((trials, N)), 3: np.zeros((trials, N))}
    
    for strategy in [1, 2, 3]:
        for trial in range(trials):
            # BUG 1 FIX: seed on `trial`, not `strategy`
            np.random.seed(42 + trial)
            
            # Initialize bins and balls
            bins = np.zeros(M, dtype=int)
            max_balls = 0
            
            # BUG 2 FIX: removed the `if strategy == 3: curr_strat += 1` block
            # curr_strat should simply equal strategy (1, 2, or 3 choices respectively)
            curr_strat = strategy

            for t in range(N):
                choices = np.random.choice(M, size=curr_strat, replace=False)
                
                # Find the minimum number of balls in the chosen bins
                min_balls = np.min(bins[choices])
                
                # Choose bin
                best_choices = [c for c in choices if bins[c] == min_balls]
                
                # BUG 3 FIX: use `min()` to pick smallest index among tied bins, not `max()`
                chosen_bin = min(best_choices)
                
                # Update bin and results
                bins[chosen_bin] += 1
                if bins[chosen_bin] > max_balls:
                    max_balls = bins[chosen_bin]
                results[strategy][trial, t] = max_balls
                
    return results

def plot_results(results):
    os.makedirs('HW6/results', exist_ok=True)
    plt.figure(figsize=(10, 6))
    
    for strategy in [1, 2, 3]:
        mean_vals = np.mean(results[strategy], axis=0)
        std_vals = np.std(results[strategy], axis=0)
        
        plt.plot(mean_vals, label=f'Strategy {strategy}')
        plt.fill_between(range(len(mean_vals)), mean_vals - std_vals, mean_vals + std_vals, alpha=0.2)
        
    plt.xlabel('Timestep')
    plt.ylabel('Max Balls in Any Bin')
    plt.title('The Power of Two Choices')
    plt.legend()
    plt.savefig('HW6/results/plot.png')
    plt.close()

if __name__ == '__main__':
    results = run_experiments()
    plot_results(results)
import numpy as np

def foo_stabilizer(foo, batch_size=8, tolerance=0.1, alpha=0.05, max_iterations=50):
    data = np.array([foo() for _ in range(batch_size)])
    for _ in range(max_iterations):
        sample_mean = np.mean(data)
        resamples = np.random.choice(data, size=(10000, len(data)))
        ci_lower, ci_upper = np.percentile(
            np.mean(resamples, axis=1), 
            [alpha * 50, 100 - alpha * 50]
        )
        margin = abs(sample_mean * tolerance)
        if (sample_mean - margin) <= ci_lower and ci_upper <= (sample_mean + margin):
            return sample_mean
        data = np.append(data, [foo() for _ in range(batch_size)])

    return sample_mean
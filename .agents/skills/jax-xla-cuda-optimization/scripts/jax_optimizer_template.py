import time
import jax
import jax.numpy as jnp

class JAXPerformanceProfiler:
    """
    Utility for benchmarking and profiling JAX JIT-compiled tensor operations on GPU/TPU.
    """
    def __init__(self):
        self.devices = jax.devices()
        print(f"JAX initialized on devices: {self.devices}")

    def profile_function(self, func, *args, warmups=2, runs=100):
        """Warm up XLA compiler, then measure mean execution latency."""
        # Warmup (triggers XLA compilation)
        for _ in range(warmups):
            res = func(*args)
            res.block_until_ready()

        start = time.perf_counter()
        for _ in range(runs):
            res = func(*args)
            res.block_until_ready()
        end = time.perf_counter()

        avg_latency_ms = ((end - start) / runs) * 1000.0
        print(f"Mean Execution Latency ({runs} runs): {avg_latency_ms:.4f} ms")
        return avg_latency_ms, res

if __name__ == '__main__':
    profiler = JAXPerformanceProfiler()
    @jax.jit
    def test_matmul(A, B):
        return jnp.dot(A, B)

    key = jax.random.PRNGKey(0)
    A = jax.random.normal(key, (1000, 1000))
    B = jax.random.normal(key, (1000, 1000))

    profiler.profile_function(test_matmul, A, B)

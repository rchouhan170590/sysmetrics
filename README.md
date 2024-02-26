# System Performance

The System Performance package provides tools to benchmark and visualize the performance of your system and specific processes over time.

## Installation

You can install the package using pip:

```bash
pip install system-performance

Usage
Benchmarking System Performance
To benchmark the system performance, use the SystemPerformanceBenchmark class:

python
Copy code
from system_performance.system_performance import SystemPerformanceBenchmark

# Create an instance of SystemPerformanceBenchmark
benchmark = SystemPerformanceBenchmark()

# Benchmark system performance for 60 seconds with 1-second intervals
benchmark.benchmark(duration_secs=60, interval_secs=1, save_graph=True, filename="system_performance.png")
This will generate a graph showing the system's memory usage, disk usage, swap usage, network speed, and IO operations over time.

Benchmarking Process Performance
To benchmark the performance of a specific process by name or PID, use the ProcessPerformanceBenchmark class:

python
Copy code
from system_performance.process_performance import ProcessPerformanceBenchmark

# Create an instance of ProcessPerformanceBenchmark
process_benchmark = ProcessPerformanceBenchmark()

# Benchmark performance of a process by name for 60 seconds with 1-second intervals
process_benchmark.benchmark_by_name(process_name="python", duration_secs=60, interval_secs=1, save_graph=True, filename="python_performance.png")

# Benchmark performance of a process by PID for 60 seconds with 1-second intervals
process_benchmark.benchmark_by_pid(pid=1234, duration_secs=60, interval_secs=1, save_graph=True, filename="pid_1234_performance.png")
This will generate a graph showing the CPU and memory usage of the specified process over time.

Contributing
Contributions to the System Performance package are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to customize and extend the code according to your needs!

typescript
Copy code

You can copy and paste this content directly into your README.md f
```

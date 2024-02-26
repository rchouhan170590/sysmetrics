import time
import psutil
import matplotlib.pyplot as plt
from typing import Union

class ProcessPerformanceBenchmark:
    def __init__(self):
        pass
    
    @staticmethod
    def _get_process_by_name(process_name: str) -> psutil.Process:
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == process_name:
                return psutil.Process(proc.info['pid'])
    
    @staticmethod
    def _get_process_by_pid(pid: int) -> psutil.Process:
        return psutil.Process(pid)
    
    def _benchmark_process_performance(self, process, duration_secs: int, interval_secs: int, save_file_path: str = None) -> None:
        timestamps = []
        cpu_usage = []
        memory_usage = []

        start_time = time.time()
        while time.time() - start_time < duration_secs:
            timestamp = time.time()
            cpu = process.cpu_percent(interval=interval_secs)
            memory = process.memory_percent()
            
            timestamps.append(timestamp)
            cpu_usage.append(cpu)
            memory_usage.append(memory)
            
        # Plot the data
        plt.figure(figsize=(10, 6))
        plt.plot(timestamps, cpu_usage, label='CPU Usage (%)')
        plt.plot(timestamps, memory_usage, label='Memory Usage (%)')
        plt.xlabel('Time')
        plt.ylabel('Percentage')
        plt.title(f'Performance of Process Over Time')
        plt.legend()
        
        # Save or show the graph
        if save_file_path:
            plt.savefig(save_file_path)
            print(f"Graph saved as {save_file_path}")
        else:
            plt.show()
    
    def benchmark_by_name(self, process_name: str, duration_secs: int, interval_secs: int, save_file_path: str = None) -> None:
        process = self._get_process_by_name(process_name)
        self._benchmark_process_performance(process, duration_secs, interval_secs, save_file_path)
    
    def benchmark_by_pid(self, pid: int, duration_secs: int, interval_secs: int, save_file_path: str = None) -> None:
        process = self._get_process_by_pid(pid)
        self._benchmark_process_performance(process, duration_secs, interval_secs, save_file_path)

import time
import psutil
import matplotlib.pyplot as plt
import logging
from typing import List

logger = logging.getLogger(__name__)

class SystemPerformanceBenchmark:
    def __init__(self):
        pass
    
    @staticmethod
    def _get_timestamps(duration_secs: int, interval_secs: int) -> List[float]:
        timestamps = []
        start_time = time.time()
        while time.time() - start_time < duration_secs:
            timestamp = time.time()
            timestamps.append(timestamp)
            time.sleep(interval_secs)
        return timestamps
    
    @staticmethod
    def _get_memory_usage() -> List[float]:
        memory_usage = []
        while True:
            memory = psutil.virtual_memory().percent
            memory_usage.append(memory)
            time.sleep(1)
        return memory_usage
    
    @staticmethod
    def _get_disk_usage() -> List[float]:
        disk_usage = []
        while True:
            disk = psutil.disk_usage('/').percent
            disk_usage.append(disk)
            time.sleep(1)
        return disk_usage
    
    @staticmethod
    def _get_swap_usage() -> List[float]:
        swap_usage = []
        while True:
            swap = psutil.swap_memory().percent
            swap_usage.append(swap)
            time.sleep(1)
        return swap_usage
    
    @staticmethod
    def _get_network_speed() -> List[float]:
        network_speed: list[float] = []
        while True:
            network = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
            network_speed.append(network)
            time.sleep(1)
        return network_speed
    
    @staticmethod
    def _get_io_operations() -> List[float]:
        io_operations = []
        while True:
            io = psutil.disk_io_counters().read_count + psutil.disk_io_counters().write_count
            io_operations.append(io)
            time.sleep(1)
        return io_operations
    
    def benchmark(self, duration_secs: int, interval_secs: int, save_file_path: str = None) -> None:
        timestamps = self._get_timestamps(duration_secs, interval_secs)
        memory_usage = self._get_memory_usage()
        disk_usage = self._get_disk_usage()
        swap_usage = self._get_swap_usage()
        network_speed = self._get_network_speed()
        io_operations = self._get_io_operations()
        
        # Plot the data
        plt.figure(figsize=(10, 6))
        plt.plot(timestamps, memory_usage, label='Memory Usage (%)')
        plt.plot(timestamps, disk_usage, label='Disk Usage (%)')
        plt.plot(timestamps, swap_usage, label='Swap Usage (%)')
        plt.plot(timestamps, network_speed, label='Network Speed (bytes)')
        plt.plot(timestamps, io_operations, label='IO Operations')
        plt.xlabel('Time')
        plt.ylabel('Percentage / Speed')
        plt.title('System Performance Over Time')
        plt.legend()
        
        # Save or show the graph
        if save_file_path:
            plt.savefig(save_file_path)
            logger.info(f"Graph saved as {save_file_path}")
        else:
            plt.show()
            logger.info("Graph displayed.")

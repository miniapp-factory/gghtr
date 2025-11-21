import time
import threading

class Stopwatch:
    def __init__(self):
        self._start_time = None
        self._elapsed = 0.0
        self._running = False
        self._lock = threading.Lock()

    def start(self):
        with self._lock:
            if not self._running:
                self._start_time = time.perf_counter()
                self._running = True

    def stop(self):
        with self._lock:
            if self._running:
                self._elapsed += time.perf_counter() - self._start_time
                self._running = False

    def reset(self):
        with self._lock:
            self._start_time = None
            self._elapsed = 0.0
            self._running = False

    def elapsed(self):
        with self._lock:
            if self._running:
                return self._elapsed + (time.perf_counter() - self._start_time)
            return self._elapsed

    def __str__(self):
        return f"{self.elapsed():.3f} seconds"

if __name__ == "__main__":
    sw = Stopwatch()
    print("Starting stopwatch...")
    sw.start()
    time.sleep(2)
    sw.stop()
    print(f"Elapsed: {sw}")
    sw.start()
    time.sleep(1)
    sw.stop()
    print(f"Elapsed: {sw}")
    sw.reset()
    print(f"After reset: {sw}")

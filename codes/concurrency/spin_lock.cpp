#include <atomic>

class SpinLock {
public:
    SpinLock() : flag_(false) {}

    void Lock() {
        while (flag_.exchange(true, std::memory_order_acquire)) {
            // Spin until the lock is acquired
        }
    }

    void Unlock() {
        flag_.store(false, std::memory_order_release);
    }

private:
    std::atomic<bool> flag_;
};

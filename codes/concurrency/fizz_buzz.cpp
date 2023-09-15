#include "../base.h"

class FizzBuzz {
private:
    int n;
    int cur;
    mutex mtx;
    condition_variable cv;


public:
    FizzBuzz(int n) {
        this->n = n;
        this->cur = 1;
    }

    // printFizz() outputs "fizz".
    void fizz(function<void()> printFizz) {
        while (true) {
            unique_lock<mutex> lock(mtx);
            cv.wait(lock, [&](){return (cur > n || (cur % 3 == 0 && cur % 5 != 0));});
            if (cur > n)
                return;

            printFizz();
            cur += 1;
            cv.notify_all();
        }        
    }

    // printBuzz() outputs "buzz".
    void buzz(function<void()> printBuzz) {
        while (true) {
            unique_lock<mutex> lock(mtx);
            cv.wait(lock, [&](){return (cur > n || (cur % 3 != 0 && cur % 5 == 0));});
            if (cur > n)
                return;
            printBuzz();
            cur += 1;
            cv.notify_all();
        }
    }

    // printFizzBuzz() outputs "fizzbuzz".
	void fizzbuzz(function<void()> printFizzBuzz) {
        while (cur <= n) {
            unique_lock<mutex> lock(mtx);
            cv.wait(lock, [&](){return (cur > n || (cur % 3 == 0 && cur % 5 == 0));});
            if (cur > n)
                return;

            printFizzBuzz();
            cur += 1;
            cv.notify_all();
        }         
    }

    // printNumber(x) outputs "x", where x is an integer.
    void number(function<void(int)> printNumber) {
        while (cur <= n) {
            unique_lock<mutex> lock(mtx);
            cv.wait(lock, [&](){return (cur > n || (cur % 3 && cur % 5));});
            if (cur > n)
                return;

            printNumber(cur);
            cur += 1;
            cv.notify_all();
        }        
    }
};
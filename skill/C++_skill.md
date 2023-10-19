# smart pointer
- unique pointer
`#include <iostream>
#include <memory>

class MyClass {
public:
    void DoSomething() {
        std::cout << "MyClass is doing something." << std::endl;
    }
};

int main() {
    // Creating a unique_ptr to an instance of MyClass
    std::unique_ptr<MyClass> uniqueObj = std::make_unique<MyClass>();

    // Accessing the object's member function
    uniqueObj->DoSomething();

    // When uniqueObj goes out of scope, the memory is released automatically
    return 0;
}`

- shared pointer
`
#include <iostream>
#include <memory>

class Node {
public:
    std::shared_ptr<Node> next;

    Node(int data) : data(data) {}

private:
    int data;
};

int main() {
    // Creating a cyclic reference with shared_ptr
    std::shared_ptr<Node> node1 = std::make_shared<Node>(1);
    std::shared_ptr<Node> node2 = std::make_shared<Node>(2);
    
    node1->next = node2;
    node2->next = node1;

    // When both shared_ptrs go out of scope, memory is released properly
    return 0;
}

`
# Constructor and Destructor
- Member initialization via a member initialization list
  - Because the C++ standard says so, the members in a member initializer list are always initialized in the order in which they are defined inside the class (not in the order they are defined in the member initializer list).
  - Member initialization lists are more efficient than assignment within the constructor body. When you use an assignment inside the constructor body, the default constructor for the member variable is called first, followed by the assignment operator. In contrast, member initialization lists allow you to directly initialize the member variable with the desired value.
  - Member initialization lists are required for constant members (const) and reference members (&) because these members must be initialized upon construction and cannot be reassigned later.

`
#include <algorithm> // for std::max
#include <iostream>

class Foo
{
private:
    int m_x{};
    int m_y{};

public:
    Foo(int x, int y)
        : m_y{ std::max(x, y) }, m_x{ m_y } // issue on this line
    {
    }

    void print() const
    {
        std::cout << "Foo(" << m_x << ", " << m_y << ")\n";
    }
};
`

- If the virtual destructor is not defined in the base class, then when an object of a derived class is deleted through a pointer to the base class, the destructor of the base class will be called instead of the destructor of the derived class. This can lead to memory leaks and resource leaks if the derived class has dynamically allocated memory or resources that are not properly cleaned up by the base class destructor. Additionally, if the base class destructor has any virtual functions, they will not be called, which can result in undefined behavior.
- When a derived class object is destroyed through a base class pointer or reference, it is important for the correct derived class destructor to be called. If the base class destructor is not declared as virtual, the base class destructor will be called instead of the derived class destructor, even if the object being deleted is actually of the derived class type. This can lead to resources not being properly cleaned up and released, causing memory leaks and other undefined behavior.

- Therefore, it is recommended to declare the base class destructor as virtual, to ensure that the correct derived class destructor is called, when destroying the derived class object through a base class pointer or reference.

- When an exception is thrown in a scope, the stack is unwound and all the objects created in the scope are destroyed, starting from the most recently created object. If an object has a destructor, it will be called automatically by the compiler during the stack unwinding process. This means that even if an exception is thrown, all the objects in the scope will be cleaned up properly, which can help avoid memory leaks or other resource leaks.


`
#include <iostream>
#include <utility>

class MyClass {
public:
  MyClass() { std::cout << "Default constructor called" << std::endl; }
  MyClass(const MyClass& other) { std::cout << "Copy constructor called" << std::endl; }
  MyClass(MyClass&& other) noexcept { std::cout << "Move constructor called" << std::endl; }
};

void foo(MyClass obj) {}

int main() {
  MyClass obj1;                // Default constructor called
  MyClass obj2 = obj1;         // Copy constructor called
  MyClass obj3 = std::move(obj1);  // Move constructor called

  foo(obj1);                  // Copy constructor called

  return 0;
}

`

- the copy constructor will also be called for MyClass obj2(obj1);. This syntax is called direct initialization and it creates a new object obj2 initialized with the values of obj1. Since this creates a new object, the copy constructor is called to copy the values.

- MyClass obj2 = obj1; will call the copy constructor, not the copy assignment operator. The copy assignment operator is invoked when an object already exists and we want to assign a new value to it. For example, obj2 = obj1; would call the copy assignment operator.
## the virtual table
- the compiler also adds a hidden pointer that is a member of the base class, which we will call *__vptr. *__vptr is set (automatically) when a class object is created so that it points to the virtual table for that class. Unlike the *this pointer, which is actually a function parameter used by the compiler to resolve self-references, *__vptr is a real pointer. Consequently, it makes each class object allocated bigger by the size of one pointer. It also means that *__vptr is inherited by derived classes, which is important. 
- The entries in the virtual table point to the most-derived version of the function that objects of that class are allowed to call. 
`
int main()
{
    D1 d1 {};
    Base* dPtr = &d1;
    dPtr->function1();

    return 0;
}
`
[virtual table](../pictures/VTable.gif)

- Note that because dPtr is a base pointer, it only points to the Base portion of d1. However, also note that *__vptr is in the Base portion of the class, so dPtr has access to this pointer. Finally, note that dPtr->__vptr points to the D1 virtual table! Consequently, even though dPtr is of type Base*, it still has access to D1’s virtual table (through __vptr). 
- First, the program recognizes that function1() is a virtual function. Second, the program uses dPtr->__vptr to get to D1’s virtual table. Third, it looks up which version of function1() to call in D1’s virtual table. This has been set to D1::function1(). Therefore, dPtr->function1() resolves to D1::function1()!

# pure virtual functions
- Using a pure virtual function has two main consequences: First, any class with one or more pure virtual functions becomes an abstract base class, which means that it can not be instantiated! 
- Second, any derived class must define a body for this function, or that derived class will be considered an abstract base class as well.

`
#include <string>
#include <string_view>

class Animal // This Animal is an abstract base class
{
protected:
    std::string m_name {};

public:
    Animal(std::string_view name)
        : m_name{ name }
    {
    }

    const std::string& getName() const { return m_name; }
    virtual std::string_view speak() const = 0; // note that speak is now a pure virtual function

    virtual ~Animal() = default;
};


`

## virtual destructor
- Resource Cleanup: If a base class manages any resources (such as dynamically allocated memory or file handles) and doesn't have a virtual destructor, deleting an object of a derived class through a base class pointer won't call the derived class destructor. As a result, any custom cleanup logic in the derived class's destructor may not execute, leading to resource leaks. By declaring the destructor as virtual in the base class, you ensure that the correct destructor (including any destructors in derived classes) is called when objects are deleted through pointers or references to the base class.  

# const
- const int* ptr or int const* ptr:
  - The integer pointed to by ptr is constant and cannot be modified through this pointer.
  - ptr itself can be modified to point to another memory location.
  - This means that the value of the integer at the memory location ptr is pointing to is read-only, but the pointer ptr itself can be changed to point somewhere else.
`
const int x = 10;
const int y = 20;
const int* ptr = &x;
ptr = &y;       // This is valid.
//*ptr = 30;    // This would be an error, because the pointed value can't be changed.
`

- int* const ptr:
  - The pointer ptr itself is constant and cannot be modified to point to another memory location.
  - The integer pointed to by ptr can be modified.
  - This means that the value of the integer at the memory location ptr is pointing to can be changed, but the pointer ptr itself cannot be reassigned to a new memory location.
`
int x = 10;
int y = 20;
int* const ptr = &x;
*ptr = 30;      // This is valid, the value of x is now 30.
//ptr = &y;    // This would be an error, because the pointer can't be changed.

`


# Static variables:

- singleton / multiple threading

# Friend
- In C++, the keyword friend is used to give a function or another class access to private and protected members of a class.

  - A friend function: It can be either a member function of another class or a global function. This function can access the private and protected members of the class in which it is declared as a friend.
  - A friend class: When a class is declared as a friend class, all member functions of the friend class can access the private and protected members of the class in which it is declared as a friend.
 `class MyClass {
private:
    int secret = 123;

public:
    friend void revealSecret(MyClass& mc);
};

void revealSecret(MyClass& mc) {
    std::cout << "The secret is: " << mc.secret << std::endl;
}

int main() {
    MyClass my_class;
    revealSecret(my_class);
    return 0;
}`

# RAII:

RAII stands for "Resource Acquisition Is Initialization". It's a common idiom in C++ that ties the life cycle of a resource (which could be memory, a file handle, a lock, or any other resource that is limited and requires explicit management) to the lifetime of an object.

The idea is that you acquire the resource in the constructor of an object, and release it in the destructor. That way, you can never forget to release the resource, because it's done automatically when the object is destroyed. This happens when the object goes out of scope, or when it is explicitly deleted (for dynamically allocated objects).

Here's a simple example:

```
class MyResource {
    int* ptr;
public:
    MyResource() : ptr(new int[100]) {
        // Resource (in this case, memory) is acquired in the constructor
    }

    ~MyResource() {
        delete[] ptr; // Resource is released in the destructor
    }
};
```

# Function and Functor and std::bind

`
#include <iostream>
#include <functional>

int add(int x, int y) {
    return x + y;
}

int main() {
    auto add_five = std::bind(add, 5, std::placeholders::_1);

    std::cout << add_five(3) << std::endl;  // output: 8

    return 0;
}

`
- In this example, we define a function add that takes two arguments and returns their sum. We then create a new function object add_five by calling std::bind with add as the first argument, 5 as the second argument, and the placeholder _1 as the third argument. The placeholder _1 represents the first argument to the new function object, which is the value we want to add to 5. We can then call add_five with a single argument, which will be passed as the second argument to add, resulting in the sum of 5 and the argument passed to add_five.

std::function and functors are both callable objects in C++, but there are some differences between them.

Definition: std::function is a type-erased function wrapper that can be used to store any Callable target, including functions, function pointers, member function pointers, and functors (class objects that overload the operator()). On the other hand, functors are class objects that overload the operator() and can be used as callable objects.

Flexibility: std::function is more flexible than functors, as it can store any callable object, regardless of its type. On the other hand, functors can only store objects of a specific type.

Performance: Functors are typically faster than std::function objects, as they are not type-erased and can be optimized by the compiler. std::function objects, on the other hand, incur some overhead due to the type-erasure and dynamic allocation involved.

Standard Library: std::function is part of the C++ Standard Library and is a type-safe way to store callable objects. Functors are not part of the Standard Library, but are widely used in C++.

Function objects (functors) in C++ are used for several reasons over simple function pointers:
1. Functors can contain state. A functor can have member variables that maintain state between calls. Function pointers are just addresses of functions and hold no state.
2. Functors work with templates. C++ templates can accept functor parameters, but not bare function pointers. This allows for more flexibility and genericity.
3. Functors can be passed as runtime arguments. You can pass a functor to a function to be called, but not a bare C-style function pointer.
4. Functors have a type (their class) which helps with overloaded functions and templates. Function pointers have ambiguous types without elaborate typdefs.
5. Functors can be used in standard algorithms and range-based for loops. These parts of the standard library work with objects that define operator(), but not function pointers.
State:
```
cpp
struct Functor {
  int count = 0;
  void operator()() {
    count++;
  }
};

int main() {
  Functor f;
  f(); // count is 1
  f(); // count is 2
}

```
 Templates:
```
cpp
template<typename F>
void call(F f) { f(); }

void func1() { } 
void (*func2)() = func1;

struct Functor {
  void operator()() { } 
};

int main() {
  call(func1);     // Error, can't pass function
  call(&func1);    // Error, can't pass function pointer
  call(Functor()); // Ok, can pass functor 
}
```
Runtime arguments:
```
cpp
void call(void (*f)()) { f(); }
void call(std::function<void()> f) { f(); }

int main() {
  void func1() { }
  call(func1);           // Error, can't pass function 
  call(&func1);          // Ok, passes pointer
  call(std::function(func1)); // Ok, passes functor
} 

```

# Declarative Programming

C++ supports declarative programming in a few key ways:1. Templates - Templates allow expressing logic in a generic, abstract manner. The specific details for different types are left to the compiler to implement. For example:
```
cpp
template<typename T>
void foo(T a, T b) {
  // ...
}

```
Here we declaratively express the intent (a function that works with two args of any type) and the compiler generates the specific implementations for each T.
2. Standard Library Algorithms - Algorithms like std::sort, std::accumulate, std::find, etc allow expressing logic in a declarative manner. We state what we want to achieve, and the algorithm determines the details. For example:
```
cpp 
std::sort(vec.begin(), vec.end()); 

```
  This is far more declarative than writing out the imperative bubble/select sort algorithms in detail.
3. Lambda Expressions - Lambdas are a concise way to write inline bits of logic. They nicely complement the standard algorithms and allow passing declarative logic to higher order functions. For example:
```
cpp
std::count_if(vec.begin(), vec.end(), [](int i) { return i > 10; });

```
This is more declarative than the imperative-style explicit loop to count elements over 10.
4. Range-based for - The range-based for loop is a simple way to iterate over a range without needing to spell out all the index incrementing details. For example:  
```
cpp
for (int x : vec) { doSomething(x); }

```
  This is slightly more declarative than the index-based for loop:
```
cpp 
for (int i = 0; i < vec.size(); i++) { doSomething(vec[i]); } 

```
5. Parallel Algorithms - The parallel versions of standard algorithms and execution policies determine the async implementation details under the hood. We can simply call:
```
cpp
std::transform(policy, vec1.begin(), vec1.end(), vec2.begin(), multiplies());

std::transform is a C++ standard library algorithm that transforms elements in a range by applying a function to them. It has two main forms:
cpp
// Transform one range 
std::transform(begin1, end1, begin1, func);  

// Transform two ranges at once  
std::transform(begin1, end1, begin2, begin2, func); 
The first form transforms elements in the range [begin1, end1) by applying func to each element and storing the result in the same location.
The second form simultaneously transforms corresponding elements from two ranges [begin1, end1) and [begin2, end2) using func and stores the results in the output range beginning at begin2.
For example:
cpp
std::vector<int> vec {1, 2, 3};

// Add one to each element 
std::transform(vec.begin(), vec.end(), vec.begin(), [](int n) { return n + 1; });
// vec is now {2, 3, 4}

std::vector<double> vec2 {1.1, 2.2, 3.3};  

// Multiply corresponding elements 
std::transform(vec.begin(), vec.end(), vec2.begin(), vec2.begin(), 
  [](int n, double m) { return n * m; });
// vec is still {2, 3, 4}, vec2 is now {2.2, 6.6, 13.2}

```
And the compiler generates the async parallel logic, unbeknownst to the programmer. This is declarative parallelism!So while C++ supports both imperative and declarative styles, there are influences from both procedural and functional paradigms in the language that enable more declarative coding. By leveraging tools like templates, standard algorithms, lambdas, range-based for and parallelism, C++ programs can focus more on desired results rather than step-by-step procedures.

# Functional Programming

Higher-order functions are functions that operate on or return other functions. They are a key aspect of functional programming languages and styles.Some examples of higher-order functions include:- Functions that accept functions as arguments, like std::sort which accepts a comparator function argument.- Functions that return functions, like functions that return lambda expressions or std::function objects.- Functions that satisfy both of the above, accepting functions as input and returning functions as output.Some examples in C++:Function accepting a function:
```
cpp
void doSomething(std::function<void()> func) {
  func(); 
}

```
Here doSomething accepts a function (specifically a std::function) as an argument.Function returning a function:
```
cpp
auto makeFunction() {
  return []() { /* ... */ }; 
}

```
  Here makeFunction returns a lambda expression, which is a function.Function that does both:
```
cpp
template<typename F>
auto higherOrder(F func) {
  return [func]() { 
    func();
  };  
}

```
Here higherOrder accepts a function func and returns a new function (a lambda) that calls func.Some key uses of higher-order functions are:
1. Abstraction - They allow us to abstract over functions and not have to specify concrete function names. This enables more generic logic. 
2. Composition - They enable combining multiple functions together into new functions. The outputs of some functions become the inputs to others.
3. Callbacks - They naturally model callbacks, where one function passes a function to be called at a later point in time.
4. Currying - They can be used to partially apply function arguments one at a time, producing new functions. This is related to function composition.
5. Recursion - Since functions are values that can be passed around, a function can return a recursive reference to itself.
So in summary, higher-order functions enable new ways to compose and abstract logic by treating functions as first-class values that can be passed around and returned from other functions.They are a key part of functional programming in any language, including C++!


Functional languages prefer immutable data for a few key reasons:

1. Simpler reasoning - With immutable data, the value of a variable or data structure can only be assigned once. This means its value is fixed and cannot change unexpectedly due to reassignment in some other part of the code. This makes the code easier to reason about and understand.
2. Concurrency - Immutable data is inherently thread-safe, since its value cannot change after initialization. This means immutable data structures can be safely shared and accessed across threads without synchronization or locking. This makes functional languages with immutable data well suited for concurrent and parallel programming.
3. Recursion - Recursion is a natural fit for processing immutable data structures. Since their values cannot change, a recursive call receives the exact same data structure and can continue drilling down on it. Mutable data requires special handling for recursion to avoid changing data that has yet to be processed. 
4. Persistence - Immutable data structures are naturally persistent, meaning previous versions are still accessible even after "updates" since the data is technically never updated in-place. This enables powerful features like infinite undo or accessing older snapshots.
5. Function purity - Pure functions (meaning no side effects) operate without mutating external state. The only way they can operate on data is by taking in input and returning output. This forces the use of immutable data since the input cannot be updated in-place. Most functional languages aim for pure, side-effect free functions when possible.

# Template
Template Instantiation: When you use this template in your code, such as when you call add(3, 4), the compiler knows that you want to use the add function with int arguments.

Code Generation: The compiler generates concrete code for the specific instantiation you're using. In this case, it generates code for add(int a, int b).

Type Deduction: The compiler uses a process called template argument deduction to determine the actual type or types (in this case, int) to replace the type placeholders (e.g., T) in the template.

Compilation: The generated code is then compiled into machine code or intermediate code, which becomes part of the final executable.

So, the compiler deduces the types based on how you use the template in your code and generates specialized code for each specific combination of template arguments. This is why C++ templates are often referred to as "compile-time generics" because the specialization occurs at compile time based on the context in which the template is used.
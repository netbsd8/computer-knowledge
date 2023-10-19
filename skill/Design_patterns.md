# singleton
`
class Singleton {
  private:
    static Singleton *instance;
    int data;

    // Private constructor to prevent object creation from outside
    Singleton() { data = 0; }

  public:
    static Singleton *getInstance() {
      if (!instance)
        instance = new Singleton();
      return instance;
    }

    int getData() { return data; }
    void setData(int d) { data = d; }
};

// Static member definition
Singleton *Singleton::instance = nullptr;`

# Factory
`
class Shape {
 public:
  virtual void draw() = 0;
};

class Triangle : public Shape {
 public:
  void draw() {
    std::cout << "Drawing Triangle" << std::endl;
  }
};

class Square : public Shape {
 public:
  void draw() {
    std::cout << "Drawing Square" << std::endl;
  }
};

class Rectangle : public Shape {
 public:
  void draw() {
    std::cout << "Drawing Rectangle" << std::endl;
  }
};

class ShapeFactory {
 public:
  static Shape* getShape(std::string type) {
    if (type == "Triangle") {
      return new Triangle();
    } else if (type == "Square") {
      return new Square();
    } else if (type == "Rectangle") {
      return new Rectangle();
    }
    return nullptr;
  }
};

`
- In this example, the factory class ShapeFactory is responsible for creating objects of the concrete classes based on the input type provided. The client code just needs to call the getShape method with the required shape type and the factory class returns the appropriate object. This way, the client code doesn't need to know the details of how the objects are created and the creation process is encapsulated in the factory class.
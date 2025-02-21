abstract class Shape{
    abstract double area();
    abstract double perimeter();
    void display()
    {
        System.out.println("This is a shape.");
    }
}
class Circle extends Shape {
    double radius;
    Circle(double radius) {
        this.radius = radius;
    }
    double area () {
        return Math.PI *radius *radius;

    }
    double perimeter ()
    {
        return 2 * Math.PI * radius;

    }
}
class Rectangle extends Shape{
    double width, height;
    Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
        
    }
    double area() {
        return width *height;

    }
    double perimeter() {
        return 2* ( width + height);
    }
}
public class Area{
    public static void main(String[] args) {
       Shape Circle = new Circle(5);
       Shape Rectangle = new Rectangle(4, 7);
       System.out.println("Circle Area" +Circle.area());
       System.out.println("Circle Perameter" +Circle.perimeter());

       System.out.println("Rectangle Area" +Rectangle.area());
       System.out.println("Rectangle Perameter" +Rectangle.perimeter());
        
    }
}
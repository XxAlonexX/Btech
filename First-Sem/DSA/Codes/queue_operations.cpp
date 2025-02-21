#include <iostream>
#define MAX_SIZE 5
using namespace std;

// Regular Queue
class Queue {
protected:
    int arr[MAX_SIZE];
    int front, rear;

public:
    Queue() : front(-1), rear(-1) {}

    bool isFull() {
        return (rear == MAX_SIZE - 1);
    }

    bool isEmpty() {
        return (front == -1 || front > rear);
    }

    void enqueue(int x) {
        if (isFull()) {
            cout << "Queue Overflow\n";
            return;
        }
        if (front == -1) front = 0;
        arr[++rear] = x;
    }

    int dequeue() {
        if (isEmpty()) {
            cout << "Queue Underflow\n";
            return -1;
        }
        return arr[front++];
    }
};

// Circular Queue
class CircularQueue {
    int arr[MAX_SIZE];
    int front, rear;

public:
    CircularQueue() : front(-1), rear(-1) {}

    bool isFull() {
        return ((front == 0 && rear == MAX_SIZE - 1) || (rear == (front - 1) % (MAX_SIZE - 1)));
    }

    bool isEmpty() {
        return (front == -1);
    }

    void enqueue(int x) {
        if (isFull()) {
            cout << "Queue Overflow\n";
            return;
        }
        if (front == -1) front = 0;
        rear = (rear + 1) % MAX_SIZE;
        arr[rear] = x;
    }

    int dequeue() {
        if (isEmpty()) {
            cout << "Queue Underflow\n";
            return -1;
        }
        int item = arr[front];
        if (front == rear) {
            front = -1;
            rear = -1;
        }
        else {
            front = (front + 1) % MAX_SIZE;
        }
        return item;
    }
};

// Priority Queue
class PriorityQueue {
    struct Item {
        int value;
        int priority;
    };
    Item arr[MAX_SIZE];
    int size;

public:
    PriorityQueue() : size(0) {}

    void enqueue(int value, int priority) {
        if (size >= MAX_SIZE) {
            cout << "Queue Overflow\n";
            return;
        }
        
        // Add new item at the end
        arr[size].value = value;
        arr[size].priority = priority;
        
        // Maintain heap property
        int i = size;
        while (i > 0 && arr[(i - 1) / 2].priority < arr[i].priority) {
            swap(arr[i], arr[(i - 1) / 2]);
            i = (i - 1) / 2;
        }
        size++;
    }

    int dequeue() {
        if (size <= 0) {
            cout << "Queue Underflow\n";
            return -1;
        }
        
        int value = arr[0].value;
        size--;
        if (size > 0) {
            arr[0] = arr[size];
            
            // Maintain heap property
            int i = 0;
            while (true) {
                int largest = i;
                int left = 2 * i + 1;
                int right = 2 * i + 2;
                
                if (left < size && arr[left].priority > arr[largest].priority)
                    largest = left;
                if (right < size && arr[right].priority > arr[largest].priority)
                    largest = right;
                
                if (largest == i) break;
                
                swap(arr[i], arr[largest]);
                i = largest;
            }
        }
        return value;
    }
};

int main() {
    // Test Regular Queue
    cout << "Testing Regular Queue:\n";
    Queue q;
    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);
    cout << q.dequeue() << " dequeued\n";
    
    // Test Circular Queue
    cout << "\nTesting Circular Queue:\n";
    CircularQueue cq;
    cq.enqueue(1);
    cq.enqueue(2);
    cq.enqueue(3);
    cout << cq.dequeue() << " dequeued\n";
    
    // Test Priority Queue
    cout << "\nTesting Priority Queue:\n";
    PriorityQueue pq;
    pq.enqueue(3, 1);
    pq.enqueue(4, 2);
    pq.enqueue(5, 3);
    cout << pq.dequeue() << " dequeued (highest priority)\n";
    
    return 0;
}

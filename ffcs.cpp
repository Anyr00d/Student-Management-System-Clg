#include <iostream>
#include <queue>
using namespace std;
class Student {
public:
    int rollNumber;
    string name;
    bool transport;
    float cgpa;
    int attendance;
    Student(int rollNumber, string name, bool transport, float cgpa, int attendance) {
        this->rollNumber = rollNumber;
        this->name = name;
        this->transport = transport;
        this->cgpa = cgpa;
        this->attendance = attendance;
    }
};
int main() {
    // Create an array of 20 Student objects
    Student students[] = {
        Student(1, "Alice", true, 9.5, 90),
        Student(2, "Bob", true, 9.2, 87),
        Student(3, "Charlie", false, 8.9, 82),
        Student(4, "David", true, 8.9, 95),
        Student(5, "Emily", true, 9.2, 87),
        Student(6, "Frank", true, 9.4, 90),
        Student(7, "Grace", true, 8.9, 85),
        Student(8, "Harry", true, 8.9, 82),
        Student(9, "Isabella", true, 9.2, 95),
        Student(10, "Jack", false, 8.9, 80),
        Student(11, "Lily", true, 8.9, 87),
        Student(12, "Michael", true, 9.2, 85),
        Student(13, "Olivia", false, 8.9, 90),
        Student(14, "Peter", true, 8.9, 92),
        Student(15, "Rachel", false, 8.9, 85),
        Student(16, "Sarah", true, 9.2, 87),
        Student(17, "Thomas", false, 8.9, 80),
        Student(18, "Victoria", true, 8.9, 95),
        Student(19, "William", false, 8.9, 82),
        Student(20, "Zoe", true, 9.2, 87),
    };
    // Define the four queues
    queue<Student> highPriorityQueue;
    queue<Student> mediumPriorityQueue;
    queue<Student> lowPriorityQueue;
    queue<Student> lowestPriorityQueue;
    // Assign students to the appropriate queues
    for (int i = 0; i < 20; i++) {
        Student student = students[i];
        if (student.cgpa > 9.0) {
            highPriorityQueue.push(student); // Prioritize students with CGPA above 9.0 to high priority queue
        } else if (student.cgpa < 9.0 && student.attendance >= 85 && student.transport) {
            mediumPriorityQueue.push(student); // Handle students with attendance 85 or higher and transport status true
        } else if (student.cgpa < 9.0  && !student.transport) {
            lowPriorityQueue.push(student); // Handle students with attendance 85 or higher without transport
        }  else {
            lowestPriorityQueue.push(student); // Assign remaining students to the lowest priority queue
        }
    }
    // Simulate the scheduling algorithm
    while (!highPriorityQueue.empty() || !mediumPriorityQueue.empty() || !lowPriorityQueue.empty() || !lowestPriorityQueue.empty()) {
        // Process high priority queue first
        cout << "Students in first slot:"<<endl;
        while (!highPriorityQueue.empty()) {
            Student student = highPriorityQueue.front();
            highPriorityQueue.pop();
            cout<< student.name << endl;
        }
        // Process medium priority queue next
        cout << "Students in second slot:" <<endl;
        while (!mediumPriorityQueue.empty()) {
            Student student = mediumPriorityQueue.front();
            mediumPriorityQueue.pop();
            cout<< student.name << endl;
        }
        // Process low priority queue next
        cout << "Students in third slot:"<<endl;
        while (!lowPriorityQueue.empty()) {
            Student student = lowPriorityQueue.front();
            lowPriorityQueue.pop();
            cout<< student.name << endl;
        }
        // Process lowest priority queue last
        cout << "Students in last slot:"<<endl; 
        while (!lowestPriorityQueue.empty()) {
            Student student = lowestPriorityQueue.front();
            lowestPriorityQueue.pop();
            cout<< student.name << endl;
        }
    }
}
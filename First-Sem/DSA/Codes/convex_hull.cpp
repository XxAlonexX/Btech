#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Point { int x, y; };
Point p0;

int orientation(Point p, Point q, Point r) {
    int val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y);
    return (val == 0) ? 0 : (val > 0) ? 1 : 2;
}

bool compare(Point p1, Point p2) {
    int o = orientation(p0, p1, p2);
    if (o == 0) return (p1.x < p2.x);
    return (o == 2);
}

void convexHull(vector<Point> points) {
    sort(points.begin(), points.end(), [](Point a, Point b) { return a.y < b.y; });
    p0 = points[0];
    sort(points.begin() + 1, points.end(), compare);
    cout << "Convex Hull Points: ";
    for (auto &p : points) cout << "(" << p.x << ", " << p.y << ") ";
}

int main() {
    vector<Point> points = {{0, 3}, {2, 2}, {1, 1}, {2, 1}, {3, 0}};
    convexHull(points);
    return 0;
}

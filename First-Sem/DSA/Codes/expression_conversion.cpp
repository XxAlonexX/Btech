#include <iostream>
#include <stack>
#include <string>
using namespace std;

int precedence(char op) {
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    if (op == '^') return 3;
    return -1;
}

string infixToPostfix(string infix) {
    stack<char> st;
    string postfix;
    
    for (char c : infix) {
        if (isalnum(c)) {
            postfix += c;
        }
        else if (c == '(') {
            st.push(c);
        }
        else if (c == ')') {
            while (!st.empty() && st.top() != '(') {
                postfix += st.top();
                st.pop();
            }
            if (!st.empty()) st.pop();
        }
        else {
            while (!st.empty() && precedence(st.top()) >= precedence(c)) {
                postfix += st.top();
                st.pop();
            }
            st.push(c);
        }
    }
    
    while (!st.empty()) {
        postfix += st.top();
        st.pop();
    }
    
    return postfix;
}

int evaluatePostfix(string postfix) {
    stack<int> st;
    
    for (char c : postfix) {
        if (isdigit(c)) {
            st.push(c - '0');
        }
        else {
            int val1 = st.top(); st.pop();
            int val2 = st.top(); st.pop();
            switch (c) {
                case '+': st.push(val2 + val1); break;
                case '-': st.push(val2 - val1); break;
                case '*': st.push(val2 * val1); break;
                case '/': st.push(val2 / val1); break;
            }
        }
    }
    return st.top();
}

int main() {
    string infix = "a+b*(c^d-e)^(f+g*h)-i";
    cout << "Infix: " << infix << endl;
    cout << "Postfix: " << infixToPostfix(infix) << endl;
    
    string postfix = "231*+9-";
    cout << "\nEvaluating postfix expression: " << postfix << endl;
    cout << "Result: " << evaluatePostfix(postfix) << endl;
    return 0;
}

/*
#include <iostream>
#include <cmath>
#include <map>
#include <functional>
#include <vector>

using namespace std;

// Функція для task_1
double cosmic_formula(double x, double y) {
    double top_formula = 1 + pow(sin(x + y), 2);
    double bottom_formula = 2 + abs((x - 2 * x) / (1 + pow(x, 2) * pow(y, 2)));
    return top_formula / bottom_formula + x;
}

// Функція task_1
string task_1(vector<double> variables) {
    double x = (variables.size() > 0) ? variables[0] : 1;
    double y = (variables.size() > 1) ? variables[1] : 2;
    
    double result = cosmic_formula(x, y);
    return "Task: 1 + sin(x + y)^2 / (2 + abs((x - 2x)/(1 + x^2*y^2))) + x\n" + 
           "Input: x = " + to_string(x) + ", y = " + to_string(y) + "\n" +
           "Result: " + to_string(result);
}

// Функція task_3 (π * π)
string task_3(vector<double>) {
    return "Task: π * π\nInput: π = 3.141592...\nResult: " + to_string(M_PI * M_PI);
}

// Функція task_4 (π^π)
string task_4(vector<double>) {
    return "Task: π^π\nInput: π = 3.141592...\nResult: " + to_string(pow(M_PI, M_PI));
}

// Функція task_11 (сума ряду)
string task_11(vector<double> variables) {
    double a = (variables.size() > 0) ? variables[0] : 2;
    int n = (variables.size() > 1) ? int(variables[1]) : 3;
    
    double result = 0;
    for (int i = 1; i <= n; i++) {
        result += 1 / pow(a, pow(2, i));
    }

    return "Task: sum(1/a + 1/a^2 + ... + 1/a^(2^n))\n" +
           "Input: a = " + to_string(a) + ", n = " + to_string(n) + "\n" +
           "Result: " + to_string(result);
}

// Виконання задач через std::map
map<string, function<string(vector<double>)>> TASKS = {
    {"1", task_1},
    {"3", task_3},
    {"4", task_4},
    {"11", task_11}
};

// Функція для виконання задач
string execute_task(const string& task_number, vector<double> variables) {
    if (TASKS.find(task_number) == TASKS.end()) {
        return "Unknown Task";
    }

    return TASKS[task_number](variables);
}

int main() {
    string task_number;
    vector<double> inputs;

    while (true) {
        cout << "Enter task number (1, 3, 4, 11) or 'exit': ";
        cin >> task_number;
        if (task_number == "exit") break;

        inputs.clear();
        if (TASKS.find(task_number) != TASKS.end()) {
            int required_vars = (task_number == "1" || task_number == "11") ? 2 : 0;
            for (int i = 0; i < required_vars; i++) {
                double val;
                cout << "Enter value " << i + 1 << ": ";
                cin >> val;
                inputs.push_back(val);
            }
        }

        cout << execute_task(task_number, inputs) << endl << endl;
    }

    return 0;
}
*/

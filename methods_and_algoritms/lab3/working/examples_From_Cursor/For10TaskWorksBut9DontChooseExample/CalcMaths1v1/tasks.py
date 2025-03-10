import math
import numpy as np

"""
TASK_DEFINITIONS = {
    "1": ("task_1", 2, float, "Example: 
    x = 1, y = 2
    "),
    "2": ("task_2", 2, float, "Example: 
    x = 3, y = 5
    "),
    "6.a": ("task_6_a", 1, str, "Example: 
    Hello world! How are you!
    "),
    "18": ("task_18", 1, str, "Example: 
    Hello world level deed stats
    "),


}
"""

class TaskManager:
    def __init__(self):
        self.tasks = {
            "6.a": (self.task_6_a, 1, str), 
            "18": (self.task_18, 1, str),
            "det_of_matrix": (self.task_determinant_of_matrix, 1, float),
            "10": (self.task_10, 1, str)
        }
        
        # Predefined examples for systems of linear equations
        self.linear_system_examples = {
            "Example 1 (4 variables)": """4x₁ + x₂ - x₄ = -9;
x₁ - 3x₂ + 4x₃ = -7;
3x₂ - 2x₃ + 4x₄ = 12;
x₁ + 2x₂ - x₃ - 3x₄ = 0;""",
            
            "Example 2 (3 variables)": """2x₁ + x₂ + x₃ = 8;
-3x₁ + 4x₂ + 2x₃ = -2;
x₁ - x₂ + 6x₃ = 3;""",
            
            "Example 3 (2 variables)": """3x₁ + 2x₂ = 7;
5x₁ - 2x₂ = 3;""",
            
            "Example 4 (No solution)": """x₁ + x₂ = 5;
2x₁ + 2x₂ = 8;""",
            
            "Example 5 (Infinite solutions)": """x₁ + 2x₂ = 4;
2x₁ + 4x₂ = 8;"""
        }
        
        # Predefined examples for matrix determinants
        self.matrix_examples = {
            "Example 1 (3x3)": np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
            "Example 2 (3x3)": np.array([[4, 2, 1], [0, 5, 3], [2, 1, 7]]),
            "Example 3 (2x2)": np.array([[3, 4], [5, 6]]),
            "Example 4 (4x4)": np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
        }

    def execute_task(self, task_number, variables):
        if task_number not in self.tasks:
            return "Unknown Task"
        
        task_function, required_vars, data_type = self.tasks[task_number]
        if len(variables) < required_vars:
            remaining = required_vars - len(variables)
            return f"Waiting for {remaining} more input(s)... (Enter {remaining} value{'s' if remaining > 1 else ''})"
        
        try:
            converted_variables = [data_type(var) for var in variables]
            description, input_data, result = task_function(converted_variables)
            return f"{description}\nInput Data: {input_data}\nResult: {result}"
        except Exception as e:
            return f"Error during calculation: {str(e)}"
    
    def task_determinant_of_matrix(self, variables):
        # If input is a string representation of a matrix, try to parse it
        if isinstance(variables[0], str):
            try:
                # Check if it's one of our predefined examples
                for example_name, example_matrix in self.matrix_examples.items():
                    if example_name in variables[0]:
                        matrix = example_matrix
                        break
                else:
                    # Try to parse as a string representation of a matrix
                    matrix_str = variables[0].replace('[', '').replace(']', '')
                    rows = matrix_str.split('\n')
                    matrix = []
                    for row in rows:
                        if row.strip():
                            matrix.append([float(x) for x in row.split() if x.strip()])
                    matrix = np.array(matrix)
            except:
                # If parsing fails, use a default example
                matrix = self.matrix_examples["Example 1 (3x3)"]
        else:
            # Use a default example
            matrix = self.matrix_examples["Example 1 (3x3)"]
        
        try:
            determinant = self.calc_determinant_of_matrix(matrix)
            return "Determinant of matrix", f"Matrix:\n{matrix}", f"{determinant:.6f}"
        except Exception as e:
            return "Determinant of matrix", f"Matrix:\n{matrix}", f"Error: {str(e)}"
    
    def calc_determinant_of_matrix(self, matrix):
        return np.linalg.det(matrix)

    def task_6_a(self, variables):
        text = variables[0] if variables else "Hello world! How are you!"
        
        # Знаходимо індекс першого знаку оклику
        exclamation_index = text.find('!')
        if exclamation_index == -1:
            return "No exclamation mark found in the string", f"Input: {text}", 0
        
        # Підраховуємо кількість пробілів до першого знаку оклику
        spaces_count = text[:exclamation_index].count(' ')
        
        return "Count spaces before first exclamation mark", f"Input: {text}", spaces_count

    
    def text_split(self, text):
        return [word for word in text.split() if word]

    def task_18(self, variables):
        text = variables[0] if variables else "Hello world level deed stats"
        
        # Отримуємо список слів через допоміжну функцію
        words = self.text_split(text)
        
        # Знаходимо слова, де перший і останній символи співпадають
        matching_words = [word for word in words if word and word[0].lower() == word[-1].lower()]
        
        # Формуємо результат
        result = {
            "total_words": len(words),
            "matching_words": matching_words,
            "matching_count": len(matching_words)
        }
        
        return ("Count words where first and last characters match", 
                f"Input: {text}", 
                f"Matching words: {matching_words}\nCount: {len(matching_words)}")
    
    def task_10(self, variables):
        # Get the system of equations from input or use default
        equations_text = variables[0] if variables else self.linear_system_examples["Example 1 (4 variables)"]
        
        try:
            # Parse the system of equations
            lines = [line.strip() for line in equations_text.split(';') if line.strip()]
            
            # Determine the number of variables from the equations
            max_var_index = 0
            for line in lines:
                for i in range(1, 10):  # Check for variables x₁ through x₉
                    if f'x{i}' in line.replace(f'x₁', f'x1').replace(f'x₂', f'x2').replace(f'x₃', f'x3').replace(f'x₄', f'x4'):
                        max_var_index = max(max_var_index, i)
                    if f'x₁' in line or f'x1' in line:
                        max_var_index = max(max_var_index, 1)
                    if f'x₂' in line or f'x2' in line:
                        max_var_index = max(max_var_index, 2)
                    if f'x₃' in line or f'x3' in line:
                        max_var_index = max(max_var_index, 3)
                    if f'x₄' in line or f'x4' in line:
                        max_var_index = max(max_var_index, 4)
                    if f'x₅' in line or f'x5' in line:
                        max_var_index = max(max_var_index, 5)
                    if f'x₆' in line or f'x6' in line:
                        max_var_index = max(max_var_index, 6)
                    if f'x₇' in line or f'x7' in line:
                        max_var_index = max(max_var_index, 7)
                    if f'x₈' in line or f'x8' in line:
                        max_var_index = max(max_var_index, 8)
                    if f'x₉' in line or f'x9' in line:
                        max_var_index = max(max_var_index, 9)
            
            n = max_var_index  # Number of variables
            if n == 0:
                return ("System of Linear Equations", 
                        f"System:\n{equations_text}", 
                        "Error: No variables detected in the system")
            
            # Initialize coefficient matrix A and constants vector b
            A = np.zeros((len(lines), n))
            b = np.zeros(len(lines))
            
            # Parse each equation
            for i, line in enumerate(lines):
                if i >= len(lines):
                    break
                    
                # Remove any equals sign and split the equation
                if '=' in line:
                    left_side, right_side = line.split('=')
                else:
                    continue
                
                # Parse the right side (constant term)
                b[i] = float(right_side.strip())
                
                # Parse the left side (coefficients)
                terms = left_side
                # Replace subscript numbers with regular numbers
                for j in range(1, 10):
                    terms = terms.replace(f'x₁', 'x1').replace(f'x₂', 'x2').replace(f'x₃', 'x3').replace(f'x₄', 'x4')
                    terms = terms.replace(f'x₅', 'x5').replace(f'x₆', 'x6').replace(f'x₇', 'x7').replace(f'x₈', 'x8').replace(f'x₉', 'x9')
                
                # Add spaces around operators for easier parsing
                terms = terms.replace('+', ' + ').replace('-', ' - ')
                # Add spaces around variable names
                for j in range(1, 10):
                    terms = terms.replace(f'x{j}', f' x{j} ')
                
                terms = terms.split()
                
                coef = 0
                var_idx = -1
                sign = 1
                
                for term in terms:
                    if 'x' in term:
                        var_idx = int(term.replace('x', '')) - 1
                        if coef == 0:  # If no coefficient was specified, it's 1
                            coef = sign
                        A[i, var_idx] = coef
                        coef = 0
                        sign = 1
                    elif term == '+':
                        sign = 1
                    elif term == '-':
                        sign = -1
                    else:
                        try:
                            coef = float(term) * sign
                            sign = 1
                        except ValueError:
                            pass
            
            # Check if the system is solvable
            if len(lines) < n:
                return ("System of Linear Equations", 
                        f"System:\n{equations_text}", 
                        "The system is underdetermined (more variables than equations)")
            
            # Try to solve the system
            try:
                # For square systems, use direct solve
                if len(lines) == n:
                    solution = np.linalg.solve(A, b)
                    solution_text = ", ".join([f"x{i+1} = {solution[i]:.4f}" for i in range(n)])
                    return ("System of Linear Equations", 
                            f"System:\n{equations_text}", 
                            f"Solution:\n{solution_text}")
                # For overdetermined systems, use least squares
                else:
                    solution, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)
                    solution_text = ", ".join([f"x{i+1} = {solution[i]:.4f}" for i in range(n)])
                    return ("System of Linear Equations", 
                            f"System:\n{equations_text}", 
                            f"Least squares solution:\n{solution_text}\nResidual: {residuals[0] if len(residuals) > 0 else 0:.6f}")
            
            except np.linalg.LinAlgError:
                # Check if the system has infinite solutions
                augmented = np.column_stack((A, b))
                rank_A = np.linalg.matrix_rank(A)
                rank_augmented = np.linalg.matrix_rank(augmented)
                
                if rank_A == rank_augmented and rank_A < n:
                    return ("System of Linear Equations", 
                            f"System:\n{equations_text}", 
                            "The system has infinitely many solutions")
                else:
                    return ("System of Linear Equations", 
                            f"System:\n{equations_text}", 
                            "The system has no solution")
        
        except Exception as e:
            return ("System of Linear Equations", 
                    f"System:\n{equations_text}", 
                    f"Error solving the system: {str(e)}")
    
    def get_examples_for_task(self, task_number):
        """Return predefined examples for a specific task"""
        if task_number == "10":
            return self.linear_system_examples
        elif task_number == "det_of_matrix":
            return self.matrix_examples
        else:
            return {}
    
    

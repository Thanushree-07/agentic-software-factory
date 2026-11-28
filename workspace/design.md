**files**  
1. `calculator.py` – main application logic and user interface.  
2. `operations.py` – pure functions that perform arithmetic and validation.  
3. `utils.py` – helper functions for input parsing and formatting.

---

**task functions**

| Module | Function | Inputs | Return value | Description & invalid‑input handling |
|--------|----------|--------|--------------|--------------------------------------|
| `operations.py` | `add(a: float, b: float) -> float` | two numbers | sum | Returns `a + b`. No special error handling – called only after validation. |
| | `subtract(a: float, b: float) -> float` | two numbers | difference | Returns `a - b`. |
| | `multiply(a: float, b: float) -> float` | two numbers | product | Returns `a * b`. |
| | `divide(a: float, b: float) -> float` | two numbers | quotient | If `b == 0` raises `ZeroDivisionError`; otherwise returns `a / b`. |
| | `calculate(a: float, b: float, op: str) -> float` | two numbers, operator | result | Dispatches to the appropriate operation; if `op` not in `{'+' , '-', '*', '/'}` raises `ValueError`. |
| `utils.py` | `parse_number(s: str) -> float` | string | numeric value | Tries `float(s)`; on failure raises `ValueError` with message “Invalid number: {s}”. |
| | `format_result(value: float) -> str` | numeric | formatted string | Returns `"{:.2f}".format(value)` if value has fractional part, else `str(int(value))`. |
| | `is_exit_command(s: str) -> bool` | string | bool | Returns `True` if `s.lower()` in `{'q', 'quit', 'exit'}`. |
| `calculator.py` | `prompt_user() -> tuple[float, float, str]` | none | `(a, b, op)` | Repeatedly asks for first number, second number, and operator, using `utils.parse_number` and validating operator. On invalid input prints error and re‑prompts. |
| | `main() -> None` | none | None | Loop: call `prompt_user`, call `operations.calculate`, format and display result. Handles `ZeroDivisionError` and `ValueError` by printing appropriate error messages. Exits when `is_exit_command` is true, printing “Goodbye!”. |

---

**data storage**  
No persistent storage is required. All data (operands, operator, result) are kept in local variables within the function calls. No external files or databases are used.

---

**how to run**  
1. Open a terminal.  
2. Navigate to the directory containing the three files.  
3. Execute:  

```bash
python calculator.py
```

4. The program will prompt:

```
Enter first number (or 'q' to quit): 
```

5. Provide input as requested. To exit, type `q`, `quit`, or `exit` at any prompt. The program will terminate with “Goodbye!”.
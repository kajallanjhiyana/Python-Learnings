## Day 1 Practice Question: "Grocery Bill Calculator"

**Scenario:** You're building a simple program that calculates a customer's grocery bill, applies a discount if they qualify, and prints a final formatted receipt.

**Requirements (this is what ties everything together):**

1. **Get input from the user** (`input()`) for:
   - Item name (string)
   - Price per item (you'll receive this as text — you must convert it to a `float`)
   - Quantity (you'll receive this as text — convert it to an `int`)

2. **Write a function `calculate_total(price, quantity)`** that:
   - Multiplies price × quantity (arithmetic operator)
   - Returns the total as a float

3. **Write a function `is_eligible_for_discount(total, quantity)`** that:
   - Returns `True` if total is greater than 500 **and** quantity is greater than 2 (comparison + logical operators)
   - Otherwise returns `False` (this return value is a `bool`)

4. **Write a function `apply_discount(total, eligible)`** that:
   - Takes the total and the `bool` from step 3
   - If `eligible` is `True`, reduce total by 10% (arithmetic again)
   - Return the final total

5. **Write a function `display_receipt(name, quantity, total, eligible)`** that:
   - Prints a nicely formatted receipt using an **f-string**, something like:
     ```
     Receipt: 3 x Rice — Total: ₹450.00 (Discount applied: False)
     ```

6. **In your main code**, call these functions *in sequence*, passing each function's output into the next one — this is the "linking" part: `calculate_total()`'s return value feeds into `is_eligible_for_discount()`, whose return value feeds into `apply_discount()`, whose return value feeds into `display_receipt()`.

**Concepts this forces you to touch:** variables, data types (str/int/float/bool), type conversion (`int()`/`float()`), arithmetic operators, comparison operators, logical operators (`and`), `input()`/`print()`, f-strings, and function definition + return values + passing data between functions.

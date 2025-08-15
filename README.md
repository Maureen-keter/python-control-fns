# **Discount Calculator**

## **Overview**

This program calculates the final price of an item after applying a discount. It uses a custom Python function, `calculate_discount(price, discount_percent)`, to determine whether a discount should be applied and compute the final amount.

The program meets the following criteria:

* Accepts user input for the original price and discount percentage.
* Applies the discount only if it is **20% or higher**.
* Returns and displays the final price (discounted or original).

---

## **Function Description**

### `calculate_discount(price, discount_percent)`

**Parameters:**

* `price` *(float)*: The original price of the item.
* `discount_percent` *(float)*: The discount percentage to apply.

**Logic:**

1. If `discount_percent >= 20`, the function applies the discount:

   $$
   \text{final\_price} = \text{price} - (\text{price} \times \frac{\text{discount\_percent}}{100})
   $$
2. If the discount percentage is less than 20, the function returns the original price.

**Returns:**

* The final price *(float)* after applying the discount if applicable.

---

## **How the Program Works**

1. Prompts the user to input:

   * The original price.
   * The discount percentage.
2. Calls the `calculate_discount()` function to process the inputs.
3. Displays the final calculated price.

---

## **Example Run**

**Case 1 – Discount ≥ 20%**

```
Enter the original price: 1000
Enter the discount percentage: 25
The final price after discount is: 750.0
```

**Case 2 – Discount < 20%**

```
Enter the original price: 1000
Enter the discount percentage: 10
No discount applied. The price remains: 1000.0
```

## **Requirements**

* **Python Version:** Python 3.x

---

## **Author**

Maureen Chelangat.

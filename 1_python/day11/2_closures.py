def create_discount_calculator(discount_percentage):
    if discount_percentage <= 0 or discount_percentage > 99.99:
        raise ValueError(f"Invalid Discount Rate: {discount_percentage}")

    def calculate_discount(original_price):
        if original_price <= 0:
            raise ValueError(f"Invalid Item Price: {original_price}")
        discount_amount = (discount_percentage * original_price)/100
        final_amount = original_price - discount_amount

        return discount_amount, final_amount

    return calculate_discount


if __name__ == "__main__":
    premium_discount_calc = create_discount_calculator(20)
    premium_discount_amount, premium_discount = premium_discount_calc(5000)
    print(f"Applied Premium Discount, Discount: {premium_discount_amount}, Final Price: {premium_discount}")


    regular_discount_calc = create_discount_calculator(10)
    regular_discount_amount, regular_discount = regular_discount_calc(5000)
    print(f"Applied Regular Discount, Discount: {regular_discount_amount}, Final Price: {regular_discount}")


    new_discount_calc = create_discount_calculator(5)
    new_discount_amount, new_discount = new_discount_calc(5000)
    print(f"Applied New Discount, Discount: {new_discount_amount}, Final Price: {new_discount}")

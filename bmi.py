def collect_input(metric: str, unit:str) -> float:
    prompt = f"Provide your {metric} in {unit}:\n"

    while True:
        try:
            return float(input(prompt))
        except (ValueError):
            print("Input should be a float value.")
    

def calculate_bmi(weight: float, height: float) -> float:
    return round(weight / (height / 100)**2, 2)


def classify_bmi(bmi: float) -> str:
    categories = [
        (18.5, "underweight"),
        (25.0, "correct weight"),
        (30.0, "overweight"),
        (float("inf"), "obesity"),
    ]

    return next(label for limit, label in categories if bmi < limit)


def display_msg(bmi:float, category: str) -> None:
    print(f"Your BMI = {bmi}.\nThis classifies as: {category}.")


def main() -> None:
    user_weight: float = collect_input("weight", "kg")
    user_height: float = collect_input("height", "cm")

    bmi: float = calculate_bmi(user_weight, user_height)

    category = classify_bmi(bmi)

    display_msg(bmi, category)


if __name__ == "__main__":
    main()
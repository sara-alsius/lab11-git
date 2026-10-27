MONTHLY_INCOME = 1850.00
RENT = 750.00
DAYS_IN_MONTH = 30


def remaining_after_rent(income: float, rent: float) -> float:
    return income - rent


def daily_allowance(remaining: float, days: int) -> float:
    return remaining / days


def main() -> None:
    remaining = remaining_after_rent(MONTHLY_INCOME, RENT)
    print(f"After rent: {remaining:.2f}")
    print(f"Per day:    {daily_allowance(remaining, DAYS_IN_MONTH):.2f}")


if __name__ == "__main__":
    main()

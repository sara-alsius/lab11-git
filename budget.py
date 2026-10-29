MONTHLY_INCOME = 1850.00
RENT = 780.00
DAYS_IN_MONTH = 31
SAVINGS_RATE = 0.10


def remaining_after_rent(income: float, rent: float) -> float:
    return income - rent


def daily_allowance(remaining: float, days: int) -> float:
    return remaining / days


def main() -> None:
    remaining = remaining_after_rent(MONTHLY_INCOME, RENT)
    print(f"After rent: {remaining:.2f}")
    print(f"Per day:    {daily_allowance(remaining, DAYS_IN_MONTH):.2f}")
    print(f"Save:        {remaining * SAVINGS_RATE:.2f}")


if __name__ == "__main__":
    main()

def compute_intrest():
    principal = int(input("What is the principle "))
    interest_rate = int(input("what is the interest rate ")) / 100
    years = int(input("how many years are you investing for "))
    final_amount = principal * (1 + interest_rate) ** years
    print(f"final amount earned ${final_amount:,.2f}")
if __name__ == "__main__":
    compute_intrest()
n=int(input("Enter a number: "));odd_num=[i for i in range(n) if i%2!=0];print(f"Odd numbers below {n}: {odd_num}");e_num=[i for i in range(n) if i%2==0];print(f"even numbers below {n}: {e_num}")
fruits=input("Enter fruit names separated by commas: ").split(',');capitalized_fruits=[f"{f.strip()[0].upper()}{f.strip()[1:]}" for f in fruits];print(f"Updated fruit list: {capitalized_fruits}")

def main(n: int) -> dict:
    return {
        "Q1": hex(n & 0xFF),
        "Q2": hex((n >> 8) & 0x3),
        "Q3": hex((n >> 10) & 0x7F),
        "Q4": hex((n >> 17) & 0x7),
    }

if __name__ == "__main__":
    test_cases = [292308, 359343, 447023, 228934]
    for case in test_cases:
        print(f"main({case}) ->", main(case))
        

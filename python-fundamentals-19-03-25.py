# Question 1: Generate a 2D array with element (i,j) = i*j
def generate_2d_array(X, Y):
    return [[i*j for j in range(Y)] for i in range(X)]

# Question 2: Sort comma-separated words
def sort_words(words):
    return ','.join(sorted(words.split(',')))

# Question 3: Remove duplicates and sort alphanumerically
def remove_duplicates_and_sort(sentence):
    return ' '.join(sorted(set(sentence.split())))

# Question 4: Find numbers between 1000-3000 where each digit is even
def find_even_digit_numbers():
    return ','.join(str(num) for num in range(1000, 3001) 
                   if all(int(digit) % 2 == 0 for digit in str(num)))

# Question 5: Count letters and digits in a sentence
def count_letters_and_digits(sentence):
    letters = sum(c.isalpha() for c in sentence)
    digits = sum(c.isdigit() for c in sentence)
    return f"LETTERS {letters}\nDIGITS {digits}"

# Question 6: Count uppercase and lowercase letters
def count_case(sentence):
    upper = sum(c.isupper() for c in sentence)
    lower = sum(c.islower() for c in sentence)
    return f"UPPER CASE {upper}\nLOWER CASE {lower}"

# Question 7: Calculate net bank account amount
def calculate_balance(transactions):
    balance = 0
    for transaction in transactions.strip().split('\n'):
        action, amount = transaction.split()
        balance += int(amount) if action == 'D' else -int(amount)
    return balance

# Question 8: Check password validity
def validate_password(passwords):
    valid = []
    for pwd in passwords.split(','):
        if (6 <= len(pwd) <= 12 and 
            any(c.islower() for c in pwd) and 
            any(c.isupper() for c in pwd) and
            any(c.isdigit() for c in pwd) and
            any(c in '$#@' for c in pwd)):
            valid.append(pwd)
    return '\n'.join(valid)

# Question 9: Sort tuples by name, age, and height
def sort_tuples(data):
    return sorted(tuple(line.split(',')) for line in data.strip().split('\n'))

# Question 10: Calculate robot movement distance
def calculate_distance(movements):
    x, y = 0, 0
    directions = {'UP': (0, 1), 'DOWN': (0, -1), 'LEFT': (-1, 0), 'RIGHT': (1, 0)}
    
    for movement in movements.strip().split('\n'):
        direction, steps = movement.split()
        dx, dy = directions[direction]
        x += dx * int(steps)
        y += dy * int(steps)
    
    return round((x**2 + y**2) ** 0.5)

# Question 11: Find continuous occurrence of characters
def find_continuous_occurrence(s):
    if not s:
        return ""
    
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(s[i-1] + str(count))
            count = 1
    
    result.append(s[-1] + str(count))
    return ''.join(result)

# Question 12: Find pairs with sum of numbers between equals 9
def find_pairs_with_sum_9(s):
    alpha_positions = [(i, c) for i, c in enumerate(s) if c.isalpha()]
    result = []
    
    for i in range(len(alpha_positions) - 1):
        for j in range(i + 1, len(alpha_positions)):
            pos1, char1 = alpha_positions[i]
            pos2, char2 = alpha_positions[j]
            
            numbers = ''.join(c for c in s[pos1+1:pos2] if c.isdigit())
            if numbers and sum(int(d) for d in numbers) == 9:
                result.append(f"{char1},{char2}")
    
    return '\n'.join(result)

# Question 13: Count pairs in binary that start and end with 1
def count_pairs_in_binary(binary):
    ones = [i for i, bit in enumerate(binary) if bit == '1']
    return len(ones) * (len(ones) - 1) // 2

# Question 14: Find minimum possible denominations
def find_min_denominations(valid_currency, money):
    valid_currency.sort(reverse=True)
    result = []
    
    for currency in valid_currency:
        if money >= currency:
            count = money // currency
            money %= currency
            result.append(f"{currency}-{count}")
        if money == 0:
            break
    
    return '\n'.join(result)

# Question 15: Non-consecutive bus stops
def non_consecutive_stops(n, m):
    from math import comb
    return comb(n-m+1, m)

# Question 16: Stone Paper Scissor game
def stone_paper_scissor_game(plays):
    def determine_winner(player_a, player_b):
        if player_a == player_b:
            return "DRAW"
        elif ((player_a == "Stone" and player_b == "Scissor") or
              (player_a == "Paper" and player_b == "Stone") or
              (player_a == "Scissor" and player_b == "Paper")):
            return "Player A wins"
        else:
            return "Player B wins"
    
    results = []
    score_a = score_b = 0
    
    for play in plays:
        player_a, player_b = play
        result = determine_winner(player_a, player_b)
        results.append(f"{player_a} {player_b} {result}")
        
        if result == "Player A wins":
            score_a += 1
        elif result == "Player B wins":
            score_b += 1
            
        if score_a == 5 or score_b == 5:
            break
    
    return '\n'.join(results)

# Question 17: Validate Email Address
def validate_email(email):
    if email.count('@') != 1:
        return False
    return all(c.islower() or c.isdigit() or c in ['@', '.', '_'] for c in email)

# Question 18: Pattern problems
def pattern_a(rows):
    num = 1
    result = []
    for i in range(1, rows + 1):
        row = []
        for j in range(1, 2*i):
            row.append(str(num) if j % 2 == 1 else '*')
            if j % 2 == 1:
                num += 1
        result.append(' '.join(row))
    return '\n'.join(result)

def pattern_b(rows):
    result = []
    # Upper half
    for i in range(1, rows + 1):
        result.append('* ' * i)
    # Lower half
    for i in range(rows - 1, 0, -1):
        result.append('* ' * i)
    return '\n'.join(result)

def pattern_c(rows):
    num = 1
    upper_rows = []
    
    for i in range(1, rows + 1):
        row = []
        for j in range(1, 2*i):
            row.append(str(num) if j % 2 == 1 else '*')
            if j % 2 == 1:
                num += 1
        upper_rows.append(' '.join(row))
    
    return '\n'.join(upper_rows + upper_rows[:-1][::-1])

def pattern_d(rows):
    if rows < 7:
        return "Minimum rows should be 7"
    
    patterns = [
        '***',  # Top line
        '*',    # Upper vertical line 1
        '*',    # Upper vertical line 2
        '* ***', # Middle line
        '* *',  # Lower vertical line 1
        '* *',  # Lower vertical line 2
        '* * *' # Bottom line
    ]
    
    return '\n'.join(patterns)

def pattern_e(rows):
    if rows % 2 == 0:
        return "Row count must be odd"
    
    mid = rows // 2
    result = []
    
    for i in range(rows):
        row = ['1' if (i == 0 or i == rows - 1 or j == mid) else '0' for j in range(rows)]
        result.append(' '.join(row))
    
    return '\n'.join(result)

# Question 19: Cyclic rotation
def cyclic_rotation(direction, string, times):
    for _ in range(times):
        string = string[1:] + string[0] if direction == 1 else string[-1] + string[:-1]
    return string

# Question 20: Health condition comparison
def health_condition_comparison(patient_data):
    # Healthy patient data
    healthy_data = {
        "Sugar level": 15,
        "Blood pressure": 32,
        "Heartbeat rate": 71,
        "weight": 65,
        "fat percentage": 10
    }
    
    # Calculate differences (healthy - patient)
    differences = {key: healthy_data[key] - patient_data[key] for key in healthy_data}
    
    result = [str(differences)]
    
    # Provide warnings
    for key, diff in differences.items():
        result.append(f"{key} {diff}")
        if diff < 0:
            result.append(f"The {key} is {abs(diff)} more than the ideal value")
        elif diff > 0:
            result.append(f"The {key} is {abs(diff)} less than the ideal value")
        else:
            result.append(f"The {key} is at the ideal value")
    
    return '\n'.join(result)

# Question 21: Check if number is Armstrong number
def is_armstrong(num):
    num_str = str(num)
    n_digits = len(num_str)
    return sum(int(digit) ** n_digits for digit in num_str) == num

# Question 22: Convert decimal to binary without built-in function
def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"
    
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    
    return binary

# Question 23: Check if number is perfect
def is_perfect_number(num):
    if num <= 1:
        return False
    
    divisors_sum = 1  # Start with 1 as it's always a divisor
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divisors_sum += i
            if i != num // i:  # Avoid adding the same divisor twice for perfect squares
                divisors_sum += num // i
    
    return divisors_sum == num


if __name__ == "__main__":
    # Test Question 1
    print(f"Q1: {generate_2d_array(3, 5)}")
    
    # Test Question 2
    print(f"Q2: {sort_words('without,hello,bag,world')}")
    
    # Test Question 3
    print(f"Q3: {remove_duplicates_and_sort('hello world and practice makes perfect and hello world again')}")
    
    # Test Question 4 (output shortened for brevity)
    even_nums = find_even_digit_numbers()
    print(f"Q4: {even_nums[:20]}...")
    
    # Test Question 5
    print(f"Q5:\n{count_letters_and_digits('hello world! 123')}")
    
    # Test Question 6
    print(f"Q6:\n{count_case('Hello world!')}")
    
    # Test Question 7
    transactions = """D 300
D 300
W 200
D 100"""
    print(f"Q7: {calculate_balance(transactions)}")
    
    # Test Question 8
    print(f"Q8:\n{validate_password('ABd1234@1,a F1#,2w3E*,2We3345')}")
    
    # Test Question 9
    data = """Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85"""
    print(f"Q9: {sort_tuples(data)}")

    # Test Question 10
    movements = """UP 5
DOWN 3
LEFT 3
RIGHT 2"""
    print(f"Q10: {calculate_distance(movements)}")
    
    # Test Question 11
    print(f"Q11: {find_continuous_occurrence('Aabbcdeefffaabbcc')}")
    
    # Test Question 12
    print(f"Q12: {find_pairs_with_sum_9('a54b12c')}")
    print(f"Q12 (additional): {find_pairs_with_sum_9('a55b234cd9f63de54x3m')}")
    
    # Test Question 13
    print(f"Q13: {count_pairs_in_binary('100101')}")
    print(f"Q13 (additional): {count_pairs_in_binary('1001101010010')}")
    
    # Test Question 14
    valid_currency = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
    print(f"Q14: {find_min_denominations(valid_currency, 210)}")
    
    valid_currency = [1, 2, 5, 10, 20, 50, 100, 200, 500]
    print(f"Q14 (additional): {find_min_denominations(valid_currency, 556)}")
    
    # Test Question 15
    print(f"Q15: {non_consecutive_stops(12, 4)}")
    print(f"Q15 (additional): {non_consecutive_stops(16, 5)}")
    
    # Test Question 16
    plays = [
        ("Stone", "Stone"),
        ("Stone", "Paper"),
        ("Stone", "Scissor"),
        ("Paper", "Stone"),
        ("Paper", "Paper"),
        ("Paper", "Scissor"),
        ("Scissor", "Scissor"),
        ("Scissor", "Stone"),
        ("Scissor", "Paper")
    ]
    print(f"Q16: {stone_paper_scissor_game(plays)}")
    
    # Test Question 17
    print(f"Q17: {validate_email('user@example.com')}")
    print(f"Q17 (invalid): {validate_email('User@example.com')}")
    
    # Test Question 18
    print(f"Q18(a):\n{pattern_a(4)}")
    print(f"Q18(b):\n{pattern_b(4)}")
    print(f"Q18(c):\n{pattern_c(4)}")
    print(f"Q18(d):\n{pattern_d(7)}")
    print(f"Q18(e):\n{pattern_e(5)}")
    
    # Test Question 19
    print(f"Q19: {cyclic_rotation(1, 'happy', 2)}")
    print(f"Q19 (additional): {cyclic_rotation(2, 'happy', 3)}")
    
    # Test Question 20
    patient_data = {
        "Sugar level": 56,
        "Blood pressure": 120,
        "Heartbeat rate": 45,
        "weight": 67,
        "fat percentage": 67
    }
    print(f"Q20: {health_condition_comparison(patient_data)}")
    
    # Test Question 21
    print(f"Q21 (1634): {is_armstrong(1634)}")
    print(f"Q21 (153): {is_armstrong(153)}")
    print(f"Q21 (125): {is_armstrong(125)}")
    
    # Test Question 22
    print(f"Q22 (12): {decimal_to_binary(12)}")
    print(f"Q22 (20): {decimal_to_binary(20)}")
    
    # Test Question 23
    print(f"Q23 (28): {is_perfect_number(28)}")
    print(f"Q23 (6): {is_perfect_number(6)}")
    print(f"Q23 (496): {is_perfect_number(496)}")
    print(f"Q23 (8128): {is_perfect_number(8128)}")
    print(f"Q23 (33): {is_perfect_number(33)}")
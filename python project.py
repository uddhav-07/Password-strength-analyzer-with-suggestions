def grade_password(password):
    score = 0
    feedback = []

    if len(password) > 15:
        score += 3
    elif 12 <= len(password) <= 15:
        score += 2
    else:
        score -= 2
        feedback.append("Make your password longer than 12 characters.")

    if any(char.isupper() for char in password):
        score += 2
    else:
        feedback.append("Add uppercase letters.")

    if any(char.islower() for char in password):
        score += 2
    else:
        feedback.append("Add lowercase letters.")

    if any(char.isdigit() for char in password):
        score += 2
    else:
        feedback.append("Add numbers.")

    if any(char in "!@#$%^&*()-_=+[{]}|;:',<.>/?`~" for char in password):
        score += 3
    else:
        feedback.append("Add special characters.")

    common_patterns = ["password", "123456", "qwerty"]
    if any(pattern in password.lower() for pattern in common_patterns):
        score -= 5
        feedback.append("Avoid common patterns like 'password' or '123456'.")

    if score >= 8:
        strength = "Strong"
    elif 4 <= score < 8:
        strength = "Moderate"
    else:
        strength = "Weak"
    return score, strength, feedback

password = input("Enter a password: ")
score, strength, feedback = grade_password(password)
print(f"Password Score: {score}")
print(f"Password Strength: {strength}")
if feedback:
    print("Suggestions to improve your password:")
    for tip in feedback:
        print(f"- {tip}")
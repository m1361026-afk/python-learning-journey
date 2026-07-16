# Collect the information needed to evaluate class eligibility
user_age = int(input("Please enter your age: "))
user_score = int(input("Please enter your score: "))
parent_agrees = input("Whether your parents agree (yes/no): ")

# Validate all inputs before evaluating class eligibility
if  (
    10 <= user_age <= 18 
    and 0 <= user_score <= 100 
    and (parent_agrees == "yes" or parent_agrees == "no")
): 
    
    # Check the advanced class first because it has stricter requirements
    if (
        user_age >= 15
        and user_score >= 80
        and parent_agrees == "yes"
    ):
        print("Advanced class.")

    # Applicants who miss the advanced requirements may still enter the basic class
    elif (
        user_age >= 12
        and user_score >= 60
        and parent_agrees == "yes"
    ):
        print("Basic class.")

    # Valid input does not necessarily mean the applicant qualifies
    else:
        print("Not eligible.")

# Reject any input outside the permitted values
else:
    print("Invalid input.")
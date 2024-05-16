def build_profile():
    profile = {
        "age": 0,
        "hobbies": []
    }
    profile["age"] = int(input("Enter the profile age"))
    # split for better testing
    more_hobbies = True
    while more_hobbies:
        profile["hobbies"].append(input("Enter a hobby:"))
        more = input("More hobbies? type y for yes, n for no")
        if more.lower() == 'n':
            more_hobbies = False
    return profile

def match(profile_1, profile_2):
    match_quality = 0
    age_diff = profile_1["age"] - profile_2["age"]
    if age_diff <= 5 and age_diff >= -5:
        match_quality += 1
    for hobby in profile_1["hobbies"]:
        if hobby in profile_2["hobbies"]:#membership operator
            match_quality += 1
    return match_quality

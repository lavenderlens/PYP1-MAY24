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
        if more.casefold() == 'n':
            more_hobbies = False
    return profile

def build_profile_with_set():
    '''see CH10-SETS'''
    profile = {
        "age": 0,
        "hobbies": set()
    }
    age = int(input("Enter the profile age"))
    profile["age"] = age
    # split for better testing
    more_hobbies = True
    while more_hobbies:
        hobby = input("Enter a hobby: >>>")
        profile["hobbies"].add(hobby)
        more = input("More hobbies? type y for yes, n for no")
        if more.casefold() == 'n':
            more_hobbies = False
    return profile

def match_via_set(profile_1, profile_2):
    '''see CH10-SETS'''
    match_quality = 0
    age_diff = abs(profile_1["age"] - profile_2["age"])#abs works with neg or pos numbers
    # age_diff = age_diff if age_diff > 0 else - age_diff # without abs
    if age_diff <= 5:
        match_quality += 1
    hobbies_in_common = profile_1["hobbies"].intersection(profile_2["hobbies"])
    match_quality += len(hobbies_in_common)
    return match_quality

def match(profile_1, profile_2):
    match_quality = 0
    age_diff = abs(profile_1["age"] - profile_2["age"])#abs works with neg or pos numbers
    # age_diff = age_diff if age_diff > 0 else - age_diff # without abs
    if age_diff <= 5:
        match_quality += 1
    for hobby in profile_1["hobbies"]:
        if hobby in profile_2["hobbies"]:#membership operator
            match_quality += 1
    return match_quality

# before:
# def match(profile_1, profile_2):
#     match_quality = 0
#     if profile_1["age"] - profile_2["age"] <= 5 or profile_2["age"] - profile_1["age"] <= 5:
#         match_quality += 1
#     for hobby in profile_1["hobbies"]:
#         for other_hobby in profile_2["hobbies"]:
#             if other_hobby.casefold() == hobby:
#                 match_quality += 1
#     # should pass each hobbies list into a set for comparison
#     # this will rule out duplicate entries
#     return match_quality
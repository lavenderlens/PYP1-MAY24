from exercise_5_profile_matcher import build_profile, match

print("Create first profile:")
p1 = build_profile()
print("Create second profile:")
p2 = build_profile()
print("Get match score:")
print(match(p1, p2))
print(p1, p2)
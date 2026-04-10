

print("a.Student Attendance Analysis")
day1 = {101, 102, 103, 104}
day2 = {103, 104, 105, 106}

both_days = day1 & (day2)
either_day = day1 | day2
absent_day2 = day1 - day2

print("Present on both days:", both_days)
print("Present on either day:", either_day)
print("Absent on second day:", absent_day2)


print("b. Course Interests of Two Users")

user1 = {"Python", "Data Science", "Machine Learning"}
user2 = {"Data Science", "AI", "Cloud Computing"}

common = user1 & (user2)
suggestions = user2 - user1

print("Common interests:", common)
print("Suggestions for user1:", suggestions)


print("c. Online Store Products")

available = {"laptop", "phone", "tablet", "monitor"}
sold = {"phone", "monitor"}

in_stock = available - sold
sold_out = available &  (sold)

print("Products in stock:", in_stock)
print("Products sold out:", sold_out)



print("d. IP Address Analysis")

L = {"192.168.1.1", "192.168.1.2", "192.168.1.3"}
F = {"192.168.1.2", "192.168.1.4", "192.168.1.5"}
B = {"192.168.1.5", "192.168.1.6"}

both_not_blacklisted = (L & (F)) - B
attempted_not_succeeded = F - L
only_blacklisted = B - (L | F)

print("IPs in both success and fail, not blacklisted:", both_not_blacklisted)
print("IPs attempted but not succeeded:", attempted_not_succeeded)
print("Only blacklisted IPs:", only_blacklisted)



print("e. Skills Matching")

required_skills = {"Python", "SQL", "Machine Learning", "Communication"}
applicant_skills = {"Python", "Communication", "HTML"}
outdated_skills = {"SQL"}

missing_skills = (required_skills - applicant_skills) - outdated_skills

print("Missing required skills (excluding outdated):", missing_skills)

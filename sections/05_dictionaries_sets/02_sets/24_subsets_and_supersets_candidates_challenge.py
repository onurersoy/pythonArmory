required_skills = ['python', 'github', 'linux']

candidates = {
    'anna': {'java', 'linux', 'windows', 'github', 'python', 'full stack'},
    'bob': {'github', 'linux', 'python'},
    'carol': {'linux', 'javascript', 'html', 'python', 'github'},
    'daniel': {'pascal', 'java', 'c++', 'github'},
    'ekani': {'html', 'css', 'github', 'python', 'linux'},
    'fenna': {'linux', 'pascal', 'java', 'c', 'lisp', 'modula-2', 'perl', 'github'},
}

interviewees = set()
for candidate, skills in candidates.items():
    # if skills.issuperset(required_skills):
    if skills > set(required_skills):  # It checks if it's a 'proper' superset
        # Instead of converting the list to set inside the loop, do this conversion before the loop, so you don't have
        # to convert it each time the code goes into the loop^^.
        interviewees.add(candidate)

print(interviewees)

def introduction(name, age, grade, university, cgpa, hobbies, hometown, favorite_subject,
                 skills, career_goal, languages, clubs, achievements, favorite_quote, fun_fact):
    print  (
        "Hi, my name is ",name," and I am",age," years old. ",
        "I am currently pursuing", grade," at",university ,"with a CGPA of",cgpa,". ",
        "I came from ",hometown,". My favorite subject is", favorite_subject," and I enjoy ",hobbies,". "
        "I have skills in", skills,". My career goal is", career_goal ,". ",
        "I speak", languages," and am active in", clubs,". ",
        "Some of my achievements include",achievements,". ",
        "My favorite quote is ","'" +favorite_quote+"'",".  fun _fact:",fun_fact,"."
    )
    



introduction(
    "Ameesha", 21, "BTech", "MGRIE", 8.8, "drawing and painting", "Khammam",
    "Computer Science", "Python programming, problem solving",
    "becoming a software engineer", "English, Telugu",
    "Coding Club, Art Society", "publishing a literature in newspaper",
    "Failuers are stepping stone to success", "I can finish reading a book in one night"
)

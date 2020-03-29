

"""

Time = Lecture_Times['Time']

Lecturer_Free_Times = one(Lecturer_Free, Lecturer_Names, Time)
Classroom_Times = one(Classroom_Free, Classrooms, Time)
Lecture_Free_Times = one(Lecture_Times, Subject_Names, Time)



"""

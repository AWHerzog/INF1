

def register(enrollments, student, course):
    if student not in enrollments:
        enrollments[student] = {course}
    else:
        enrollments[student].add(course)
    return enrollments

def deregister(enrollments, student, course):
    if student in enrollments:
        if course in enrollments[student]:
            enrollments[student].remove(course)
        if len(enrollments[student]) == 0:
            del(enrollments[student])
    return enrollments




print( register(  {},                        111, "INF-1") )
print( register(  {222: {"INF-1", "BIO-2"}}, 222, "PHY-2") )
print( register(  {222: {"INF-1", "BIO-2"}}, 333, "PHY-2") )
print( deregister({222: {"INF-1", "BIO-2"}}, 222, "INF-1") )
print( deregister({222: {"INF-1"}},          222, "INF-1") )
print( deregister({222: {"INF-1", "BIO-2"}}, 111, "INF-1") )
print( deregister({},                        111, "INF-1") )
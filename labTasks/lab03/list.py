work_days = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday" ]

for i in range( len(work_days) ):
    print( work_days[i] )

for day in work_days:
    print( day )


# POZOR SEZNAMY JSOU PREDANY REFERENCI
# seznam1 = [0, 1, 2]
# seznam2 = seznam1
# seznam1[0] = 120
# seznam2 se take zmeni -> pouzivat seznam2 = seznam1.copy()
# muzu mit vnoreny seznamy -> na to uz deep copy
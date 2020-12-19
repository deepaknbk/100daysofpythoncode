from data import us_state_abbrev,states_list
"""
- Print out the 10th item in each.
- Print out the 45th key in the dictionary.
- Print out the 27th value in the dictionary. """

i=1
print("10th Element in US State Abbrev:")
for k,v in us_state_abbrev.items():
    if i%10==0:
        print(k,v)
    i += 1
print("10th Element in State List:",states_list[9::10])

i=1
print("45th Key in US State Abbrev:")
for k,v in us_state_abbrev.items():
    if i==45:
        print(k)
    i += 1

i=1
print("27th Value in US State Abbrev:")
for k,v in us_state_abbrev.items():
    if i==27:
        print(v)
    i += 1



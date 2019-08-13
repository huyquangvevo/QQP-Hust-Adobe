from fuzzywuzzy import fuzz,process

q1_not = "What do you do with row"
q2_not = "What do you do with row"

q1_d = "How can I be a good geologist?"
q2_d = "What should I do to be a great geologist?"


q1_list = q1_not.split()
q2_list = q2_not.split()

i = 0
len_ = min(len(q1_list),len(q2_list))

while  i< len_:
    if q1_list[i] == q2_list[i]:
        i+=1

j = 0
while j<len_:
    if q1_list[len(q1_list) - 1 - j] == q2_list[len(q2_list) - 1-j]:
        j += 1

if i & j:
    print("True")
else:
    print("False")

# m = fuzz.ratio(q1_not,q2_not)
# print(m)
# n = fuzz.partial_token_sort_ratio(q1_not,q2_not)
# print(n)

# print(fuzz.partial_token_sort_ratio(q1_not,q2_not))

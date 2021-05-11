#Designed to count phrases of words grouped in 2s

def group_text(text, group_size):
    """
    groups a text into text groups set by group_size
    returns a list of grouped strings
    """
    word_list = text.split()
    group_list = []
    for k in range(len(word_list)):
        start = k
        end = k + group_size
        group_slice = word_list[start: end]
        # append only groups of proper length/size
        if len(group_slice) == group_size:
            group_list.append(" ".join(group_slice))
    return group_list
        

text = "test this is test a this is a test"

group_size = 2
group_list = group_text(text, group_size)
# convert list to set to avoid duplicates
group_set = set(group_list)

#if wanting to output a text count uncomment the below and remove the group_set print
#for group in group_set:
#    count = text.count(group)
#    sf = "'%s' appears %d times in the text"
#   print(sf % (group, count))

print(group_set)

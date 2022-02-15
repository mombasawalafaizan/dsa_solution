def recursivelyPrint(words, cur_string, cur_row):
    if cur_row == len(words):
        print(cur_string)
        return 
    for i in words[cur_row]:
        recursivelyPrint(words, cur_string +" "+ i, cur_row+1)

words = [["you", "we"],
        ["have", "are"],
        ["sleep", "eat", "drink"]]

recursivelyPrint(words, '', 0)

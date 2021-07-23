
mylist = [6,5,4,3,1,20,60,120]
# mylist [1, 3, 4, 5, 6, 20, 60, 120]
def sort_list(var_list):# sort_list is  var
    for i in var_list:
        var_list.sort()
    print(var_list)
    return var_list

sort_list(mylist)
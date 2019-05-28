from sanitize_a_grocery_list_final import get_all_the_items, remove_all_not_vege, save_the_list


name_of_file='unchecked_grocery_list.txt'
list_of_items = get_all_the_items(name_of_file)
#remove anything that is not vegetarian based on a list
non_vege_file = 'non_vege_list.txt'
good_list = remove_all_not_vege(non_vege_file, list_of_items)
#save all the items in a file
name_of_output_file = 'checked_grocery_list.txt'
save_the_list(name_of_output_file, good_list)
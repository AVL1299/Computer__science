
def find_common_participants(participants_first_group, participants_second_group, separ=","):
    list_1 = set(participants_first_group.split(separ))
    list_2 = set(participants_second_group.split(separ))
    list_new = list(list_1.intersection(list_2))
    list_new.sort()
    return list_new

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


print(find_common_participants(participants_first_group, participants_second_group, separ="|"))





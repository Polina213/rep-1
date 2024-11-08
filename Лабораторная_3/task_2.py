def find_common_participants(group_1, group_2, split=','):
    first_group = group_1.split(split)
    second_group = group_2.split(split)
    intersection_set = list(set(first_group).intersection(set(second_group)))
    intersection_set.sort()
    return intersection_set


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, split='|')
print("Общие участники:", result)

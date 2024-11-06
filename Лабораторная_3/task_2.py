def find_common_participants(participants_first_group, participants_second_group, split=','):
    first_group = participants_first_group.split(split)
    second_group = participants_second_group.split(split)
    intersection_set = list(set(first_group).intersection(set(second_group)))
    intersection_set.sort()
    return intersection_set


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", result)

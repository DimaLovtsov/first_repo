#converting to a set

days = ['Mon', 'Tus', 'Wen', 'Thur', 'Fri', 'Fri']
days_set = set(days)
print(days_set)

#adding 

days_set.add('Sun')
print(days_set)

#updating

temperature = {11, 6, 8, 8, 12, -2, 6, -1, 0, 3, 3}
temperature_up = {-3, -3, -2, -4}

temperature.update(temperature_up)

print(temperature)

temperature_above_0 = temperature.remove(-1)
print(temperature)
print(temperature_above_0)

#clearing
print("Clearing")
temperature = {11, 6, 8, 8, 12, -2, 6, -1, 0, 3, 3}
temperature.clear()
print(temperature)

#item is in the set
temperature = {11, 6, 8, 8, 12, -2, 6, -1, 0, 3, 3}
print(-1 in temperature)

#loop
temperature = {11, 6, 8, 8, 12, -2, 6, -1, 0, 3, 3}
for temp in temperature:
    print(temp)

#union two sets
print("union two sets")
temperature_jan = {11, 6, 8, 8, 12, -2, 6, -1, 0, 3, 3}
temperature_feb = {10, 6, 8, 8, 10, -2, -4}

temp_union = temperature_jan.union(temperature_feb)
print(temp_union)

#intersection of two sets
print("intersection of two sets")
temperature_jan = {11, 6, 8, 8, 12, -2, 6, -1, 0, 3, 3}
temperature_feb = {10, 6, 8, 8, 10, -2, -4}
temp_inters_1 = temperature_jan.intersection(temperature_feb)
temp_inters_2 = temperature_jan & temperature_feb
print(temp_inters_1)
print(temp_inters_2)

#symetric difference
print("symetric difference")
temperature_jan = {11, 6, 8, 8, 12, -2, 6, -1, 0, 3, 3}
temperature_feb = {10, 6, 8, 8, 10, -2, -4}
temp_dif_1 = temperature_jan.symmetric_difference(temperature_feb)
temp_dif_2 = temperature_jan ^ temperature_feb
print(temp_dif_1)
print(temp_dif_2)
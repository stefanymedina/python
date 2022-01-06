def is_all_strings(coll):
   return all([type(i) == str for i in coll ])
print(is_all_strings([2, 'b', 'c']))
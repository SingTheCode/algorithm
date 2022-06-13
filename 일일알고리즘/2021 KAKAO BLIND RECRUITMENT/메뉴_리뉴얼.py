# from itertools import combinations
#
#
# def convertObj(order, courseItem, solObj):
#     if len(order) < courseItem:
#         return
#
#     tmp = list(combinations(order, courseItem))
#     for value in tmp:
#         value = tuple(sorted(value))
#         key = ""
#         for k in range(courseItem):
#             key += value[k]
#         if key in solObj:
#             solObj[key] += 1
#         else:
#             solObj[key] = 0
#
#
# def solution(orders, course):
#     result = []
#
#     for i in range(len(orders)):
#         orders[i] = list(orders[i])
#     for courseItem in course:
#         solObj = {}
#
#         for order in orders:
#             convertObj(order, courseItem, solObj)
#         all_keys = solObj.keys()
#         all_values = solObj.values()
#         if len(all_keys) >= 2:
#             mmax = max(all_values)
#             if mmax > 0:
#                 for key, value in solObj.items():
#                     if value == mmax:
#                         result.append(key)
#     result.sort()
#
#     return result
#
#

# import collections
# import itertools
#
#
# def solution(orders, course):
#     result = []
#
#     for course_size in course:
#         order_combinations = []
#         for order in orders:
#             order_combinations += itertools.combinations(sorted(order), course_size)
#
#         most_ordered = collections.Counter(order_combinations).most_common()
#         print(most_ordered)
#         result += [k for k, v in most_ordered if v > 1 and v == most_ordered[0][1]]
#         print(result)
#     return [''.join(v) for v in sorted(result)]
#
#
# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))

arr = [(('A', 'C'), 4), (('C', 'D'), 3), (('C', 'E'), 3), (('D', 'E'), 3), (('B', 'C'), 2), (('B', 'F'), 2),
       (('B', 'G'), 2), (('C', 'F'), 2), (('C', 'G'), 2), (('F', 'G'), 2), (('A', 'D'), 2), (('A', 'E'), 2),
       (('A', 'B'), 1), (('A', 'F'), 1), (('A', 'G'), 1), (('A', 'H'), 1), (('C', 'H'), 1), (('D', 'H'), 1),
       (('E', 'H'), 1)]
is_True = 0
result = [v for k, v in arr]
print(result)

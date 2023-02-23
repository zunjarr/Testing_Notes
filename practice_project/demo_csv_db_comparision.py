import re

import pandas as pd

# df_csv = pd.read_csv(r'C:/Users/dorugzu/Downloads/Idorsia tdms.inventory_analytics.csv',
#                      converters={i: str for i in range(1000)})
# df_csv1 = pd.read_csv(r'C:/Users/dorugzu/Downloads/Idorsia tdms.inventory_analytics_DB.csv',
#                       converters={i: str for i in range(1000)})
# # print('Week column data is: ', df_csv['week'])
# print(' new_df before sorting is ', df_csv)
# print(type(df_csv))
#
# df_sorted = df_csv.sort_values(by='week')
# print(' new_df after sorting is ', df_sorted)
#
# # df1 = pd.read_csv(r'C:/Users/dorugzu/Downloads/Idorsia tdms.inventory_analytics.csv')
# # df2 = pd.read_csv(r'C:/Users/dorugzu/Downloads/Idorsia tdms.inventory_analytics_DB.csv')
#
# lis_dic = df_csv.to_dict('records')
# lis_dic1 = df_csv1.to_dict('records')
# # print('Type is ', type(lis_dic))
# # print('Type is  ', type(lis_dic1))
#
# print('First df ', lis_dic)
# print('Second df ', lis_dic1)
#
# empty_list = []
# empty_list1 = []
# # for 1st csv
# for ele in lis_dic:
#     dic = {}
#     week = ele['week']
#     channel = ele['channel']
#     prod_grp_id = ele['prod_grp_id']
#     ecs_qs = ele['ecs_qs']
#     keyd = week + '_' + channel + '_' + prod_grp_id
#     dic[keyd] = ecs_qs
#     # li.append(keyd)
#     empty_list.append(dic)
# print('Merged columns for 1st csv', empty_list)
#
# # for second csv
# for ele1 in lis_dic1:
#     dic1 = {}
#     week = ele1['week']
#     channel = ele1['channel']
#     prod_grp_id = ele1['prod_grp_id']
#     ecs_qs = ele1['ecs_qs']
#     keyd = week + '_' + channel + '_' + prod_grp_id
#     dic1[keyd] = ecs_qs
#     # li.append(keyd)
#     empty_list1.append(dic1)
# print('Merged columns for second csv', empty_list1)
#
# result = []
# First_df_data = []
# for eles in empty_list:
#
#     if eles in empty_list1:
#         resu = eles
#         out = "pass"
#         First_df_data.append(resu)
#         result.append(out)
#     else:
#         resu = eles
#         out = "fail"
#         First_df_data.append(resu)
#         result.append(out)
# print('Comparision is ', result)
# print(First_df_data)
# df_csv['status'] = result
# df_csv['record'] = First_df_data
# df_csv.to_csv("Final_Report.csv")

# ----------------------------------------------------------
# ----------------------------------------------------------

# df_csv = pd.read_csv(r'C:\Users\reddyma\sample_data\Test\Read_Write_Data\Data\Idorsia tdms.inventory_analytics (3).csv',
#                              converters={i: str for i in range(1000)})
# df_csv1 = pd.read_csv(r'Data/Idorsia tdms.inventory_analytics_DB.csv',
#                              converters={i: str for i in range(1000)})

# df_csv = pd.read_csv(r'C:/Users/dorugzu/Downloads/Idorsia tdms.inventory_analytics.csv',
#                      converters={i: str for i in range(1000)})
# df_csv1 = pd.read_csv(r'C:/Users/dorugzu/Downloads/Idorsia tdms.inventory_analytics_DB.csv',
#                       converters={i: str for i in range(1000)})
# lis_dic = df_csv.to_dict('records')
# lis_dic1 = df_csv1.to_dict('records')
# # print(lis_dic)
# # print(lis_dic1)
#
# # print(type(lis_dic))
#
# empty_list = []
# empty_list1 = []
# # for 1st csv
# for ele in lis_dic:
#     dic = {}
#     week = ele['week']
#     channel = ele['channel']
#     prod_grp_id = ele['prod_grp_id']
#     ecs_qs = ele['ecs_qs']
#     trx_cnt = ele['trx_cnt']
#     trx_qty = ele['trx_qty']
#     build_burn = ele['build_burn']
#     demand = ele["demand"]
#     keyd = week + '_' + channel + '_' + prod_grp_id
#     # trx_cnt, trx_qty, build_burn, demand
#     dic[keyd] = {"ecs_qs": ecs_qs, "trx_cnt": trx_cnt, "trx_qty": trx_qty, "build_burn": build_burn, "demand": demand}
#     # li.append(keyd)
#     empty_list.append(dic)
# # print(empty_list)
# # for second csv
# for ele1 in lis_dic1:
#     dic1 = {}
#     week = ele1['week']
#     channel = ele1['channel']
#     prod_grp_id = ele1['prod_grp_id']
#     ecs_qs = ele1['ecs_qs']
#     trx_cnt = ele1['trx_cnt']
#     trx_qty = ele1['trx_qty']
#     build_burn = ele1['build_burn']
#     demand = ele1["demand"]
#     keyd = week + '_' + channel + '_' + prod_grp_id
#     dic1[keyd] = {"ecs_qs": ecs_qs, "trx_cnt": trx_cnt, "trx_qty": trx_qty, "build_burn": build_burn, "demand": demand}
#     # li.append(keyd)
#     empty_list1.append(dic1)
# print(empty_list)
# # print(empty_list1)
# print(empty_list1)
# var = []
# r = []
# for eles in empty_list:
#     if eles in empty_list1:
#         print('checking in 2nd list: ', eles)
#         ind = empty_list1.index(eles)
#         # print(empty_list1(ind))
#         for el11, eq in eles.items():
#
#             for el in empty_list1[ind].values():
#                 print(el)
#                 if eq['ecs_qs'] == el['ecs_qs'] and eq['trx_cnt'] == el['trx_cnt'] and eq['trx_qty'] == el['trx_qty']:
#                     out = "pass"
#                     r.append("element is passed")
#                     var.append(out)
#                 # f = eq['ecs_qs']
#                 # g = eq['trx_cnt']
#                 # h = eq['trx_qty']
#                 # irf = eq['build_burn']
#                 # j = eq["demand"]
#                 #
#                 # a = el['ecs_qs']
#                 # b = el['trx_cnt']
#                 # c = el['trx_qty']
#                 # d = el['build_burn']
#                 # e = el["demand"]
#
#         # resu = eles
#         # out = "pass"
#         # r.append(resu)
#         # var.append(out)
#     else:
#         # resu = eles
#         out = "fail"
#         r.append("element is failled")
#         var.append(out)
#
# # print(var)
# # print(r)
# df_csv['status'] = var
# df_csv['record'] = r
# df_csv.to_csv("output.csv")
# -----------------------------------------------------
# ----------------------------------------------------------

# df_csv = pd.read_csv(r'C:/Users/dorugzu/Downloads/Idorsia tdms.inventory_analytics.csv',
#                              converters={i: str for i in range(1000)})

# # df = pd.read_csv('test.csv')
# ----------------------------------------------------------
# ----------------------------------------------------------
# pattern = re.compile(r'\d\d.\d\d.\d\d\d\d')
#
# matches = pattern.finditer(stored_data)
#
# for match in matches:
#     print(match)
# ----------------------------------------------------------
# ----------------------------------------------------------

# df_csv = pd.read_csv(r'C:/Users/dorugzu/Downloads/Idorsia tdms.inventory_analytics.csv',
#                      converters={i: str for i in range(1000)})
# df_csv1 = pd.read_csv(r'C:/Users/dorugzu/Downloads/Idorsia tdms.inventory_analytics_DB.csv',
#                       converters={i: str for i in range(1000)})
# lis_dic = df_csv.to_dict('records')
# lis_dic1 = df_csv1.to_dict('records')


df_csv = pd.read_csv(r'C:/Users/dorugzu/Downloads/First_file.csv',
                             converters={i: str for i in range(1000)})
df_csv1 = pd.read_csv(r'C:/Users/dorugzu/Downloads/Second_file.csv',
                             converters={i: str for i in range(1000)})
lis_dic = df_csv.to_dict('records')
lis_dic1 = df_csv1.to_dict('records')
# print(lis_dic)
# print(lis_dic1)
# print(type(lis_dic))

empty_list = []
empty_list1 = []

# for 1st csv
for ele in lis_dic:
    dic = {}
    week = ele['week']
    channel = ele['channel']
    prod_grp_id = ele['prod_grp_id']
    ecs_qs = ele['ecs_qs']
    trx_cnt = ele['trx_cnt']
    trx_qty = ele['trx_qty']
    build_burn = ele['build_burn']
    demand = ele["demand"]
    doh = ele["doh"]
    inventory = ele["inventory"]
    keyd = week + '_' + channel + '_' + prod_grp_id
    # trx_cnt, trx_qty, build_burn, demand
    dic[keyd] = {"ecs_qs": ecs_qs, "trx_cnt": trx_cnt, "trx_qty": trx_qty, "build_burn": build_burn, "demand": demand, "doh": doh, "inventory": inventory}
    empty_list.append(dic)
# print(empty_list)

# for second csv
for ele1 in lis_dic1:
    dic1 = {}
    week = ele1['week']
    channel = ele1['channel']
    prod_grp_id = ele1['prod_grp_id']
    ecs_qs = ele1['ecs_qs']
    trx_cnt = ele1['trx_cnt']
    trx_qty = ele1['trx_qty']
    build_burn = ele1['build_burn']
    demand = ele1["demand"]
    doh = ele1["doh"]
    inventory = ele1["inventory"]
    keyd = week + '_' + channel + '_' + prod_grp_id
    dic1[keyd] = {"ecs_qs": ecs_qs, "trx_cnt": trx_cnt, "trx_qty": trx_qty, "build_burn": build_burn, "demand": demand, "doh": doh, "inventory": inventory}
    empty_list1.append(dic1)
# print(empty_list)
# print(empty_list1)

var = []
r = []
for f_element in empty_list:
    for s_element in empty_list1:
        if f_element.keys() == s_element.keys():
            f_element_values = f_element.values()
            var.append(*f_element_values)
            s_element_values = s_element.values()
            r.append(*s_element_values)
# print(var)
# print(r)
status = []
comment = []
for f_list_dict, s_list_dict in zip(var, r):
    print('f_list_dict is : ', f_list_dict)
    print('s_list_dict : ', s_list_dict)
    # print(ele2['ecs_qs'])
    if (f_list_dict['ecs_qs'] == s_list_dict['ecs_qs']) and (f_list_dict['trx_cnt'] == s_list_dict['trx_cnt']) and (f_list_dict['trx_qty'] == s_list_dict['trx_qty']) and (f_list_dict['build_burn'] == s_list_dict['build_burn']) and (f_list_dict['demand'] == s_list_dict['demand']) and (f_list_dict['doh'] == s_list_dict['doh']) and (f_list_dict['inventory'] == s_list_dict['inventory']):
        s = "pass"
        status.append(s)
        c = "Values are matching hence passed"
        comment.append(c)
    elif f_list_dict['ecs_qs'] != s_list_dict['ecs_qs']:
        s = "fail"
        status.append(s)
        c= f"In second file there is miss match and its ecs_qs {s_list_dict['ecs_qs']} is not same"
        comment.append(c)
    elif f_list_dict['trx_cnt'] != s_list_dict['trx_cnt']:
        s = "fail"
        status.append(s)
        c = f"In second file there is miss match and its trx_cnt {s_list_dict['trx_cnt']} is not same"
        comment.append(c)
    elif f_list_dict['trx_qty'] != s_list_dict['trx_qty']:
        s = "fail"
        status.append(s)
        c = f"In second file there is miss match and its trx_qty {s_list_dict['trx_qty']} is not same"
        comment.append(c)
    elif f_list_dict['build_burn'] != s_list_dict['build_burn']:
        s = "fail"
        status.append(s)
        c = f"In second file there is miss match and its build_burn {s_list_dict['build_burn']} is not same"
        comment.append(c)
    elif f_list_dict['demand'] != s_list_dict['demand']:
        s = "fail"
        status.append(s)
        c = f"In second file there is miss match and its demand {s_list_dict['demand']} is not same"
        comment.append(c)
    elif f_list_dict['doh'] != s_list_dict['doh']:
        s = "fail"
        status.append(s)
        c = f"In second file there is miss match and its doh {s_list_dict['doh']} is not same"
        comment.append(c)
    elif f_list_dict['inventory'] != s_list_dict['inventory']:
        s = "fail"
        status.append(s)
        c = f"In second file there is miss match and its inventory {s_list_dict['inventory']} is not same"
        comment.append(c)
    else:
        s = "fail"
        status.append(s)
        c = "elements are not same"
        comment.append(c)
print(status)
print(comment)
df_csv1['status'] = status
df_csv1['comment'] = comment
print(df_csv1.to_csv("Result.csv"))

from behave import *
import csv
import datetime
import pandas as pd
from datetime import date, timedelta
import psycopg2


# 'host': 'Idorsia.aws.integrichain.com', 'user': 'icuser', 'password': 'int@gri#hai$', 'port': 3306, 'db': 'tdms'


# mydb = connection.connect(host="localhost", database = 'Student',user="root", passwd="root",use_pure=True)
#         con = connection.connect(host='prod-general-purpose-db.cbptgzgybgnp.us-east-1.rds.amazonaws.com',
#                                              database='',
#                                              user='devuser',
#                                              password='xua@EpJw3B4k')
#         query = "Select * from ic.inventory_analytics_algorithm iaa limit 100;"
#         # "select * from ic.inventory_analytics_algorithm iaa limit 100"
#         result_dataFrame = pd.read_sql(query,con)
#         result_dataFrame.to_csv('Test.csv')
#         # con.close() #close the connection


df = pd.read_csv(r'C:/Users/dorugzu/Downloads/Idorsia tdms.inventory_analytics.csv')
# print(df)

channel_name = df['channel']
# print("channel_name is ", channel_name)

channel_week = df['week']
# print("channel_week is ", channel_week)

# unique_channels
channels = df['channel'].tolist()
# print("channels are ", channels)
unique_channel = list(set(channels))
# print("unique_channel are ", unique_channel)

# unique_prod_grp_id
prod_group_id = df['prod_grp_id'].tolist()
# print(type(prod_group_id))
unique_prod_grp_ids = list(set(prod_group_id))
# print("unique_prod_grp_ids are", unique_prod_grp_ids)
# print(len(unique_prod_grp_ids))

# today_date = pd.Timestamp.today().strftime('%d-%m-%Y')
# print("today date ", today_date)
# print(type(today_date))
# -------------------------------------------------
# start_day = '26.09.2022'
# end_day = '05.09.2022'
# start_day = pd.to_datetime(start_day)
# end_day = pd.to_datetime(end_day)
# print('check')
# print(type(start_day))
# print(type(end_day))
# -------------------------------------------------

# df = df[df['week'].between(start_day, end_day)]
# print(df)
# print('11 ****************************')
# df1 = df[df["channel"] == "Retail Pharmacy"]
# print("df1 is  ", '\n', df1)
# print(type(df1))
# print('1 ****************************')

# week = df['week']  # .tolist()
# print(type(week))

# df = pd.to_datetime(df['week'], format='%d%b%Y:%H:%M:%S.%f')
# print(df)
# df['week'] = pd.to_datetime(df.week)
# df['week'] = pd.to_datetime(df['week'], format='%Y%m%d')
# print('22 ****************************')
# print(df)
# print(df.dtypes)
# week = df['week'].tolist()
# print(week)
# print(type(week))
print('2 ****************************')

# for w, i in df.iterrows():
#     print(i[1])
#     # print(type(i[1]))
#     i = pd.to_datetime(i)
#     print(type(i))

# print(week)
last_date = df["week"].iloc[-1]
print('Last date is ', last_date)

def subtract_days_from_date(date, days):
    subtracted_date = pd.to_datetime(last_date) - timedelta(days=days)
    subtracted_date = subtracted_date.strftime("%d-%m-%Y")

    return subtracted_date


date_subtraction = subtract_days_from_date(last_date, 30)
print('Date_30_days', date_subtraction)
print(type(date_subtraction))

sorted_df_of_30_days = df[df['week'].between(date_subtraction, last_date)]
print('sorted_df_of_30_days is', sorted_df_of_30_days)

for i in df['week']:
    # print(i)
    if i > date_subtraction:
        print('Date from last 4 weeks ', i)
# -------------------------------------------------
# start_date = date(date_subtraction)
# end_date = date(last_date)  # perhaps date.now()
#
# delta = end_date - start_date  # returns timedelta
# print(delta)
# for i in range(delta.days + 1):
#     day = start_date + timedelta(days=i)
#     print(day)
#
# pd.date_range(start=start_date, end=end_date)

# week = df['week','id','week','channel','prod_grp_id','ecs_qs','trx_cnt','trx_qty','build_burn','demand','doh','inventory','ts']

# newDate = datetime.strptime(last_date, "%Y-%m-%d")
# print('newDate is', newDate)
# newDate2 = (time.strptime(last_date[, "%Y-%m-%d"]))

# df = df.sort_values(by=["week"], ascending=False)
# print('sorted dates ', df)

# df.iloc[:,-1:]

# converting to dataframe
# df = pd.DataFrame({'week': week})

# extracting the week number
# df['week_number'] = df['week'].dt.week

# print(df['week_number'])
# print('1 ****************************')

# df['year'] = pd.DatetimeIndex(df.week).year
# print(df['year'])
# empty_yr_list = []
# for y in df['year']:
#     if y not in empty_yr_list:
#         empty_yr_list = empty_yr_list.append(y)
#     print('empty_yr_list is ', empty_yr_list)
# print(y)
#     if y not in unique_channel:
#         unique_channel.append(y)
# print(unique_channel)

# df['month'] = pd.DatetimeIndex(df.week).month
# print(df['month'])

# df['week'] = pd.DatetimeIndex(df.week).week
# print(df['week'])

# print(df.loc[0, 'week'].dt.day_name())
#

# df1['week'] = pd.to_datetime(df1['week'], format='%d-%m-%y %I %p')
# print("df1 is latest", df1['week'])


# last_week_date = df[df.week.date > (df.week.date[-1] - pd.Timedelta(weeks=4))]
# print("last_4_week_dates are ", last_week_date)

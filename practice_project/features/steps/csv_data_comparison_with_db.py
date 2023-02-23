import mysql.connector
from behave import *
import csv
import datetime
import pandas as pd
from datetime import date, timedelta
import psycopg2
import prettytable
from pandas._libs.tslibs.timestamps import Timestamp


# import mysql.connector as connection


@given('Read csv data and data from database')
def read_csv_and_db_data(context):
    context.df_csv = pd.read_csv(r'C:/Users/dorugzu/Downloads/Idorsia tdms.inventory_analytics.csv',
                                 converters={i: str for i in range(1000)})
    # print(context.df_csv['week'][0])

    for i, v in context.df_csv.iteritems():
        print(i, v)
        print('type of cols is ', type(i))
        print('type of cols is ', type(v))

    # input_file = csv.DictReader(open(r'C:/Users/dorugzu/Downloads/Idorsia tdms.inventory_analytics.csv'))
    # print('type is ', type(input_file))

    # for row in input_file:
    #     print('row is ', row)
    #     print('type is ', type(row))
    #     for index, data in enumerate(row):
    #         print('index and data is ', index, data)
    # if row['data'] == '24-01-2022':
    #     print(row['data'])

    context.new_df_csv = context.df_csv.to_dict('records')
    print('Method 1')
    # context.new_df_csv.iter
    print(type(context.new_df_csv))
    # print(context.new_df_csv)
    print(context.new_df_csv[1])
    # print(context.df_csv.loc[0, 'id'])
    print(context.new_df_csv[0]['week'])
    print(context.new_df_csv[0]['channel'])
    # print(context.new_df_csv[0]['prod_grp_id'])
    # print(context.new_df_csv[0]['ecs_qs'])
    if context.new_df_csv[0]['week'] == '24-01-2022' and context.new_df_csv[0]['channel'] == 'Retail Pharmacy' and \
            context.new_df_csv[0]['prod_grp_id'] == '65428':
        print('inside if condition')
        print(context.new_df_csv[0]['ecs_qs'])
    # print(type(context.new_df[context.df_csv['week']]))

    # list_week = []
    # for ele in context.new_df_csv:
    #     list_week.append(ele['week'])
    # print('list_week is ', list_week)
    # print('First value of list_week is ', list_week[0])

    # for row in context.new_df_csv:
    #     print(row[0])
    #     for key, value in row.items():
    #         print(key, '->', value)
    #         if row['week'] == '24-01-2022':
    #             print(row['week'])

    # for key, val in context.df_csv.iteritems():
    #     # print(key, val[0], val[1], val[2], val[3])
    #     print(key, val[0])
    #     if val[1] == '05-09-2022' and val[2] == 'Retail Pharmacy' and val[3] == '65428':
    #         print(f'{val[1]} {val[2]} {val[3]} ', val[4])
    #         break

    # def fetch_db_data(context):
    #     try:
    #         context.con = psycopg2.connect(dbname=f'tdms', host='Idorsia.aws.integrichain.com',
    #                                        port='3306', user='icuser', password='int@gri#hai$')
    #         cur = context.con.cursor()
    #         query = f"select week,channel,prod_grp_id,ecs_qs from inventory_analytics limit 1;"
    #         cur.execute(f'{query}')
    #         db_data = cur.fetchall()
    #         print(db_data)
    #         # return db_data
    #     except Exception as e:
    #         print(e)

    # try:
    #     print('Inside Try block')
    #     context.con = psycopg2.connect(dbname=f'tdms', host='Idorsia.aws.integrichain.com',
    #                                    port='3306', user='icuser', password='int@gri#hai$')
    #     cur = context.con.cursor()
    #     query = f"select week,channel,prod_grp_id,ecs_qs from inventory_analytics limit 1;"
    #     cur.execute(f'{query}')
    #     db_data = cur.fetchall()
    #     print(db_data)
    #     # return db_data
    # except Exception as e:
    #     print(e)
    print('Before connection')
    try:
        conn = mysql.connector.Connect(host='Idorsia.aws.integrichain.com', database=f'tdms',
                                       port='3306', user='icuser', password='int@gri#hai$')
        print('connected to DB')
        cur = conn.cursor()
        cur.execute("show databases")
        for i in cur:
            print(i)
    except Exception as e:
        print(e)


@when(
    'Check the data for combination of week,channel and prod_grp_id with DB data for all the respective columns whether its same or different')
def step_impl(context):
    print('step 2')


@then('If there is a mismatch in ecs_qs in 4 weeks or outside of 4 weeks is failure')
def step_impl(context):
    print('step 3')


@then('If there is a mismatch in any channel other then Pharmacy Retailer, its a failure')
def step_impl(context):
    print('step 4')


@then('If there is a mismatch in parameters other then ecs_qs within 4 weeks is pass case')
def step_impl(context):
    print('step 5')


@then('Generate the report')
def step_impl(context):
    print('step 6')

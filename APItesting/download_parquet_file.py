import awswrangler as wr

customer_name = 'aimmune'
prescription_medicine = 'palforzia'
table_name = 'sp_dispense_status_master'

# nbqa_s3_parquet_location = f's3://uat-icdr-data/icdr-uat/{customer_name}/{prescription_medicine}/dimensional/{table_name}'
# nbqa_s3_parquet_location = f's3://nbstage-icdr-data/icdr-nbstage/aimmune/palforzia/dimensional/sp_dispense_status_master/47663b89db7242738acd3b6bdb81e8f9.parquet'
# nbqa_df = wr.s3.read_parquet(path=nbqa_s3_parquet_location, dataset=True)
nbqa_df = wr.s3.read_parquet(f's3://nbstage-icdr-data/icdr-nbstage/aimmune/palforzia/dimensional/sp_dispense_status_master/47663b89db7242738acd3b6bdb81e8f9.parquet')

# nbqa_df = wr.s3.read_parquet(f's3://nbstage-icdr-data/icdr-nbstage/aimmune/palforzia/dimensional/sp_dispense_status_master', dataset=True)
# nbqa_df = nbqa_df.sort_values(by='pharmacy_transaction_id',ascending=True)
# nbqa_df.head()
#nbqa_df = nbqa_df.replace(r'^\s*$', np.NaN, regex=True)
#nbqa_df.to_excel(f'C:/Users/patilan/Desktop/daff23/{customer_name}/{table_name}/nbqa.xlsx',index=False)
nbqa_df.to_csv(f'C:/Users/dorugzu/Downloads/nbstage_Aimmune.csv', index=False)

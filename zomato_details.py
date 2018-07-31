import requests
import json
import pandas as pd
import csv
import sys

if len(sys.argv) < 2:
    print('\n [-] Zomato API Credentials and all paths are not entered ')
    sys.exit(0)
if len(sys.argv) < 4 :
    print('\n [-] All Paths are not entered : ')
    sys.exit(0)

user_api=sys.argv[1]
zomato_cuisins_path=sys.argv[2]
zomato_details_path=sys.argv[3]

header={"Accept": "application/json","user-key": user_api}


'''
#categories
categories=requests.get("https://developers.zomato.com/api/v2.1/categories", headers=header)
categories_json=json.loads(categories.content.decode('utf-8'))

categories_json_df=pd.DataFrame(categories_json)

categories_id=[]

for i in range(len(categories_json_df.index)) :
    for cat,nid in (categories_json_df.loc[i].iloc[0]).items() :
        cat_id=list(nid.values())
        categories_id.append([cat_id[1],cat_id[0]])


#collections

collections=requests.get("https://developers.zomato.com/api/v2.1/collections?city_id=1",headers=header)
collections_json=json.loads(collections.content.decode('utf-8'))

collections_json_df=pd.DataFrame(collections_json)

description=[]
title=[]
res_count=[]
collection_id=[]
for i in range(len(collections_json_df.index)) :
    for coll,coll_det in (collections_json_df.loc[i].iloc[0]).items() :
        description.append(coll_det['description'])
        title.append(coll_det['title'])
        res_count.append(coll_det['res_count'])
        collection_id.append(coll_det['collection_id'])

'''


#cuisins

cuisine = requests.get("https://developers.zomato.com/api/v2.1/cuisines?city_id=1",headers=header)
cuisine_json=json.loads(cuisine.content.decode('utf-8'))

cuisine_json_df=pd.DataFrame(cuisine_json)

cuisine_id_name=[]

for i in range(len(cuisine_json_df.index)) :
    for cui,cui_det in (cuisine_json_df.loc[i].iloc[0]).items() :
        cuisine_id_name.append([cui_det['cuisine_id'],cui_det['cuisine_name']])

with open(zomato_cuisins_path,'w') as cuisine_csv :
    cuisine_csv_w=csv.writer(cuisine_csv)
    cuisine_csv_w.writerow(['Cuisine ID','Cuisine Name'])
    for c_id_name in cuisine_id_name :
        cuisine_csv_w.writerow((c_id_name[0],c_id_name[1]))


'''#establishments

establish=requests.get("https://developers.zomato.com/api/v2.1/establishments?city_id=1",headers=header)
establish_json=json.loads(establish.content.decode('utf-8'))

establish_json_df=pd.DataFrame(establish_json)

establish_id_name=[]

for i in range(len(establish_json_df.index)) :
    for est,est_det in (establish_json_df.loc[i].iloc[0]).items() :
        establish_id_name.append([est_det['id'],est_det['name']])
'''


#location details
entity_id_type=[[6,'zone'],[4,'zone'],[5,'zone'],[7,'zone'],[1,'zone'],[109788,'zone'],[2,'zone'],[600,'zone'],[501,'zone'],
                 [279,'subzone'],[212,'subzone'],[289,'subzone'],[276,'subzone'],[271,'subzone'],[119,'subzone']]

res_id=[]
for id_type in entity_id_type :
    
    loc_details=requests.get("https://developers.zomato.com/api/v2.1/location_details?entity_id="+str(id_type[0])+
                             "&entity_type="+str(id_type[1]),headers=header)
    loc_details_json=json.loads(loc_details.content.decode('utf-8'))

    loc_details_json_df=pd.DataFrame.from_dict(loc_details_json,orient='index')
    
    res_sub_id=loc_details_json_df.loc['nearby_res']
    res_id=res_id+res_sub_id.iloc[0]


#restaurant
column_names=['Restaurant Name','Restaurant Cuisines','Average cost for two','Price Range','Online Delivery','Table Booking','Bogo Offers',
              'User Aggregate Rating','Rating Text','User Votes']

with open(zomato_details_path,'w') as csv_file :
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(col for col in column_names)
    for id_ in res_id :
        restaurant=requests.get("https://developers.zomato.com/api/v2.1/restaurant?res_id="+str(id_),headers=header)
        restaurant_json=json.loads(restaurant.content.decode('utf-8'))

        restaurant_json_df=pd.io.json.json_normalize(restaurant_json)
        csv_writer.writerow((restaurant_json_df['name'].iloc[0],restaurant_json_df['cuisines'].iloc[0],restaurant_json_df['average_cost_for_two'].iloc[0],
                           restaurant_json_df['price_range'].iloc[0],restaurant_json_df['has_online_delivery'].iloc[0],restaurant_json_df['has_table_booking'].iloc[0],
                         restaurant_json_df['include_bogo_offers'].iloc[0],restaurant_json_df['user_rating.aggregate_rating'].iloc[0],
                         restaurant_json_df['user_rating.rating_text'].iloc[0],restaurant_json_df['user_rating.votes'].iloc[0]))
       
        

    


    


       
    

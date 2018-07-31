import pandas as pd
import matplotlib.pyplot as plt
import sys

if len(sys.argv) < 3 :
    print('\n [-] Both (Cuisins.csv and Details.csv) paths are not entered ')
    sys.exit(0)

zomato_cuisins_path=sys.argv[1]
zomato_details_path=sys.argv[2]

zomato_csv=pd.read_csv(zomato_details_path)
zomato_csv_df=pd.DataFrame(zomato_csv)

avg_cost_for_two_mean=zomato_csv_df['Average cost for two'].mean()
avg_cost_for_two_std=zomato_csv_df['Average cost for two'].std()
user_votes_mean=zomato_csv_df['User Votes'].mean()

rating=zomato_csv['Restaurant Name'].groupby(zomato_csv['Rating Text']).nunique()

zomato_cuisine_csv=pd.read_csv(zomato_cuisins_path)
cuisine_names_df=pd.DataFrame(zomato_cuisine_csv['Cuisine Name'])

all_cui=[]
res_cuisines_df=pd.DataFrame(zomato_csv_df['Restaurant Cuisines'])
for ind in res_cuisines_df.index :
    sub_cui=res_cuisines_df.iloc[ind]
    all_cui.extend(*sub_cui.str.split(','))

all_cui_=[cui.strip() for cui in all_cui]  
all_cui_vc=((pd.Series(all_cui_)).value_counts())[:10]




#visualization
##hist

fig,ax1=plt.subplots(2,2,figsize=(15,6.5))

plt.subplots_adjust(left=0.07,bottom=0.05,right=0.98,top=.93,wspace=.18,hspace=.30)
zomato_csv_df['Average cost for two'].plot(ax=ax1[0,0],kind='hist',bins=20,)
ax1[0,0].set_title('Average cost for two')

zomato_csv_df['Price Range'].plot(ax=ax1[0,1],kind='hist',bins=20)
ax1[0,1].set_title('Price Range')

zomato_csv_df['User Aggregate Rating'].plot(ax=ax1[1,0],kind='hist',bins=20)
ax1[1,0].set_title('Aggregate Rating')

zomato_csv_df['User Votes'].plot(ax=ax1[1,1],kind='hist',bins=20)
ax1[1,1].set_title('Votes')


##bar
fig,ax2=plt.subplots(1,3)
plt.subplots_adjust(left=0.05,bottom=0.08,right=0.99,top=.96,wspace=.27,hspace=.4)

xbar=list(range(len(rating.values)))

for i,j in zip(rating.values,xbar) :
    ax2[0].bar(j,height=i)
ax2[0].set_xticks(range(5))
ax2[0].set_xticklabels(rating.index,fontsize='x-small')
ax2[0].set_ylabel('No. of Restaurant',labelpad=8,fontsize=10)
ax2[0].set_title('Rating')


##scatter
(zomato_csv_df[zomato_csv_df['User Aggregate Rating']>0]).plot(ax=ax2[1],x='Average cost for two',
                                                               y='User Aggregate Rating',kind='scatter',color='r',figsize=(15,7))
ax2[1].set_title('Average Cost vs Aggregate Rating')


#cusines counts
hbar=list(range(len(all_cui_vc.values)))

for h,l in zip(all_cui_vc.values,hbar) :
    ax2[2].barh(l,width=h)
ax2[2].set_title('Top 10 Cuisines')
ax2[2].set_yticks(range(10))
ax2[2].set_yticklabels(all_cui_vc.index,fontsize='x-small')
ax2[2].set_ylabel('Cuisines',fontsize=10)
ax2[2].set_xlabel('No. of Restaurants',fontsize=10)



plt.show()


import pandas as pd
import numpy as np

from datetime import datetime


def store_relational_JH_data():
    ''' Transformes the COVID data in a relational data set

    '''

    data_path= r'C:\Users\SurabhiD\ads_covid_19\data\raw\COVID-19\csse_covid_19_data\csse_covid_19_time_series\time_series_covid19_confirmed_global.csv'
    pd_raw=pd.read_csv(data_path)

    pd_data_base=pd_raw.rename(columns={'Country/Region':'country',
                      'Province/State':'state'})

    pd_data_base['state']=pd_data_base['state'].fillna('no')

    pd_data_base=pd_data_base.drop(['Lat','Long'],axis=1)
    test_pd = pd_data_base.set_index(['state','country']).T
    test_pd.stack(level=[0,1])
    pd_relational = test_pd.stack(level=[0,1]).reset_index()
    pd_relational = pd_relational.rename(columns={'level_0': 'date',0:'confirmed'})

    # pd_relational_model=pd_data_base.set_index(['state','country']) \
    #                             .T                              \
    #                             .stack(level=[0,1])             \
    #                             .reset_index()                  \
    #                             .rename(columns={'level_0':'date',
    #                                                0:'confirmed'},
    #                                               )
    pd_relational['date'] = pd.to_datetime(pd_relational['date'])
    #pd_relational_model['date']=pd_relational_model.date.astype('datetime64[ns]')

    pd_relational.to_csv(r'C:\Users\SurabhiD\ads_covid_19\data\processed\COVID_relational_confirmed.csv',sep=';',index=False)
    print(' Number of rows stored: '+str(pd_relational.shape[0]))

if __name__ == '__main__':

    store_relational_JH_data()

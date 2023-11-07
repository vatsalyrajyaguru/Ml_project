import os
import sys
# from Exeption import exeptionhandel
from exeption import CustomException
from logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class dataingestionconfig:
    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','data.csv')


class dataingetion:
    def __init__(self):
        self.ingetion_config =dataingestionconfig()

    def initiate_data_ingetion(self):
        logging.info('enter the data ingetion method')

        try:
            df= pd.read_csv('D:\ml_project\notebook\data\stud.csv')
            logging.info('read the dataset')

            os.makedirs(os.path.dirname(self.ingetion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingetion_config.raw_data_path,index=False,header=True)

            logging.info("train test split initiat")
            train_set,test_set=train_test_split(df,train_size=0.2,random_state=42)

            train_set.to_csv(self.ingetion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingetion_config.test_data_path,index=False,header=True)

            logging.info("ingetion of the data complete")

            return(
                self.ingetion_config.train_data_path,
                self.ingetion_config.test_data_path,
            )

        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj=dataingetion()
    obj.initiate_data_ingetion()

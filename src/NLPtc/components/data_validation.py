import pandas as pd
from src.NLPtc import logger
import os
from src.NLPtc.entity import DataValidationConfig
from sklearn.model_selection import train_test_split


class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir,sep='\t',names=['label','text'])
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                        
            logger.info(validation_status)
        
        except Exception as e:
            raise e
        
    def train_test_spliting(self):
        data = pd.read_csv(self.config.unzip_data_dir,sep='\t',names=['label','text'])
            
        # Split the data into training and test sets. (0.75, 0.25) split.
        x = data.drop('label',axis=1)
        y = data.label
        xtrain, xtest, ytrain, ytest = train_test_split(x,y,random_state=42)

        xtrain.to_csv(os.path.join(self.config.root_dir, "xtrain.csv"),index = False)
        xtest.to_csv(os.path.join(self.config.root_dir, "xtest.csv"),index = False)
        ytrain.to_csv(os.path.join(self.config.root_dir, "ytrain.csv"),index = False)
        ytest.to_csv(os.path.join(self.config.root_dir, "ytest.csv"),index = False)


        logger.info("Splited data into training and test sets")
        logger.info(xtrain.shape)
        logger.info(xtest.shape)
        logger.info(ytrain.shape)
        logger.info(ytest.shape)
            


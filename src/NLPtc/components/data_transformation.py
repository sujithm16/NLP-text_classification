import os
from src.NLPtc import logger
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from src.NLPtc.config.configuration import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    def data_transform(self):
        data= pd.read_csv(self.config.clean_data_path,sep='\t',names=['text','label'])
        
        cor = data['text']
        tv = TfidfVectorizer(max_features=2500)
        x = tv.fit_transform(cor).toarray()
        x = pd.DataFrame(x)
        y = pd.get_dummies(data['label'],dtype=int,drop_first=True)
        
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 0)
        
        X_train.to_csv(os.path.join(self.config.root_dir, "xtrain.csv"),index = False)
        X_test.to_csv(os.path.join(self.config.root_dir, "xtest.csv"),index = False)
        y_train.to_csv(os.path.join(self.config.root_dir, "ytrain.csv"),index = False)
        y_test.to_csv(os.path.join(self.config.root_dir, "ytest.csv"),index = False)
        
        logger.info(X_train.shape)
        logger.info(X_test.shape)
        logger.info(y_train.shape)
        logger.info(y_test.shape)
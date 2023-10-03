import pandas as pd
from src.NLPtc import logger
import os
from src.NLPtc.entity import DataValidationConfig
from nltk.corpus import stopwords
import re
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import numpy as np
stem = PorterStemmer()
lem = WordNetLemmatizer()


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
   
    def data_clean(self):
        data= pd.read_csv(self.config.unzip_data_dir,sep='\t',names=['label','text'])
        corpus = []
        for i in range(0, len(data)):
            review = re.sub('[^a-zA-Z]', ' ', data['text'][i])
            review = review.lower()
            review = review.split()
            
            review = [stem.stem(word) for word in review if not word in stopwords.words('english')]
            review = ' '.join(review)
            corpus.append(review)
                       
        df = pd.DataFrame({'text': corpus})
        df['label'] = data['label']

        df.to_csv(os.path.join(self.config.root_dir, "sms_cleaned.csv"),index = False)
        
           
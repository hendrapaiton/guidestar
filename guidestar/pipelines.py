from email import header
from itemadapter import ItemAdapter
import pandas as pd

class GuidestarPipeline:

    def process_item(self, item, spider):
        self.data = self.data.append(item['name'], ignore_index=True)
        return item

    def open_spider(self, spider):
        self.data = pd.DataFrame()

    def close_spider(self, spider):
        self.data.columns = ['organization_name']
        try:
            check = pd.read_csv('organization.csv')
        except:
            check = pd.DataFrame()
        if check.empty:
            self.data.to_csv('organization.csv', index=False)
        else:
            self.data.to_csv('organization.csv', mode='a', index=False, header=False)

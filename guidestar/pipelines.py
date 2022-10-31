from itemadapter import ItemAdapter
import pandas as pd

class GuidestarPipeline:

    def process_item(self, item, spider):
        self.data = self.data.append(item['name'], ignore_index=True)
        return item

    def open_spider(self, spider):
        self.data = pd.DataFrame()

    def close_spider(self, spider):
        self.data.columns = ['Name']

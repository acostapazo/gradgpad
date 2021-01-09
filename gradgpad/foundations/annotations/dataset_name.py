class DatasetName:
    def __init__(self, value):
        self.value = value

    # @staticmethod
    # def from_item(item):
    #     try:
    #         value = item.info["meta_learning"]["specific"]["fw"].split("/")[0][3:]
    #     except:  # noqa
    #         value = None
    #     return DatasetName(value)

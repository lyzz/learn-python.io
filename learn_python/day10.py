

class RubbishClassification:

    def dry_rubbish(name):

        if name in ["纸巾", "塑料带", "纸尿裤", "口香糖"]:
            return "是干垃圾"
        else:
            return "不是干垃圾"

    def wet_rubbish(self,name):

        if name in ["果皮", "花瓣", "瓜子壳", "厨余" ]:
            return "是湿垃圾"
        else:
            return "不是湿垃圾"
    def harmful_rubbish(self,name):
        # self.name = name
        if name in ["电池", "药物", "指甲油", "油漆"]:
            return "有害垃圾"
        else:
            return "不是有害垃圾"

    print(dry_rubbish("香加皮"))
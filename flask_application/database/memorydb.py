class MemoryDatabase(object):
    db = dict()

    def populate(self, objectcollection):
        self.db = objectcollection

    def set_one(self, id, dataobject):
        self.db[id] = dataobject

    def get_one(self, id):
        return self.db[id]

    def get_all(self):
        return self.db.values()

import db

class DB(db.DB):
    def create_cell(self, input):
        self.c.code.insert({'input':input})
    
    def get_unevaluated_cells(self):
        return self.c.code.find({'output':{'$exists': False}})
    
    def get_evaluated_cells(self):
        return self.c.code.find({'output':{'$exists': True}})
    
    def set_output(self, id, output):
        self.c.code.update({'_id':id}, {'$set':{'output':output}})
    
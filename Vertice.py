class Vertice(object):

    def __init__(self, label):
        self.label = label
        self.arestas = {}

    def set_label(self, label):
        self.label = label

    def get_label(self):
        return self.label

import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        pass
    def findPath(self):
        self.bestPath=[]
        self.bestScore=0
        for l in self.grafo.nodes:
            self.ricorsione([l])
        return self.bestPath, self.bestScore
    def ricorsione(self, parziale):
        #trova il cammino piu lungo: score = len(soluzione)
        if self.termine(parziale): #tutti i vicini sono nel parziale
            if self.migliore(parziale): #è piu lungo della migliore
                self.bestPath = copy.deepcopy(parziale)
                self.bestScore = len(self.bestPath)
            return
        print("chiamo ricorsione")
        for n in self.grafo.neighbors(parziale[-1]):
            if n not in parziale:
                parziale.append(n)
                self.ricorsione(parziale)
                parziale.pop()

    def termine(self, parziale):
        for n in self.grafo.neighbors(parziale[-1]):
            if n not in parziale:
                return False
        return True
    def migliore(self,parziale):
        if len(parziale)> self.bestScore:
            return True
        return False


    def creaGrafo(self, loc):
        self.grafo = nx.Graph()
        self.grafo.add_nodes_from(loc)
        for n1 in loc:
            for n2 in loc:
                if n1 != n2:
                    if DAO.esisteArco(n1, n2)[0] > 0:
                        self.grafo.add_edge(n1, n2, weight=DAO.getPesi(n1, n2)[0])
                        print(n1,n2)


    def statistica(self, location):
        connessioni = nx.connected_components(self.grafo)
        for c in connessioni:
            if location in c:
                return location, c
    def getPeso(self,n1,n2):
        print (n1,n2)
        return self.grafo[n1][n2]["weight"]
    def stampa(self):
        return f"num nodi: {len(self.grafo.nodes)}, num archi: {len(self.grafo.edges)}"





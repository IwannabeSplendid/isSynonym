class node:
    def __init__(self, name, syn = None):
        if syn is None:
            self.syn = set()
        else:
            self.syn = syn
        self.name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name + " " + str(self.syn)


class Graph():
    def __init__(self, nodes = None):
        if nodes is None:
            self.nodes = {}
        else:
            self.nodes = nodes

    def __repr__(self):
        return str(self.nodes)

    def __str__(self):
        return str(self.nodes)

def isSynonym(w1, w2, syn_dict):
    w1 = w1.lower()
    w2 = w2.lower()
    if(w1==w2):
        return "synonyms"
    else:
        try:
            if w2 in syn_dict.get(w1):
                return "synonyms"
        except:
            try:
                if w1 in syn_dict.get(w2):
                    return "synonyms"
            except:
                return "different"
    return "different"

def updateSet(w1, w2, syn_set):
    w1, w2 = w1.lower(), w2.lower()
    graph1, graph2 = Graph({w1}), Graph({w2})
    not_in_dict1, not_in_dict2 = True, True

    #Find coressponding graphs
    for graph in syn_set:
        if w1 in graph.nodes:
            graph1 = graph
            not_in_dict1 = False
        if w2 in graph.nodes:
            graph2 = graph
            not_in_dict2 = False

    #If there is none create it and add it
    if not_in_dict1:
        syn_set.add(graph1)
    if not_in_dict2:
        syn_set.add(graph2)

    #if there are already not in the same graph, update one of the graph and remove the other one
    if graph1 != graph2:
        graph1.nodes.update(graph2.nodes)
        syn_set.remove(graph2)


def createDict(syn_set):
    syn_dict = dict()
    for graph in syn_set:
        for word in graph.nodes:
            syn_dict.update({word : graph.nodes})
    return syn_dict


if __name__ == '__main__':
    input_data = open("example_big.in", "r")
    right_answer = open("example_big.out", "r")

    num_testcase = int(input_data.readline())

    for testcase in range(num_testcase):
        # Dictionary part
        syn_set = set()
        n = int(input_data.readline())

        for i in range(n):
            w1, w2 = input_data.readline().split()
            updateSet(w1, w2, syn_set)
        print(syn_set)
        syn_dict = createDict(syn_set)

        # Testing part
        m = int(input_data.readline())
        for i in range(m):
            w1, w2 = input_data.readline().split()
            r_answer = right_answer.readline().strip()
            print(isSynonym(w1, w2, syn_dict)==r_answer)









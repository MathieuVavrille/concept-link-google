import subprocess
import sys
from graphviz import Graph

command = ["-H", """Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8""", "--compressed", "-H", """Accept-Language: fr-FR,en-US;q=0.7,en;q=0.3""", "-H", 'Cache-Control: max-age=0', "-H", 'Connection: keep-alive', "-H", 'Cookie: NID=127=DlMcKvbb576AcaA3wNMf-mi3wD28c28aXH0DzpKYlUvDnPoGm0FTgNwBGkS398RS9gT7oe3_FRAVf7tAB_voibocV1fUZAVNQOM0ZPmwRipBwDYagfHgeS6QOGHPFO04CysZQsvMh3AtpF9z5DW2WJGBD0DYV1ADWkgQ4kJma3e3e_wdRJFAHNrnYtLUeHcf5unSBLGcSbfWXTt3aaH0AtgwtPp3L2ILNPLRTWyXPDZEOfxL_OOM6cnRQ0b61_AXJ7A; CONSENT=YES+FR.fr+20150906-13-0; SID=wgRRxS1UxKzPX7sB4hVJDsdoiAa9Rex2KSVh6r8rw63I9vjFiYgMhlkI2xRBm0yOK4xQhA.; HSID=AzlNklXaHjCTFVRR_; SSID=APa7Dm1LTllY7tOPx; APISID=0soWdi59XMT-15Wt/AAZw-qQD1lx7_FFmv; SAPISID=QUaWOdLPLg1QGSHQ/A-o90f8pYzktRsfeE; 1P_JAR=2018-3-30-19; OGPC=19005035-1:; DV=w2id59Bk6K1OUPBfaeE_xvMUwnqHJ1b5Jy26m9MjHgYAAAAGqafRlXCnmAEAAGC9VCFbQNaLZwAAAA', "-H", 'Host: www.google.fr', "-H", 'Upgrade-Insecure-Requests: 1', "-H", 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0']

class UnionFind:
    def __init__(self, size):
        self.data = [i for i in range(len(graph))]
    
    def has_one_component(self):
        for i in self.data:
            if i != 0:
                return False
        return True
    
    def same_component(self, i, j):
        return self.data[i] == self.data[j]
    
    def combine(self, i, j):
        min_id = self.data[i]
        max_id = self.data[j]
        if min_id > max_id:
            min_id, max_id = max_id, min_id
        for k in range(len(self.data)):
            if self.data[k] == max_id:
                self.data[k] = min_id

def get_nb_results(concept):
    first_el = """https://www.google.fr/search?client=ubuntu&channel=fs&q="""+concept+"""&ie=utf-8&oe=utf-8&gfe_rd=cr&dcr=0&ei=apW-WvvRNIvu8wef57vQCg"""
    first_part = """'https://www.google.fr/search?client=ubuntu&channel=fs&q="""
    second_part = """&ie=utf-8&oe=utf-8&gfe_rd=cr&dcr=0&ei=c02-WoyfAoTA8gfQooZQ' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' --compressed -H 'Accept-Language: fr-FR,en-US;q=0.7,en;q=0.3' -H 'Cache-Control: max-age=0' -H 'Connection: keep-alive' -H 'Cookie: NID=126=PmsK8wb0vwNLK1aFwtiGzdDoF1MLqyLci6G-9NXlAAu5SD-xjZOG-kolrSjvy-V6fV5bOseWPUtKtdBiTPFWBKKBd1tLufFsDIR2_-aTJLx0GkZhN0ravQEfa046ZQANpQxD64SSYUq9wNJ5yxOq13O2E7-NifhQxOg8eOxGwKGIH1nGjpIU1ftWgPLk6-9Fk1Dr9GuAjGbc25x5yT7vj-KDw4weCeyDm-zRALsbEMu4FIS2S8XaKXGXYumntpuvLic; CONSENT=YES+FR.fr+20150906-13-0; SID=wgRRxS1UxKzPX7sB4hVJDsdoiAa9Rex2KSVh6r8rw63I9vjFiYgMhlkI2xRBm0yOK4xQhA.; HSID=AzlNklXaHjCTFVRR_; SSID=APa7Dm1LTllY7tOPx; APISID=0soWdi59XMT-15Wt/AAZw-qQD1lx7_FFmv; SAPISID=QUaWOdLPLg1QGSHQ/A-o90f8pYzktRsfeE; 1P_JAR=2018-3-30-14; OGPC=19005035-1:; DV=w2id59Bk6K1OIBy4P1MyROuQ2w52J5bs_5BZ6oTAgAIAAIAGwtOLQBGLqwAAAOCpfvSir50KMgAAAA' -H 'Host: www.google.fr' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0' > test.txt"""
    request = subprocess.run(["curl", first_el] +command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    text_request = request.stdout.decode()
    part_number = text_request.split("Environ")[1].split("résultat")[0][1:].split("\xa0")[:-1]
    return int("".join(part_number))

def distance(c1, c2, cc):
    return cc/max(c1,c2)

def get_concepts(verbose, file_to_open):
    with open(file_to_open, 'r') as concept_list:
        list_to_concept = concept_list.read().split()
    if verbose:
        print("File "+file_to_open+" has been read")
    concept_to_list = {}
    for i in range(len(list_to_concept)):
        concept_to_list[list_to_concept[i]] = i
    return list_to_concept, concept_to_list

def generate_graph(verbose, list_to_concept):
    graph = [[0]*len(list_to_concept) for i in list_to_concept]
    results_per_concept = []
    count = 0
    for concept in list_to_concept:
        nb_results = get_nb_results(concept)
        count += 1
        if verbose:
            print('Concept "'+concept+'" has %d results'%(nb_results))
            print("Computing : %.2f%%"%(count*200/(len(graph)*(len(graph)+1))))
        results_per_concept.append(nb_results)
    for i in range(len(graph)):
        for j in range(i+1, len(graph[i])):
            nb_results = get_nb_results(list_to_concept[i]+"+"+list_to_concept[j])
            count += 1
            if verbose:
                print('Concepts "'+list_to_concept[i]+'" and "'+list_to_concept[j]+'" have %d results'%(nb_results))
                print("Computing : %.2f%%"%(count*200/(len(graph)*(len(graph)+1))))
            graph[i][j] = distance(results_per_concept[i], results_per_concept[j], nb_results)
    return graph, results_per_concept

def max_spanning_tree(verbose, graph):
    edge_list = []
    for i in range(len(graph)):
        for j in range(i+1, len(graph)):
            edge_list.append((graph[i][j], i, j))
    edge_list.sort()
    output_edges = []
    union_find = UnionFind(len(graph))
    while edge_list != []:
        next_edge = edge_list.pop()
        if not union_find.same_component(next_edge[1], next_edge[2]):
            union_find.combine(next_edge[1], next_edge[2])
            output_edges.append((next_edge[1], next_edge[2]))
    return output_edges

def edge_list_to_dot(verbose, edges, names):
    graph = Graph(format = 'pdf')
    for edge in edges:
        graph.edge(names[edge[0]], names[edge[1]])
    graph.render("result_graph/output")

if __name__ == "__main__":
    list_to_concept, concept_to_list = get_concepts(True, sys.argv[1])
    distance_graph, results_per_concept = generate_graph(True, list_to_concept)
    graph = [[0,1,2,3,4,5,6,7,8,9],
             [0,0,3,5,4,8,9,6,8,6],
             [0,0,0,4,2,5,7,8,6,9],
             [0,0,0,0,2,3,4,8,5,2],
             [0,0,0,0,0,1,4,3,8,2],
             [0,0,0,0,0,0,2,4,1,1],
             [0,0,0,0,0,0,0,3,5,1],
             [0,0,0,0,0,0,0,0,5,3],
             [0,0,0,0,0,0,0,0,0,6],
             [0,0,0,0,0,0,0,0,0,0]]
    print(graph)
    output_edges = max_spanning_tree(True, distance_graph)
    edge_list_to_dot(True, output_edges, list_to_concept)
    print(output_edges)








































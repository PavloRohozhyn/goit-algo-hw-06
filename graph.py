import networkx as nx

def graph():
    """ 
    Create Graph. (Internet Network)
    ISP       - Internet Service Provider.
    Router    - Internet Router.
    User      - Internet User.
    """
    G = nx.Graph()
    # Add Nodes
    nodes = ['ISP_1', 'ISP_2', 'ISP_3', 'Router_1', 'Router_2', 'Router_3', 'User_1', 'User_2', 'User_3', 'User_4']
    G.add_nodes_from(nodes)
    # Add Edges

    edges = [
        ('ISP_1', 'Router_1'), 
        ('ISP_1', 'Router_2'),
        ('ISP_2', 'Router_2'), 
        ('ISP_2', 'Router_3'),
        ('ISP_3', 'Router_1'), 
        ('ISP_3', 'Router_3'),
        ('Router_1', 'User_1'), 
        ('Router_1', 'User_2'),
        ('Router_2', 'User_3'), 
        ('Router_3', 'User_4')]
    G.add_edges_from(edges)
    return G
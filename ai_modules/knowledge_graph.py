from py2neo import Graph

graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

def query_player_profile(player_id):
    data = graph.run("MATCH (p:Player {id: $id})-[]-(m:Match) RETURN p, m", id=player_id).data()
    return {"player_id": player_id, "profile": data}

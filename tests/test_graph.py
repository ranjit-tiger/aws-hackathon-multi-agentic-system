from app.graph.builder import build_graph

def test_graph_builds():
    assert build_graph() is None

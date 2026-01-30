from core.graph import build_graph

app = build_graph()

result = app.invoke({"company": "Tesla"})

print(result["analysis"])

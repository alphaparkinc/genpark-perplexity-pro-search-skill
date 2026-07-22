from client import PerplexityProSearchClient
client = PerplexityProSearchClient()
result = client.search(
    query="What are the most significant AI breakthroughs in 2026 so far?",
    mode="deep_research",
    models=["gpt-5.2", "claude-4.6", "gemini-3.1-pro"]
)
print(f"Answer: {result['answer'][:120]}...")
print(f"Citations ({len(result['citations'])}):")
for c in result["citations"]:
    print(f"  [{c['date']}] {c['title']}")
print(f"Model Council:")
for m in result["model_council"]:
    print(f"  {m['model']}: {m['opinion'][:60]}...")

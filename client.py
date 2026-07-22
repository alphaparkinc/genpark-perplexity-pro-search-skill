import hashlib

class PerplexityProSearchClient:
    MOCK_SOURCES = [
        {"title": "Nature: AI in scientific discovery 2026", "url": "https://nature.com/ai-2026", "date": "2026-07-01"},
        {"title": "MIT Tech Review: Foundation model benchmarks", "url": "https://technologyreview.com/llm-bench", "date": "2026-06-15"},
        {"title": "arXiv: Scaling laws revisited", "url": "https://arxiv.org/abs/2606.12345", "date": "2026-06-20"},
        {"title": "Stanford HAI Annual Report 2026", "url": "https://hai.stanford.edu/report", "date": "2026-05-30"},
    ]
    MODEL_OPINIONS = {
        "gpt-5.2":        "Based on recent papers, the evidence strongly supports this conclusion.",
        "claude-4.6":     "I find this well-supported, though edge cases in low-resource settings merit caution.",
        "gemini-3.1-pro": "Concur with the synthesis. I would add that regulatory factors may shift this by 2027.",
    }

    def search(self, query: str, mode: str = "pro", models: list = None) -> dict:
        if models is None:
            models = ["gpt-5.2", "claude-4.6", "gemini-3.1-pro"]
        # Simulate ranked, cited answer
        qhash = hashlib.md5(query.encode()).hexdigest()[:6]
        answer = (
            f"[Pro Search | {mode.upper()}] Based on analysis of {len(self.MOCK_SOURCES)} sources: "
            f"'{query}' — The current consensus indicates significant progress in this area as of Q2 2026, "
            f"with key findings corroborated across peer-reviewed and institutional sources. (ID: {qhash})"
        )
        council = [{"model": m, "opinion": self.MODEL_OPINIONS.get(m, "Agrees with primary synthesis.")} for m in models]
        return {"answer": answer, "citations": self.MOCK_SOURCES[:3], "model_council": council}

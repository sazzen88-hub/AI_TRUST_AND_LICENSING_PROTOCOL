# MACH_ENGINE_V1 — Public Playground Engine
# This is a simplified, experimental engine for testing ideas.
# It does NOT represent any private ATLP logic.

class MachEngineV1:
    def __init__(self):
        self.variables = {
            "signal_strength": 0,
            "context_depth": 0,
            "coherence": 0,
            "stability": 0,
            "synthetic_factor": 0  # fake variable — safe placeholder
        }

    def configure(self, **kwargs):
        """
        Allows users to adjust engine variables.
        Example: engine.configure(signal_strength=72)
        """
        for key, value in kwargs.items():
            if key in self.variables:
                self.variables[key] = value

    def evaluate(self, text: str) -> dict:
        """
        Returns a simulated evaluation score.
        Completely fictional. Safe for public use.
        """
        length_factor = min(len(text) // 10, 100)

        score = (
            self.variables["signal_strength"] * 0.25 +
            self.variables["context_depth"] * 0.25 +
            self.variables["coherence"] * 0.20 +
            self.variables["stability"] * 0.20 +
            self.variables["synthetic_factor"] * 0.10 + 
            length_factor
        )

        return {
            "input_length": len(text),
            "engine_variables": self.variables,
            "simulated_score": round(score, 2)
        }


# OPTIONAL manual test:
if __name__ == "__main__":
    engine = MachEngineV1()
    engine.configure(signal_strength=58, coherence=90, stability=45)
    result = engine.evaluate("Hello world, this is a playground experiment.")
    print(result)

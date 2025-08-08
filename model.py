import random
import math
from copy import deepcopy
from events import EVENT_LIBRARY

class Simulation:
    def __init__(self):
        # Enterprise setup
        self.departments = [
            {"name":"Operations","readiness":55,"adoption":0.05,"p":0.02,"q":0.25},
            {"name":"Customer Service","readiness":45,"adoption":0.04,"p":0.02,"q":0.25},
            {"name":"Sales & Marketing","readiness":50,"adoption":0.04,"p":0.02,"q":0.25},
            {"name":"Finance & Legal","readiness":35,"adoption":0.03,"p":0.02,"q":0.25},
            {"name":"IT & Data Science","readiness":70,"adoption":0.12,"p":0.03,"q":0.35},
            {"name":"HR & Learning","readiness":40,"adoption":0.03,"p":0.02,"q":0.25},
        ]
        self.sentiment = 60.0
        self.budget = 15_000_000
        self.round = 1
        self.total_rounds = 12
        self.speed_multiplier = 1.0
        self.log = []  # Append dicts per round

        # Random seed for reproducibility (can change for variability)
        random.seed(42)

    # --- KPIs ---
    def overall_adoption(self):
        return 100.0 * sum(d["adoption"] for d in self.departments) / len(self.departments)

    def current_event(self):
        # Pull event by round from library
        idx = min(self.round-1, len(EVENT_LIBRARY)-1)
        return EVENT_LIBRARY[idx]

    # --- Simulation mechanics ---
    def apply_decision(self, option):
        # Deduct cost
        self.budget -= option["cost"]

        # Update targeted or enterprise-wide parameters
        # Effects structure: list of dicts with keys type, target, value
        for eff in option.get("effects", []):
            etype = eff["type"]
            tgt = eff.get("target", "enterprise")
            val = eff["value"]

            if etype == "sentiment":
                self.sentiment = max(0, min(100, self.sentiment + val))

            elif etype == "budget":
                self.budget = max(0, self.budget + val)

            elif etype == "adoption_boost":
                # direct bump to adoption%
                for d in self._iter_targets(tgt):
                    d["adoption"] = min(0.999, d["adoption"] + val/100.0)

            elif etype == "p_adjust":
                for d in self._iter_targets(tgt):
                    d["p"] = max(0.001, d["p"] + val)

            elif etype == "q_adjust":
                for d in self._iter_targets(tgt):
                    d["q"] = max(0.05, d["q"] + val)

            elif etype == "readiness":
                for d in self._iter_targets(tgt):
                    d["readiness"] = max(0, min(100, d["readiness"] + val))

        # Random risk resolution (if any risk text present, small chance of downside)
        if option.get("risks"):
            if random.random() < 0.2:
                # downside: sentiment dip and budget hit
                self.sentiment = max(0, self.sentiment - 5)
                self.budget = max(0, self.budget - 100_000)

        # Log
        self.log.append({
            "round": self.round,
            "decision": option["label"],
            "cost": option["cost"],
            "sentiment": self.sentiment,
            "budget": self.budget,
            "dept_state": deepcopy(self.departments)
        })

    def advance_round(self):
        # Run diffusion for each department once per round
        for d in self.departments:
            s_mult = (0.5 + self.sentiment/100.0)  # 1.1 at 60 sentiment, ranges 0.5–1.5
            s_mult = max(0.5, min(1.5, s_mult))
            readiness_mult = 0.5 + d["readiness"]/100.0  # 0.85 at 70 readiness

            p = d["p"] * s_mult * readiness_mult * self.speed_multiplier
            q = d["q"] * s_mult * readiness_mult * self.speed_multiplier

            A = d["adoption"]
            growth = p*(1-A) + q*A*(1-A)
            d["adoption"] = min(0.999, max(0.0, A + growth))

        # Random enterprise events (small)
        if random.random() < 0.15:
            self.sentiment = max(0, min(100, self.sentiment + random.choice([-3, -2, 2, 3])))

        self.round += 1

    # Helpers
    def _iter_targets(self, target):
        if target == "enterprise":
            return self.departments
        # target may be a list of unit names
        names = target if isinstance(target, list) else [target]
        return [d for d in self.departments if d["name"] in names]

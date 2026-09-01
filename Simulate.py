import numpy as np
from collections import Counter

N_SIMS = 1_000_000
np.random.seed(42)

matches = {
    "ML Maxline Vitebsk vs Belshina": {"home_xg": 2.35, "away_xg": 0.55},
    "Dinamo Minsk vs Naftan":         {"home_xg": 2.20, "away_xg": 0.70},
    "Yantra Gabrovo vs Pirin":        {"home_xg": 2.10, "away_xg": 0.65},
    "Levski Sofia vs Slavia Sofia":   {"home_xg": 0.85, "away_xg": 1.95},
    "Bayern vs Osnabrück":            {"home_xg": 0.45, "away_xg": 3.40},
    "AEK Athens vs Nestos":           {"home_xg": 0.40, "away_xg": 3.10},
    "Flamengo vs Mirassol":           {"home_xg": 2.15, "away_xg": 0.75},
}

def simulate_match(home_xg, away_xg, n_sims=N_SIMS):
    home_goals = np.random.poisson(home_xg, n_sims)
    away_goals = np.random.poisson(away_xg, n_sims)
    
    home_wins = np.sum(home_goals > away_goals)
    draws     = np.sum(home_goals == away_goals)
    away_wins = np.sum(home_goals < away_goals)
    
    scores = list(zip(home_goals, away_goals))
    top_scores = Counter(scores).most_common(8)
    
    return {
        "home_win_%": round(home_wins / n_sims * 100, 2),
        "draw_%":     round(draws / n_sims * 100, 2),
        "away_win_%": round(away_wins / n_sims * 100, 2),
        "top_scores": top_scores
    }

print(f"Running {N_SIMS:,} simulations per match...\n")

for name, xg in matches.items():
    result = simulate_match(xg["home_xg"], xg["away_xg"])
    
    print(f"=== {name} ===")
    print(f"Home Win: {result['home_win_%']}%")
    print(f"Draw:     {result['draw_%']}%")
    print(f"Away Win: {result['away_win_%']}%")
    print("Most common scorelines:")
    for (h, a), count in result["top_scores"]:
        pct = count / N_SIMS * 100
        print(f"  {h}-{a}: {pct:.2f}%")
    print()

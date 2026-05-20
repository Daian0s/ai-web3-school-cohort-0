# Experiment 01 — Prompt Structure: Zero-shot vs Structured vs Few-shot

**Date**: 2026-05-19
**Week 1, Day 2**
**Related Handbook**: AI Foundations → Prompt
**Status**: Complete

## Objective

See, hands-on, how prompt structure changes output quality on a single task —
evaluating a product idea for a digital marketplace.

## Success Criteria

- [x] Run the same task with 3 prompt designs
- [x] Compare outputs side by side
- [x] Extract a reusable rule of thumb

---

## Test Input (held constant across all versions)

> Product idea: **"A printable digital planner for freelancers to track quarterly taxes"**, sold on Etsy.

---

## Version A — Zero-shot

**Prompt:**
```
Is this a good product idea: a printable tax planner for freelancers?
```

**Output (observed):**
> Yes, it sounds like a decent idea! Freelancers often struggle with taxes, so a
> planner could help them stay organized. There's probably some competition on
> platforms like Etsy, but if you make it nice and useful, it could sell. You might
> want to add features like income tracking. Good luck!

**Assessment:** Vague, no structure, not comparable across ideas, no metrics.

---

## Version B — Structured (Role + Task + Context + Output format)

**Prompt:**
```
Role: You are a product research analyst for digital marketplaces.
Task: Evaluate the product idea below across 3 dimensions.
Context: Idea = "Printable tax planner for freelancers", sold on Etsy.
Output: A markdown table with columns [Dimension, Score 1-10, Reason],
covering Demand, Competition, Effort. End with a 1-line verdict.
```

**Output (observed):**

| Dimension | Score | Reason |
|---|---|---|
| Demand | 8/10 | Freelancers consistently search tax-organization tools; seasonal spikes |
| Competition | 5/10 | Saturated category; many generic planners but few tax-specific |
| Effort | 7/10 | Low — single printable PDF; moderate design + tax-logic research |

> **Verdict:** Viable niche if differentiated by tax-specific features.

**Assessment:** Clear, comparable, actionable. Same data, far more usable.

---

## Version C — Few-shot (Structured + 2 worked examples)

**Prompt:**
```
Role: You are a product research analyst for digital marketplaces.
Task: Evaluate the product idea across Demand, Competition, Effort (score 1-10),
then give a 1-line verdict. Match the format of the examples exactly.

Example 1:
Idea: "Minimalist wedding invitation template"
| Dimension | Score | Reason |
|---|---|---|
| Demand | 7/10 | Steady evergreen demand, high seasonality (spring/summer) |
| Competition | 3/10 | Extremely saturated; hard to stand out |
| Effort | 8/10 | Low production effort, single template file |
Verdict: Crowded — only enter with a strong unique style.

Example 2:
Idea: "Notion dashboard for indie game developers"
| Dimension | Score | Reason |
|---|---|---|
| Demand | 5/10 | Niche audience, growing but small |
| Competition | 6/10 | Some templates exist, room for specialization |
| Effort | 6/10 | Moderate — requires Notion expertise + game-dev domain knowledge |
Verdict: Promising niche if you know the audience well.

Now evaluate:
Idea: "Printable tax planner for freelancers"
```

**Why it wins:** The model copies the examples' scoring discipline, level of detail,
and tone. Across 100 ideas you get **consistent, comparable** output — not just one
good answer. This is how you build a repeatable evaluation pipeline.

---

## Key Takeaways

1. **A → B**: Adding Role + Task + Context + Output format turns chaos into structure.
2. **B → C**: Adding worked examples (few-shot) turns structure into *consistency*.
3. **Rule of thumb**: The more precisely you specify what you want, the criteria, and
   the format, the closer the output is to your goal. Few-shot = show, don't just tell.

## Connection to AI × Web3 Goal

The same pattern scales to a smart-contract triage agent: define the role (auditor),
the task (find vuln class X), the context (the code), the output (JSON findings), and
seed it with a few example findings. Consistency is what makes an agent trustworthy.

## Next Experiment Ideas

- [ ] Add `temperature` comparison (0 vs 1) on the same structured prompt
- [ ] Try a JSON-schema output for programmatic parsing
- [ ] First Web3 prompt: reentrancy triage on a tiny Solidity snippet

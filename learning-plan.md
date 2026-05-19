# Personal Learning Plan

## Overview

A structured but flexible roadmap to move from **AI × Web3 concepts** → **building agents that execute on-chain**.

## Phase 1: Foundations (Week 1–2)

### Week 1: AI Concepts
**Handbook Chapters**:
- LLM (understand how models work)
- Prompt (structure effective instructions)
- Context (manage token windows, retrieval)

**Minimum Path** (2–3 hours):
- Read LLM chapter
- Understand transformer basics
- Try one prompt refinement with Claude

**Recommended Path** (4–5 hours):
- Read LLM + Prompt + Context chapters
- Experiment with context window management
- Draft 2–3 example prompts for Web3 scenarios

**Challenge Path** (6+ hours):
- Deep dive: compare LLM architectures (GPT, Claude, open models)
- Read RAG chapter
- Prototype a simple RAG retrieval pipeline

### Week 2: Web3 Concepts
**Handbook Chapters**:
- Wallet (keypairs, signing, HD wallets)
- Smart Contract (bytecode, execution, state)
- Dev Stack (RPC, libraries, testing)

**Minimum Path** (2–3 hours):
- Read Wallet + Smart Contract chapters
- Understand contract interaction flow

**Recommended Path** (4–5 hours):
- Read all three chapters
- Set up Foundry or Hardhat locally
- Deploy a simple contract to testnet

**Challenge Path** (6+ hours):
- Trace a real transaction on Etherscan
- Write a contract test
- Understand storage layout

---

## Phase 2: Bridge Concepts (Week 3–4)

### Week 3: Agent Fundamentals
**Handbook Chapters**:
- Agent (decision loops, tool calling)
- Frameworks (use Claude, LangChain, or similar)
- Web3 Tool Use (calling contracts from code)

**Minimum Path** (2–3 hours):
- Understand agent loop: observe → decide → act → observe
- Read Web3 Tool Use chapter
- Review one example agent

**Recommended Path** (4–5 hours):
- Build a simple agent that reads blockchain state (balance check, token info)
- Use Claude API + ethers.js or web3.py
- Document the workflow

**Challenge Path** (6+ hours):
- Build agent that can execute transactions
- Implement safety checks (dry-run before broadcast)
- Add guardrails for fund management

### Week 4: Agent Wallet & Execution
**Handbook Chapters**:
- Agent Wallet (fund management, signing)
- Agent Workflow (end-to-end execution)
- AI Security (verification, sandboxing)

**Minimum Path** (2–3 hours):
- Understand wallet derivation for agents
- Review security considerations

**Recommended Path** (4–5 hours):
- Implement agent with testnet fund management
- Sign a transaction from an agent
- Log execution traces

**Challenge Path** (6+ hours):
- Design multi-step workflow (swap + stake + redeem)
- Implement retry logic
- Add transaction monitoring

---

## Phase 3: Product & Security (Week 5–6)

### Week 5: Product Research & Use Cases
**Handbook Chapters**:
- Agentic Commerce (autonomous buying/selling)
- DeFi (protocol mechanics, yields, risks)
- Governance AI (voting workflows)

**Minimum Path** (2–3 hours):
- Research 2 AI × Web3 product ideas
- Document market gaps

**Recommended Path** (4–5 hours):
- Write a one-page product spec for an AI agent use case
- Map to existing protocols (Uniswap, Aave, etc.)
- Identify technical requirements

**Challenge Path** (6+ hours):
- Prototype a product flow (e.g., AI portfolio rebalancer, yield arbitrageur)
- Document assumptions & risks

### Week 6: Security & Verification
**Handbook Chapters**:
- Security (contract audit mindset)
- Verifiable AI (proving behavior)
- AI Privacy (data handling)

**Minimum Path** (2–3 hours):
- Review common smart contract vulnerabilities
- Understand formal verification basics

**Recommended Path** (4–5 hours):
- Audit a simple contract for security issues
- Write invariant tests
- Document findings

**Challenge Path** (6+ hours):
- Contribute security feedback to Handbook
- Compare audit tools (Slither, Aderyn, etc.)
- Explore formal verification with Halmos

---

## Phase 4: Integration & Projects (Week 7+)

### Mini-Project Ideas

1. **AI Wallet Monitor**
   - Agent that watches your wallet
   - Alerts on unusual activity
   - Suggests rebalancing based on market conditions

2. **Yield Optimizer Agent**
   - Monitors DeFi protocols
   - Routes funds to best yields
   - Reports performance

3. **Contract Analyzer Agent**
   - Reads contracts from GitHub/Etherscan
   - Generates security report
   - Suggests improvements

4. **DAO Governance Agent**
   - Summarizes proposals
   - Simulates voting outcomes
   - Recommends positions

---

## Daily Rhythm

- **Morning** (optional): Review Handbook chapters, set day's learning path
- **Work**: Read, experiment, build
- **Check-in**: Draft daily note + WCB check-in
- **Review**: Reflect on blockers, adjust next day

---

## Metrics

Track in `daily/` notes:
- Handbook chapters read
- Code experiments completed
- Questions/blockers encountered
- Handbook feedback submitted

---

## Notes

- **Flexibility**: Skip phases if a topic isn't relevant; adjust based on interests
- **Pace**: These are suggested weeks; move faster/slower as needed
- **Projects**: Start mini-projects when Phase 2 is comfortable (Week 4–5)
- **Feedback**: Track Handbook issues in `handbook-feedback/` as you go

---

**Last Updated**: 2026-05-19

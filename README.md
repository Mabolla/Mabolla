<div align="center">

# Mabolla

### Onchain product builder

**Base · Arc / Circle · Payment infrastructure · Smart contracts · Open source**

I build and test usable onchain products—from contract design and public testnet deployment to verified transactions and production-facing applications.

</div>

---

## Featured Builds

### [`arc-paylink`](https://github.com/Mabolla/arc-paylink) — Verifiable USDC settlement on Arc

Turns an invoice, milestone, or agent task into a shareable USDC payment with a verifiable source-to-destination audit trail.

- Arc and Base Sepolia payment routes with Circle CCTP settlement on Arc
- Google-authenticated Circle smart-account recipient onboarding
- Deterministic claimable escrow with EIP-712 and EIP-1271 support
- Private, append-only settlement records and controlled, non-executable recovery plans
- Verified end-to-end Arc Testnet payment, bridge, smart-account, and claim flows

**Stack:** `TypeScript` · `Next.js` · `Solidity` · `Circle App Kit` · `CCTP` · `USDC` · `Arc`

---

### [`arc-environmental-retainage`](https://github.com/Mabolla/arc-environmental-retainage) — Environmental performance assurance

A programmable retainage system for environmental commitments, deployed on Arc Testnet.

- USDC-funded milestone lifecycle
- Separate owner, contractor, verifier, and remediation roles
- Evidence anchoring with bounded review and cure periods
- Tested Solidity contracts and a public Next.js application

[**Live app**](https://mabolla.github.io/arc-environmental-retainage/) · [**Testnet contract**](https://testnet.arcscan.app/address/0x19fbf0B85e66d68D312cD18D04A1a789107387FF)

**Stack:** `Solidity` · `Hardhat` · `Next.js` · `ethers.js` · `USDC` · `Arc`

---

## Base Builds

### [`base-receipt`](https://github.com/Mabolla/base-receipt) — Base USDC payments and MCP receipts

A Base Mainnet USDC payment flow for wallet users and agents, with independent settlement verification before issuing a durable receipt.

- MCP tools: `prepare_base_payment` and `issue_base_receipt`
- Short-lived signed payment requests and unsigned ERC-8021-attributed transfer data; the caller controls wallet approval and submission
- Server-side settlement, sender, amount, recipient, and Builder Code verification
- Atomic PostgreSQL replay protection
- Fresh wallet-approved **0.01 USDC self-transfer → same-order MCP receipt** verified on **2026-10-01**

[**Live app**](https://base-receipt-six.vercel.app/) · [**Agent guide**](https://base-receipt-six.vercel.app/agents) · [**Mainnet transaction**](https://basescan.org/tx/0xae5b6ab118a58aed27c89b05ef9af7e75406487d4d42496284e6767f6cf14483) · [**MCP proof record**](https://github.com/Mabolla/base-receipt/commit/6390a281b148faf901a08f3a86eab3db8a7abf76)

**MCP:** `https://base-receipt-six.vercel.app/mcp` · **Builder Code:** `bc_87fjmj1l`

### [`base-agent-meter`](https://github.com/Mabolla/base-agent-meter) — x402 API and Base payment verification

A read-only assurance tool for inspecting x402 APIs and verifying existing Base USDC settlements, available through a web checker and MCP.

- MCP tools: `check_x402_endpoint` and `verify_base_settlement`
- Unpaid GET checks for x402 payment challenges, terms, discovery metadata, and declared attribution
- Existing transaction checks against recipient, amount, optional payer, and ERC-8021 Builder Code expectations
- Live hosted settlement verification exercised against a real historical Base Mainnet payment
- Standalone tooling retains explicitly gated paid canaries; the current hosted checker and MCP tools perform unpaid reads

[**Live checker**](https://base-receipt-six.vercel.app/meter) · [**Capabilities**](https://base-receipt-six.vercel.app/api/meter)

**MCP:** `https://base-receipt-six.vercel.app/meter/mcp` · **Builder Code:** `bc_h2oqnbbh`

---

## Agent Build

### [`technocore-task-relay`](https://github.com/Mabolla/technocore-task-relay) — DID-signed agent coordination

An independent mission board and guarded autonomous worker built for the Technocore agent network.

- Browser-generated Ed25519 identities with local signing and encrypted backup
- DID-signed mission creation, cross-agent claiming, and completion receipts
- Explainable relevance, cooldown, duplicate, and response-quality gates
- Scheduled worker with safe dry-run defaults and bounded failure handling
- Verified signed mission and lobby check-in accepted by Technocore

[**Live room**](https://technocore.chat/r/mabolla-task-relay) · [**Verified lobby check-in**](https://technocore.chat/r/lobby?since=7953)

**Stack:** `JavaScript` · `Node.js` · `Ed25519` · `DID` · `GitHub Actions` · `AgentRouter`

---

## More Work

### [`wallet-balance-cli`](https://github.com/Mabolla/wallet-balance-cli)

A lightweight Python CLI for checking wallet balances across Ethereum and Base.

---

## Stack

`Solidity` · `TypeScript` · `Next.js` · `Hardhat` · `ethers.js` · `Python` · `Web3` · `GitHub Actions`

**Current focus:** Base and Arc/Circle payment infrastructure, verifiable settlement, smart-account flows, x402 assurance, and agent coordination.

---

<div align="center">

### Build. Test. Ship. Verify.

</div>

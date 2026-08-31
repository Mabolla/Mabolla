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

### [`base-receipt`](https://github.com/Mabolla/base-receipt) — Server-verified Base Pay receipts

A production-minded Base Mainnet USDC payment flow that independently verifies settlement before issuing a durable receipt.

- Short-lived signed payment requests and server-side amount/recipient verification
- Atomic PostgreSQL replay protection
- Verified production flow with a real Base Mainnet USDC payment

### [`base-agent-meter`](https://github.com/Mabolla/base-agent-meter) — x402 production assurance

A Base-native assurance tool for checking whether agents can discover, pay for, settle, and consume x402 services.

- Unpaid pre-deploy checks and explicitly gated live paid canaries
- Base USDC settlement proof and ERC-8021 builder-attribution verification
- Verified x402 v2 seller flow with a real Base Mainnet payment

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

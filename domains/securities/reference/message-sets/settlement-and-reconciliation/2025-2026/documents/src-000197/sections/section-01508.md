---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.81 UnmatchedReason22Choice", "35.1.29.81.2 Proprietary <Prtry>"]
file_pages: [2003]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.81.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 2003 to 2003.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2003

```text
CodeName Name Definition
REPA RepurchaseAmount Termination transaction amount does not
match.
CADE RepurchaseCallDelay Transaction call delay does not match.
REPP RepurchasePremiumAmount Premium amount does not match.
REPO RepurchaseRate Repurchase rate does not match.
RERT RepurchaseRateType Repurchase rate type does not match.
RSPR RepurchaseSpreadRate Spread rate does not match.
RTGS RTGSSystem Counterparty is for Real Time Gross
Settlement (RTGS) system, you are for
non-RTGS or vice versa.
SAFE SafekeepingAccount Safekeeping account used as matching
criteria on the market concerned does
not match. This includes Buyer/seller's
account, direct client's account at the
receiving/delivering agent, or receiving/
delivering agent's account at the CSD.
DMON SettlementAmount Settlement amount does not match.
DDAT SettlementDate Settlement date/time does not match.
SETS SettlementSystemMethod Settlement system/method does not
match (for example, instruction is to
settle using settlement system/method
A. Counterparty expects settlement to
occur using settlement system/method
B).
SETR SettlementTransaction Settlement transaction type does not
match (relates to the settlement
transaction type codes available for field:
22F:: SETR.).
TXST TaxStatus Disagreement on the tax status of the
financial instruments to be settled.
DTRD TradeDate Trade date does not match.
DEAL TransactionDealAmount Deal amount does not match.
DELN TransactionDirection Direction of the trade does not match.
Counterparty expects a delivery from
you, not a receipt or vice versa.
UNBR UnmatchedMarketSide Market side trade is unmatched.
VASU VariableRateSupport Variable rate support does not match
(repo).
DCMX CumEx Disagreement if trade was executed cum
or ex.
DMCT AutomaticGeneration Disagreement on automatic generation
of market claim or transformation.
35.1.29.81.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction has an unmatched status.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2003 March 2026
```


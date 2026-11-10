---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 semt.013.001.07 IntraPositionMovementInstructionV07"]
file_pages: [135, 136]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.013.001.07"]
---

# 4 semt.013.001.07 IntraPositionMovementInstructionV07

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 135 to 136.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 135

```text
4 semt.013.001.07
IntraPositionMovementInstructionV07
4.1 MessageDefinition Functionality
Scope
An account owner sends a IntraPositionMovementInstruction to an account servicer to instruct the
movement of securities within its holding from one sub-balance to another, for example, blocking of
securities.
The account owner/servicer relationship may be:
- a global custodian which has an account with its local agent (sub-custodian), or
- an investment management institution which manage a fund account opened at a custodian, or
- a broker which has an account with a custodian, or
- a central securities depository participant which has an account with a central securities depository, or
- a central securities depository which has an account with a custodian, another central securities
depository or another settlement market infrastructure.
Usage
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information.
using the relevant elements in the Business Application Header.
Outline
The IntraPositionMovementInstructionV07 MessageDefinition is composed of 12
MessageBuildingBlocks:
A. TransactionIdentification
Unambiguous identification of the transaction as known by the instructing party.
B. CorporateActionEventIdentification
Identification assigned by the account servicer to unambiguously identify a corporate action event.
C. NumberCounts
Count of the number of transactions linked.
D. Linkages
Approved by the Securities SEG on 27 January 2026 semt.013.001.07
IntraPositionMovementInstructionV07
Settlement And Reconciliation - Maintenance 2025 - 2026 135 March 2026
```

## File page 136

```text
Link to another transaction that must be processed after, before or at the same time.
E. AccountOwner
Party that legally owns the account.
F. SafekeepingAccount
Account to or from which a securities entry is made.
G. BlockChainAddressOrWallet
Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
H. SafekeepingPlace
Place where the securities are safe-kept, physically or notionally. This place can be, for example, a
local custodian, a Central Securities Depository (CSD) or an International Central Securities
Depository (ICSD).
I. FinancialInstrumentIdentification
Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
J. FinancialInstrumentAttributes
Elements characterising a financial instrument.
K. IntraPositionDetails
Intra-position movement transaction details.
L. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 semt.013.001.07
IntraPositionMovementInstructionV07
Settlement And Reconciliation - Maintenance 2025 - 2026 136 March 2026
```


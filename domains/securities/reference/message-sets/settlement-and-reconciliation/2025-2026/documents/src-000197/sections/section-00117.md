---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 semt.015.001.10 IntraPositionMovementConfirmationV10"]
file_pages: [162, 163]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.015.001.10"]
---

# 6 semt.015.001.10 IntraPositionMovementConfirmationV10

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 162 to 163.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 162

```text
6 semt.015.001.10
IntraPositionMovementConfirmationV10
6.1 MessageDefinition Functionality
Scope
The IntraPositionMovementConfirmation is sent by an account servicer to an account owner to confirm
the movement of securities within its holding from one sub-balance to another, for example, blocking of
securities.
The account servicer/owner relationship may be:
- a central securities depository or another settlement market infrastructure acting on behalf of its
participant
- an agent (sub-custodian) acting on behalf of its global custodian customer, or
- a custodian acting on behalf of an investment management institution or a broker/dealer.
Usage
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information
using the relevant elements in the Business Application Header.
Outline
The IntraPositionMovementConfirmationV10 MessageDefinition is composed of 10
MessageBuildingBlocks:
A. AdditionalParameters
Additional parameters for the transaction.
B. Linkage
Link to another transaction that triggered the intra-position movement.
C. AccountOwner
Party that legally owns the account.
D. SafekeepingAccount
Account to or from which a securities entry is made.
E. BlockChainAddressOrWallet
Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
Approved by the Securities SEG on 27 January 2026 semt.015.001.10
IntraPositionMovementConfirmationV10
Settlement And Reconciliation - Maintenance 2025 - 2026 162 March 2026
```

## File page 163

```text
F. SafekeepingPlace
Place where the securities are safe-kept, physically or notionally. This place can be, for example, a
local custodian, a Central Securities Depository (CSD) or an International Central Securities
Depository (ICSD).
G. FinancialInstrumentIdentification
Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
H. FinancialInstrumentAttributes
Elements characterising a financial instrument.
I. IntraPositionDetails
Intra-position movement transaction details.
J. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 semt.015.001.10
IntraPositionMovementConfirmationV10
Settlement And Reconciliation - Maintenance 2025 - 2026 163 March 2026
```


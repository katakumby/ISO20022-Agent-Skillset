---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "13.1 MessageDefinition Functionality"]
file_pages: [433]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.022.001.07"]
---

# 13.1 MessageDefinition Functionality

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 433 to 433.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 433

```text
13 semt.022.001.07
SecuritiesSettlementTransactionAuditTrailRe
portV07
13.1 MessageDefinition Functionality
Scope
This message is sent by the Market Infrastructure to the CSD to advise of the history of all the statuses,
modifications, replacement and cancellation of a specific transaction during its whole life cycle when the
instructing party is a direct participant to the Settlement Infrastructure.
Usage
The message may also be used to:
- re-send a message sent by the market infrastructure to the direct participant,
- provide a third party with a copy of a message being sent by the market infrastructure for information,
- re-send to a third party a copy of a message being sent by the market infrastructure for information
using the relevant elements in the Business Application Header.
Outline
The SecuritiesSettlementTransactionAuditTrailReportV07 MessageDefinition is composed of 7
MessageBuildingBlocks:
A. Pagination
Page number of the message (within a statement) and continuation indicator to indicate that the
statement is to continue or that the message is the last page of the statement.
B. QueryReference
Identification of the message sent to request this report.
C. TransactionIdentification
Provides unambiguous transaction identification information.
D. SafekeepingAccount
Account to or from which a securities entry is made.
E. BlockChainAddressOrWallet
Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
F. AccountOwner
Party that legally owns the account.
G. StatusTrail
Provides the history of status and reasons for a pending, posted or cancelled transaction.
Approved by the Securities SEG on 27 January 2026 semt.022.001.07
SecuritiesSettlementTransactionAuditTrailReportV0
7
Settlement And Reconciliation - Maintenance 2025 - 2026 433 March 2026
```


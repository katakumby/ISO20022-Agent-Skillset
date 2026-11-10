---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08"]
file_pages: [1300, 1301]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.039.001.08"]
---

# 33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1300 to 1301.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1300

```text
33 sese.039.001.08
SecuritiesSettlementTransactionModification
RequestStatusAdviceV08
33.1 MessageDefinition Functionality
Scope
An account servicer sends a SecuritiesSettlementTransactionModificationRequestStatusAdvice to an
account owner to advise the status of a SecuritiesSettlementModificationRequest message previously
sent by the account owner.
The account servicer may be:
- a central securities depository or another settlement market infrastructure managing securities
settlement transactions on behalf of their participants
- an custodian acting as an accounting and/or settlement agent.
Usage
The message may also be used to:
- re-send a message sent by the account owner to the account servicer,
- provide a third party with a copy of a message being sent by the account owner for information,
- re-send to a third party a copy of a message being sent by the account owner for information
using the relevant elements in the Business Application Header.
Outline
The SecuritiesSettlementTransactionModificationRequestStatusAdviceV08 MessageDefinition is
composed of 8 MessageBuildingBlocks:
A. ModificationRequestReference
Reference to the unambiguous identification of the cancellation request as per the account owner.
B. AccountOwner
Party that legally owns the account.
C. SafekeepingAccount
Account to or from which a securities entry is made.
D. BlockChainAddressOrWallet
Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
E. TransactionIdentification
Provides unambiguous transaction identification information.
Approved by the Securities SEG on 27 January 2026 sese.039.001.08
SecuritiesSettlementTransactionModificationReques
tStatusAdviceV08
Settlement And Reconciliation - Maintenance 2025 - 2026 1300 March 2026
```

## File page 1301

```text
F. ModificationProcessingStatus
Provides details on the processing status of the request.
G. TransactionDetails
Identifies the details of the transaction.
H. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.039.001.08
SecuritiesSettlementTransactionModificationReques
tStatusAdviceV08
Settlement And Reconciliation - Maintenance 2025 - 2026 1301 March 2026
```


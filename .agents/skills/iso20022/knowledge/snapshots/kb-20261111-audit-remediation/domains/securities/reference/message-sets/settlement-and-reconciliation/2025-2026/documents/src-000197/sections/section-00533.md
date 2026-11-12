---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11"]
file_pages: [802, 803]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.031.001.11"]
---

# 25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 802 to 803.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 802

```text
25 sese.031.001.11
SecuritiesSettlementConditionModificationSt
atusAdviceV11
25.1 MessageDefinition Functionality
Scope
An account servicer sends a SecuritiesSettlementConditionsModificationStatusAdvice to an account
owner to advise the status of a modification request previously instructed by the account owner.
The account servicer/owner relationship may be:
- a central securities depository or another settlement market infrastructure acting on behalf of their
participants
- an agent (sub-custodian) acting on behalf of their global custodian customer, or
- a custodian acting on behalf of an investment management institution or a broker/dealer.
Usage
A SecuritiesSettlementConditionsModificationRequest may contain requests on multiple transactions.
However, one SecuritiesSettlementConditionsModificationStatusAdvice must be sent per transaction
modified unless the SecuritiesSettlementConditionsModificationRequest is rejected as a whole.
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information using the relevant elements in the
Business Application Header.
Outline
The SecuritiesSettlementConditionModificationStatusAdviceV11 MessageDefinition is composed of 7
MessageBuildingBlocks:
A. RequestReference
Identification of the SecuritiesSettlementConditionsModificationRequest.
B. AccountOwner
Party that legally owns the account.
C. SafekeepingAccount
Account to or from which a securities entry is made.
D. BlockChainAddressOrWallet
Approved by the Securities SEG on 27 January 2026 sese.031.001.11
SecuritiesSettlementConditionModificationStatusAd
viceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 802 March 2026
```

## File page 803

```text
Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
E. RequestDetails
Details of the request.
F. ProcessingStatus
Provides details on the processing status of the request.
G. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.031.001.11
SecuritiesSettlementConditionModificationStatusAd
viceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 803 March 2026
```


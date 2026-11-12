---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["10 MX secl.009.001.03 BuyInConfirmationV03"]
file_pages: [294]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.009.001.03"]
---

# 10 MX secl.009.001.03 BuyInConfirmationV03

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 294 to 294.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 294

```text
10 MX secl.009.001.03
BuyInConfirmationV03
10.1 MessageDefinition Functionality
Scope
The Buy In Confirmation message is sent by the central counterparty (CCP) to the clearing member to
confirm the details of the transaction resulting from the buy in.
The message definition is intended for use with the ISO 20022 Business Application Header.
Usage
The Buy In Confirmation message is sent by the central counterparty (CCP) to confirm the details of the
buy in transaction.
Outline
The BuyInConfirmationV03 MessageDefinition is composed of 5 MessageBuildingBlocks:
A. TransactionIdentification
Unambiguous identification of the transaction as known by the instructing party.
B. ClearingMember
Provides the identification of the clearing member (individual clearing member or general clearing
member).
C. BuyInDetails
Provides the buy-in details.
D. OriginalSettlementObligation
Provides details about the original settlement obligation that did not settle and for which the buy in
process will be launched.
E. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.009.001.03 BuyInConfirmationV03
March 2026 294
```


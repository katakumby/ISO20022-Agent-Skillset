---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["77 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01"]
file_pages: [2689]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.032.001.01"]
---

# 77 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2689 to 2689.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2689

```text
77 semt.032.001.01
SecuritiesTransactionCancellationRequestQu
eryV01
77.1 MessageDefinition Functionality
The SecuritiesTransactionCancellationRequestQuery message is sent from an account owner/
requestor to a settlement infrastructure to query for the status of settlement or intra-position movement
cancellation instruction(s) based on a set of search criteria or business attributes.
The message may also be used to:
- re-send a message sent by the account owner to the account servicer (the sub-function of the
message is "Duplicate")
- provide a third party with a copy of a message being sent by the account owner for information (the
sub-function of the message is "Copy")
- re-send to a third party a copy of a message being sent by the account owner for information (the sub-
function of the message is "Copy Duplicate").
Outline
The SecuritiesTransactionCancellationRequestQueryV01 MessageDefinition is composed of 2
MessageBuildingBlocks:
A. QueryDefinition
Defines the intra-position movement cancellation query criteria.
B. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.032.001.01
SecuritiesTransactionCancellationRequestQueryV0
1
Target2-Securities 2689 August 2026
```


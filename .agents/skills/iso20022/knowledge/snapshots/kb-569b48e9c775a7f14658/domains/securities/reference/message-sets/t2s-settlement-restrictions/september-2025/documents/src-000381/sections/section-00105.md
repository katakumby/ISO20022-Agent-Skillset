---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["6 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01"]
file_pages: [134]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.032.001.01"]
---

# 6 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 134 to 134.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 134

```text
6 semt.032.001.01
SecuritiesTransactionCancellationRequestQu
eryV01
6.1 MessageDefinition Functionality
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
Approved by the Securities SEG on 21 August 2025 semt.032.001.01
SecuritiesTransactionCancellationRequestQueryV0
1
Target2-Securities - Settlement Restrictions 134 September 2025
```


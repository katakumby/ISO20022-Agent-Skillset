---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["77 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01", "77.3 Constraints"]
file_pages: [2691]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.032.001.01"]
---

# 77.3 Constraints

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2691 to 2691.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2691

```text
77.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
77.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
77.4.1 QueryDefinition <QryDef>
Presence: [1..1]
Definition: Defines the intra-position movement cancellation query criteria.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.032.001.01
SecuritiesTransactionCancellationRequestQueryV0
1
Target2-Securities 2691 August 2026
```


---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["75 semt.030.001.01 SecuritiesSettlementConditionsModificationRequestQueryV01", "75.3 Constraints"]
file_pages: [2644]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.030.001.01"]
---

# 75.3 Constraints

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2644 to 2644.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2644

```text
75.3 Constraints
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
75.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
75.4.1 QueryDefinition <QryDef>
Presence: [1..1]
Definition: Defines the intra-position movement modification query criteria.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.030.001.01
SecuritiesSettlementConditionsModificationRequest
QueryV01
Target2-Securities 2644 August 2026
```


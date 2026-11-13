---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["35 reda.015.001.01 PartyQueryV01", "35.4 Message Building Blocks", "35.4.3 ReturnCriteria <RtrCrit>", "35.4.3.14 LockStatus <LckSts>"]
file_pages: [2071]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.015.001.01"]
---

# 35.4.3.14 LockStatus <LckSts>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2071 to 2071.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2071

```text
35.4.3.14  LockStatus <LckSts>
Presence: [0..1]
Definition: Indicates whether the lock status is requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 3323):
• Meaning When True: Requested
• Meaning When False: Not Requested
35.4.3.15  MarketSpecificAttribute <MktSpcfcAttr>
Presence: [0..1]
Definition: Indicates whether the market specific attributes for the party are requested.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 3323):
• Meaning When True: Requested
• Meaning When False: Not Requested
35.4.4 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C3 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 3011 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 3011
   Envelope <Envlp> [1..1] (External Schema) 3012
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.015.001.01 PartyQueryV01
Target2-Securities 2071 August 2026
```


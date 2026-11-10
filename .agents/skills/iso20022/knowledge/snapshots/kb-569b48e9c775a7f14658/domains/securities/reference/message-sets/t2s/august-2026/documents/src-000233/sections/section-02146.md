---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.7 Clearing System Member Identification"]
file_pages: [2907]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.7 Clearing System Member Identification

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2907 to 2907.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2907

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.7 Clearing System Member Identification
82.1.7.1  PlaceOfClearingIdentification2
Definition: Identification of infrastructure which may be a component of a clearing house and which
facilitates clearing and settlement for its members by standing between the buyer and the seller. It may
net transactions and it substitutes itself as settlement counterparty for each position.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] IdentifierSet C2 2907
   LEI <LEI> [0..1] IdentifierSet 2907
82.1.7.1.1  Identification <Id>
Presence: [0..1]
Definition: Unique identification of the place of clearing.
Impacted by: C2 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 3320
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
82.1.7.1.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a place of clearing.
Datatype: "LEIIdentifier" on page 3322
82.1.8 Date Period
82.1.8.1  DatePeriod1Choice
Definition: Period as a date, a month or a date time span for which the statement is provided.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2907 August 2026
```


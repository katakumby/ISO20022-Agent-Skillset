---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.7 Clearing System Member Identification"]
file_pages: [315]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.7 Clearing System Member Identification

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 315 to 315.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 315

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.1.7 Clearing System Member Identification
7.1.7.1  PlaceOfClearingIdentification2
Definition: Identification of infrastructure which may be a component of a clearing house and which
facilitates clearing and settlement for its members by standing between the buyer and the seller. It may
net transactions and it substitutes itself as settlement counterparty for each position.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] IdentifierSet C2 315
   LEI <LEI> [0..1] IdentifierSet 315
7.1.7.1.1  Identification <Id>
Presence: [0..1]
Definition: Unique identification of the place of clearing.
Impacted by: C2 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 551
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
7.1.7.1.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a place of clearing.
Datatype: "LEIIdentifier" on page 552
7.1.8 Date Period
7.1.8.1  DatePeriod1Choice
Definition: Period as a date, a month or a date time span for which the statement is provided.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 315 March 2026
```


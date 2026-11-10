---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.6 Clearing System Member Identification"]
file_pages: [1434]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.6 Clearing System Member Identification

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1434 to 1434.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1434

```text
Definition: Cash settlement system expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.6 Clearing System Member Identification
35.1.6.1  PlaceOfClearingIdentification2
Definition: Identification of infrastructure which may be a component of a clearing house and which
facilitates clearing and settlement for its members by standing between the buyer and the seller. It may
net transactions and it substitutes itself as settlement counterparty for each position.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] IdentifierSet C5 1434
   LEI <LEI> [0..1] IdentifierSet 1434
35.1.6.1.1  Identification <Id>
Presence: [0..1]
Definition: Unique identification of the place of clearing.
Impacted by: C5 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 2185
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
35.1.6.1.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a place of clearing.
Datatype: "LEIIdentifier" on page 2187
35.1.7 Date Period
35.1.7.1  Period7Choice
Definition: Choice between date and date-time for the specification of a period.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1434 March 2026
```


---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.17 Organisation Identification", "35.1.17.1 OrganisationIdentification31", "35.1.17.1.2 Other <Othr>"]
file_pages: [1660]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.17.1.2 Other <Othr>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1660 to 1660.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1660

```text
Definition: Code allocated to an institution by the ISO 9362 Registration Authority as described in ISO
9362 "Banking - Banking telecommunication messages - Business identifier code (BIC)".
Impacted by: C5 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 2185
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
35.1.17.1.2  Other <Othr>
Presence: [0..*]
Definition: Unique identification of an organisation, as assigned by an institution, using an identification
scheme.
Other <Othr> contains the following GenericOrganisationIdentification1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1660
   SchemeName <SchmeNm> [0..1]  1660
{Or     Code <Cd> [1..1] CodeSet 1660
Or}     Proprietary <Prtry> [1..1] Text 1661
   Issuer <Issr> [0..1] Text 1661
35.1.17.1.2.1  Identification <Id>
Presence: [1..1]
Definition: Identification assigned by an institution.
Datatype: "Max35Text" on page 2192
35.1.17.1.2.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
SchemeName <SchmeNm> contains one of the following
OrganisationIdentificationSchemeName1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1660
Or}   Proprietary <Prtry> [1..1] Text 1661
35.1.17.1.2.2.1  Code <Cd>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1660 March 2026
```


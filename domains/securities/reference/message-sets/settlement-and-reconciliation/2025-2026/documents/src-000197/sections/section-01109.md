---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.19 Tracking4Choice"]
file_pages: [1551]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.19 Tracking4Choice

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1551 to 1551.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1551

```text
Definition: Role of the party in the activity.
Datatype: "Max350Text" on page 2192
35.1.16.19  Tracking4Choice
Definition: Choice of format for the tracking information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1551
Or}   Proprietary <Prtry> [1..1] ± 1551
35.1.16.19.1  Indicator <Ind>
Presence: [1..1]
Definition: Specifies whether the loan and/or collateral is tracked.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.16.19.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Tracking information expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.20  Restriction5Choice
Definition: Choice of format for the securities restriction information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1551
Or}   Proprietary <Prtry> [1..1] ± 1552
35.1.16.20.1  Code <Cd>
Presence: [1..1]
Definition: Restrictions expressed as an ISO 20022 code.
Datatype: "OwnershipLegalRestrictions1Code" on page 2089
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1551 March 2026
```


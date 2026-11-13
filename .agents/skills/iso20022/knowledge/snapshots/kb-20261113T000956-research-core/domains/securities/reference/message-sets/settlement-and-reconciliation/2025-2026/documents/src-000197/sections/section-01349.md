---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.26 Settlement Details", "35.1.26.5 SettlementDetails230", "35.1.26.5.13 SettlingCapacity <SttlgCpcty>"]
file_pages: [1814]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.26.5.13 SettlingCapacity <SttlgCpcty>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1814 to 1814.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1814

```text
LegalRestrictions <LglRstrctns> contains one of the following elements (see "Restriction5Choice" on
page 1551 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1551
Or}   Proprietary <Prtry> [1..1] ± 1552
35.1.26.5.13  SettlingCapacity <SttlgCpcty>
Presence: [0..1]
Definition: Role of a party in the settlement of the transaction.
SettlingCapacity <SttlgCpcty> contains one of the following elements (see "SettlingCapacity7Choice"
on page 1631 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1631
Or}   Proprietary <Prtry> [1..1] ± 1632
35.1.26.5.14  TaxCapacity <TaxCpcty>
Presence: [0..1]
Definition: Tax role capacity of the instructing party.
TaxCapacity <TaxCpcty> contains one of the following elements (see "TaxCapacityParty4Choice" on
page 1564 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1564
Or}   Proprietary <Prtry> [1..1] ± 1564
35.1.26.5.15  StampDutyTaxBasis <StmpDtyTaxBsis>
Presence: [0..1]
Definition: Specifies the stamp duty type or exemption reason applicable to the settlement transaction.
StampDutyTaxBasis <StmpDtyTaxBsis> contains the following elements (see
"GenericIdentification30" on page 1502 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.26.5.16  Tracking <Trckg>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1814 March 2026
```


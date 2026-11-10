---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.26 Settlement Details", "35.1.26.9 SettlementDetails223", "35.1.26.9.13 RepurchaseType <RpTp>"]
file_pages: [1840]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.26.9.13 RepurchaseType <RpTp>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1840 to 1840.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1840

```text
Registration <Regn> contains one of the following elements (see "Registration9Choice" on page 1623
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1623
Or}   Proprietary <Prtry> [1..1] ± 1623
35.1.26.9.13  RepurchaseType <RpTp>
Presence: [0..1]
Definition: Specifies the type of repurchase transaction.
RepurchaseType <RpTp> contains one of the following elements (see "RepurchaseType22Choice" on
page 1579 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1580
Or}   Proprietary <Prtry> [1..1] ± 1580
35.1.26.9.14  LegalRestrictions <LglRstrctns>
Presence: [0..1]
Definition: Regulatory restrictions applicable to a security.
LegalRestrictions <LglRstrctns> contains one of the following elements (see "Restriction5Choice" on
page 1551 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1551
Or}   Proprietary <Prtry> [1..1] ± 1552
35.1.26.9.15  SecuritiesRTGS <SctiesRTGS>
Presence: [0..1]
Definition: Specifies whether the settlement transaction was to be settled through an RTGS or a non
RTGS system.
SecuritiesRTGS <SctiesRTGS> contains one of the following elements (see
"SecuritiesRTGS4Choice" on page 1554 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1554
Or}   Proprietary <Prtry> [1..1] ± 1554
35.1.26.9.16  SettlingCapacity <SttlgCpcty>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1840 March 2026
```


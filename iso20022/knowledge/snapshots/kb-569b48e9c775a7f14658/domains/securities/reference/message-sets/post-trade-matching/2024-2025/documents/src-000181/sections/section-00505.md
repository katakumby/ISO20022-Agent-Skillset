---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.27 Settlement Details", "7.1.27.1 SettlementDetails213", "7.1.27.1.17 RepurchaseType <RpTp>"]
file_pages: [579]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.27.1.17 RepurchaseType <RpTp>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 579 to 579.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 579

```text
7.1.27.1.17  RepurchaseType <RpTp>
Presence: [0..1]
Definition: Specifies whether the rate is fixed, variable or a forfeit.
RepurchaseType <RpTp> contains one of the following elements (see "RepurchaseType22Choice" on
page 332 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 332
Or}   Proprietary <Prtry> [1..1] ± 333
7.1.27.1.18  LegalRestrictions <LglRstrctns>
Presence: [0..1]
Definition: Regulatory restrictions applicable to a security.
LegalRestrictions <LglRstrctns> contains one of the following elements (see "Restriction5Choice" on
page 308 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 308
Or}   Proprietary <Prtry> [1..1] ± 308
7.1.27.1.19  SecuritiesRTGS <SctiesRTGS>
Presence: [0..1]
Definition: Specifies whether the settlement transaction is to be settled through an RTGS or a non
RTGS system.
SecuritiesRTGS <SctiesRTGS> contains one of the following elements (see
"SecuritiesRTGS4Choice" on page 311 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 312
Or}   Proprietary <Prtry> [1..1] ± 312
7.1.27.1.20  SettlingCapacity <SttlgCpcty>
Presence: [0..1]
Definition: Role of a party in the settlement of the transaction.
SettlingCapacity <SttlgCpcty> contains one of the following elements (see "SettlingCapacity9Choice"
on page 354 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 354
Or}   Proprietary <Prtry> [1..1] ± 354
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 579 February 2025
```


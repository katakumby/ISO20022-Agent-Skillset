---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.13 AccountingStatus1Choice", "66.1.45.13.2 Proprietary <Prtry>"]
file_pages: [5185]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.13.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5185 to 5185.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5185

```text
66.1.45.13.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Accounting status expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.45.14  PartiallySettledStatus10
Definition: Reason for a partially settled status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [1..1]  5185
{Or     Code <Cd> [1..1] CodeSet 5185
Or}     Proprietary <Prtry> [1..1] ± 5186
   AdditionalInformation <AddtlInf> [0..1] Text 5186
66.1.45.14.1  Reason <Rsn>
Presence: [1..1]
Definition: Reason for the partially settled status.
Reason <Rsn> contains one of the following PartiallySettled21Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5185
Or}   Proprietary <Prtry> [1..1] ± 5186
66.1.45.14.1.1  Code <Cd>
Presence: [1..1]
Definition: Partially settled reason expressed as a code.
Datatype: "SettledStatusReason2Code" on page 5361
CodeName Name Definition
CPST CashPartiallySettled Cash is partially settled.
GATM GatedMultipleNAV Redemption has been gated. Multiple
redemptions and multiple prices will be
required.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5185 May 2026
```


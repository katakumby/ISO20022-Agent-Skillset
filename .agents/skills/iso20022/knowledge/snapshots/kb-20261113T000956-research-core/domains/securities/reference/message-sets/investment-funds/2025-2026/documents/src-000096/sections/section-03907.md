---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.22 InRepairStatusReason4Choice", "66.1.45.22.2 ReasonDetails <RsnDtls>", "66.1.45.22.2.1 Reason <Rsn>"]
file_pages: [5199]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.22.2.1 Reason <Rsn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5199 to 5199.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5199

```text
ReasonDetails <RsnDtls> contains the following InRepairStatusReason4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [1..1]  5199
{Or     Code <Cd> [1..1] CodeSet 5199
Or}     Proprietary <Prtry> [1..1] ± 5199
   AdditionalInformation <AddtlInf> [0..1] Text 5199
66.1.45.22.2.1  Reason <Rsn>
Presence: [1..1]
Definition: Reason for the in repair status expressed as a code.
Reason <Rsn> contains one of the following InRepairStatusReason5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5199
Or}   Proprietary <Prtry> [1..1] ± 5199
66.1.45.22.2.1.1  Code <Cd>
Presence: [1..1]
Definition: In repair reason expressed as a code.
Datatype: "InRepairStatusReason1Code" on page 5311
CodeName Name Definition
COMA CommercialAgreement Order has been accepted and
centralised before the cut off, but with
different sales agreement than the one
provided in the order.
66.1.45.22.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: In repair reason expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification1" on page 4552 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4552
   Issuer <Issr> [0..1] Text 4552
66.1.45.22.2.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5199 May 2026
```


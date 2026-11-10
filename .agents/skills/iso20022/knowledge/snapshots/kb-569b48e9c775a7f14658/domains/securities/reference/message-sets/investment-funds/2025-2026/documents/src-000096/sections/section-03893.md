---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.12 SuspendedStatusReason4Choice", "66.1.45.12.2 ReasonDetails <RsnDtls>", "66.1.45.12.2.1 Reason <Rsn>", "66.1.45.12.2.1.2 Proprietary <Prtry>"]
file_pages: [5184]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.12.2.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5184 to 5184.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5184

```text
Definition: Suspended reason expressed as a code.
Datatype: "SuspendedStatusReason3Code" on page 5365
CodeName Name Definition
PRIC PriceSuspension There is a suspension of pricing. The
order will stay on the books until the next
pricing.
FLOW Overflow There is a fund overflow.
66.1.45.12.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Suspended reason expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification1" on page 4552 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4552
   Issuer <Issr> [0..1] Text 4552
66.1.45.12.2.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about the suspended reason.
Datatype: "Max350Text" on page 5403
66.1.45.13  AccountingStatus1Choice
Definition: Choice of formats for the accounting status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5184
Or}   Proprietary <Prtry> [1..1] ± 5185
66.1.45.13.1  Code <Cd>
Presence: [1..1]
Definition: Accounting status expressed as a code.
Datatype: "AccountingStatus1Code" on page 5271
CodeName Name Definition
YDOM Domestic Account or party is regarded as domestic
for reporting purposes.
NDOM NotDomestic Account or party is not regarded as
domestic for reporting purposes.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5184 May 2026
```


---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.23 CancelledStatusReason16", "66.1.45.23.1 Reason <Rsn>", "66.1.45.23.1.2 Proprietary <Prtry>"]
file_pages: [5201]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.23.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5201 to 5201.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5201

```text
CodeName Name Definition
CXLR EndOfLife Transaction is rejected by the executing
party, the rejection is final therefore the
order is cancelled in the system.
CANO CancelledByOther Transaction is cancelled by a party other
than the instructing party, eg, a market
infrastructure such as a stock exchange.
66.1.45.23.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Cancelled reason expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification1" on page 4552 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4552
   Issuer <Issr> [0..1] Text 4552
66.1.45.23.1.3  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: No reason available or to report for the cancelled status.
Datatype: "NoReasonCode" on page 5331
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
66.1.45.23.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about the cancelled status.
Datatype: "Max350Text" on page 5403
66.1.45.24  RejectionReason31
Definition: Information about a rejected status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [1..1]  5202
{Or     Code <Cd> [1..1] CodeSet 5202
Or}     Proprietary <Prtry> [1..1] ± 5202
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 5202
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5201 May 2026
```


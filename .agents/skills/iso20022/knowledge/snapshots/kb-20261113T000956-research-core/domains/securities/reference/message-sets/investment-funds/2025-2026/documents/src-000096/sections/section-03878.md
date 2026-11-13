---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.1 BlockedStatusReason2Choice", "66.1.45.1.2 Reason <Rsn>", "66.1.45.1.2.3 Reason <Rsn>", "66.1.45.1.2.3.2 Proprietary <Prtry>"]
file_pages: [5168]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.1.2.3.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5168 to 5168.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5168

```text
CodeName Name Definition
TRPE Reregistration Reregistration.
SANC Sanctions Sanctions are in place.
TRAN Transfer Transfer.
66.1.45.1.2.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.45.1.2.4  AdditionalInformation <AddtlInf>
Presence: [1..1]
Definition: Additional information about the blocked account status.
Datatype: "Max350Text" on page 5403
66.1.45.2  ClosurePendingStatusReason1Choice
Definition: Choice of formats for a closure pending status reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5168
Or}   Reason <Rsn> [1..*]  5169
     Code <Cd> [1..1]  5169
{Or       Code <Cd> [1..1] CodeSet 5169
Or}       Proprietary <Prtry> [1..1] ± 5169
     AdditionalInformation <AddtlInf> [0..1] Text 5170
66.1.45.2.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: There is no reason available or to report for the closure pending status.
Datatype: "NoReasonCode" on page 5331
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5168 May 2026
```


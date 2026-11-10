---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.3 SwitchOrderDetailsReport <SwtchOrdrDtlsRpt>", "56.4.3.3.7 OrderStatus <OrdrSts>", "56.4.3.3.7.4 Rejected <Rjctd>", "56.4.3.3.7.4.2 AdditionalInformation <AddtlInf>"]
file_pages: [4183]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.3.7.4.2 AdditionalInformation <AddtlInf>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4183 to 4183.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4183

```text
56.4.3.3.7.4.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about the rejected reason.
Datatype: "Max350Text" on page 5403
56.4.3.3.7.5  Suspended <Sspd>
Presence: [1..1]
Definition: Status of the switch order is suspended.
Suspended <Sspd> contains one of the following elements (see "SuspendedStatusReason4Choice"
on page 5182 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5183
Or}   ReasonDetails <RsnDtls> [1..5]  5183
     Reason <Rsn> [1..1]  5183
{Or       Code <Cd> [1..1] CodeSet 5183
Or}       Proprietary <Prtry> [1..1] ± 5184
     AdditionalInformation <AddtlInf> [0..1] Text 5184
56.4.3.3.7.6  InRepair <InRpr>
Presence: [1..1]
Definition: Status of the switch order is in repair.
InRepair <InRpr> contains one of the following elements (see "InRepairStatusReason4Choice" on
page 5198 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5198
Or}   ReasonDetails <RsnDtls> [1..5]  5198
     Reason <Rsn> [1..1]  5199
{Or       Code <Cd> [1..1] CodeSet 5199
Or}       Proprietary <Prtry> [1..1] ± 5199
     AdditionalInformation <AddtlInf> [0..1] Text 5199
56.4.3.3.7.7  PartiallySettled <PrtlySttld>
Presence: [1..1]
Definition: Status of the switch order is partially settled.
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4183 May 2026
```


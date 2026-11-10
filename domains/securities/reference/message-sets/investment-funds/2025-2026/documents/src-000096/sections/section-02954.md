---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.2 IndividualOrderDetailsReport <IndvOrdrDtlsRpt>", "56.4.3.2.7 OrderStatus <OrdrSts>", "56.4.3.2.7.4 Rejected <Rjctd>", "56.4.3.2.7.4.2 AdditionalInformation <AddtlInf>"]
file_pages: [4146]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.2.7.4.2 AdditionalInformation <AddtlInf>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4146 to 4146.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4146

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification1" on page 4552 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4552
   Issuer <Issr> [0..1] Text 4552
56.4.3.2.7.4.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about the rejected reason.
Datatype: "Max350Text" on page 5403
56.4.3.2.7.5  Suspended <Sspd>
Presence: [1..1]
Definition: Status of the individual order is suspended.
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
56.4.3.2.7.6  InRepair <InRpr>
Presence: [1..1]
Definition: Status of the individual order is in repair.
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4146 May 2026
```


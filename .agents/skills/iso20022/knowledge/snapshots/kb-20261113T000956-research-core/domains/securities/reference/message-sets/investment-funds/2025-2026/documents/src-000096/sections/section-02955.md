---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.2 IndividualOrderDetailsReport <IndvOrdrDtlsRpt>", "56.4.3.2.7 OrderStatus <OrdrSts>", "56.4.3.2.7.7 PartiallySettled <PrtlySttld>"]
file_pages: [4147]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.2.7.7 PartiallySettled <PrtlySttld>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4147 to 4147.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4147

```text
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
56.4.3.2.7.7  PartiallySettled <PrtlySttld>
Presence: [1..1]
Definition: Status of the individual order is partially settled.
PartiallySettled <PrtlySttld> contains the following elements (see "PartiallySettledStatus10" on
page 5185 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [1..1]  5185
{Or     Code <Cd> [1..1] CodeSet 5185
Or}     Proprietary <Prtry> [1..1] ± 5186
   AdditionalInformation <AddtlInf> [0..1] Text 5186
56.4.3.2.8  RepairedFee <RprdFee>
Presence: [0..10]
Definition: Elements from the original individual order that have been repaired so that the order can be
accepted.
Impacted by: C6 "CommercialAgreementRule", C12 "FeeElementRule"
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4147 May 2026
```


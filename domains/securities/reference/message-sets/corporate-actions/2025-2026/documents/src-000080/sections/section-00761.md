---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.41 NotificationIdentification5", "16.1.15.41.1 Identification <Id>"]
file_pages: [954]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.41.1 Identification <Id>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 954 to 954.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 954

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 954
   CreationDateTime <CreDtTm> [0..1] ± 954
16.1.15.41.1  Identification <Id>
Presence: [1..1]
Definition: Unique identifier of the last notification document (message) assigned by the sender of the
document.
Datatype: "Max35Text" on page 1251
16.1.15.41.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the last notification document (message) was created by the sender.
CreationDateTime <CreDtTm> contains one of the following elements (see
"DateAndDateTime2Choice" on page 848 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 848
Or}   DateTime <DtTm> [1..1] DateTime 849
16.1.15.42  GrossDividendRateFormat35Choice
Definition: Choice of format to express a gross dividend.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount C1 955
Or   AmountAndRateStatus <AmtAndRateSts> [1..1]  955
     Amount <Amt> [1..1] Amount C1 955
     RateStatus <RateSts> [1..1] CodeSet 955
Or}   RateTypeAndAmountAndRateStatus
<RateTpAndAmtAndRateSts>
[1..1]  956
     RateType <RateTp> [1..1]  956
{Or       Code <Cd> [1..1] CodeSet 956
Or}       Proprietary <Prtry> [1..1] ± 957
     Amount <Amt> [1..1] Amount C1 957
     RateStatus <RateSts> [0..1]  C52 958
{Or       Code <Cd> [1..1] CodeSet 958
Or}       Proprietary <Prtry> [1..1] ± 958
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 954 February 2026
```


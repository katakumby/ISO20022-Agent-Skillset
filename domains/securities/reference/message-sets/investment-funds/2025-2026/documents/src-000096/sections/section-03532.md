---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.27 OrderWaiver1"]
file_pages: [4782]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.27 OrderWaiver1

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4782 to 4782.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4782

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.26.27  OrderWaiver1
Definition: Information about how an order is to be processed.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OrderWaiverReason <OrdrWvrRsn> [0..*]  4782
{Or     Code <Cd> [1..1] CodeSet 4782
Or}     Proprietary <Prtry> [1..1] ± 4783
   InformationValue <InfVal> [0..1] Text 4783
Constraints
• WaiverElementRule
Either OrderWaiverReason or InformationValue must be present. Both may be present.
66.1.26.27.1  OrderWaiverReason <OrdrWvrRsn>
Presence: [0..*]
Definition: Reason why the order has to be handled differently, probably in a manual fashion, because,
for example, the investment manager has agreed a waiver to the terms.
OrderWaiverReason <OrdrWvrRsn> contains one of the following OrderWaiverReason3Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4782
Or}   Proprietary <Prtry> [1..1] ± 4783
66.1.26.27.1.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the waiver expressed as a code.
Datatype: "OrderWaiverReason1Code" on page 5334
CodeName Name Definition
LATE LateTradeDealing Dealing of the trade is outside the
normal limit.
FEND FrontEndLoadCharge Front end load charge differs from PPM.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4782 May 2026
```


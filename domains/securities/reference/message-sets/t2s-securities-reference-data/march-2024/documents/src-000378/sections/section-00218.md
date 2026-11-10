---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.2 CommonFinancialInstrumentAttributes12", "13.1.6.2.46 SettlementInformation <SttlmInf>", "13.1.6.2.46.5 DeviatingSettlementUnit <DevtgSttlmUnit>"]
file_pages: [296]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.2.46.5 DeviatingSettlementUnit <DevtgSttlmUnit>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 296 to 296.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 296

```text
MinimumMultipleQuantity <MinMltplQty> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 476 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 476
Or   FaceAmount <FaceAmt> [1..1] Amount 476
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 476
13.1.6.2.46.5  DeviatingSettlementUnit <DevtgSttlmUnit>
Presence: [0..*]
Definition: Minimum quantity of securities that can be purchased without incurring a larger fee. For
example, if the round lot size is 100 and the trade is for 125 shares, then 100 will be processed without
a fee and the remaining 25 will incur a service fee for being an odd lot size.
DeviatingSettlementUnit <DevtgSttlmUnit> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 476 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 476
Or   FaceAmount <FaceAmt> [1..1] Amount 476
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 476
13.1.6.2.47  FinancialInstrumentForm <FinInstrmForm>
Presence: [0..1]
Definition: Indicates the form of the financial Instrument.
FinancialInstrumentForm <FinInstrmForm> contains the following FinancialInstrumentForm2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BookingAppearance <BookgApprnc> [0..1]  296
{Or     Code <Cd> [1..1] CodeSet 297
Or}     Proprietary <Prtry> [1..1] ± 297
   LegalForm <LglForm> [0..1] ± 297
13.1.6.2.47.1  BookingAppearance <BookgApprnc>
Presence: [0..1]
Definition: Indicates the booking appearance of the financial Instrument.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 296 March 2024
```


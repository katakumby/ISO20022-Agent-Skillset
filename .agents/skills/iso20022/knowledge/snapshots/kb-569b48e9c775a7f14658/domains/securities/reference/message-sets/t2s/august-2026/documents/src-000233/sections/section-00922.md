---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.2 Delete <Del>", "28.4.2.1.2.2 FinancialInstrumentAttributes <FinInstrmAttrbts>", "28.4.2.1.2.2.46 SettlementInformation <SttlmInf>", "28.4.2.1.2.2.46.5 DeviatingSettlementUnit <DevtgSttlmUnit>"]
file_pages: [1348]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.2.2.46.5 DeviatingSettlementUnit <DevtgSttlmUnit>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1348 to 1348.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1348

```text
MinimumMultipleQuantity <MinMltplQty> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 2953 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 2954
Or   FaceAmount <FaceAmt> [1..1] Amount 2954
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 2954
28.4.2.1.2.2.46.5  DeviatingSettlementUnit <DevtgSttlmUnit>
Presence: [0..*]
Definition: Minimum quantity of securities that can be purchased without incurring a larger fee. For
example, if the round lot size is 100 and the trade is for 125 shares, then 100 will be processed without
a fee and the remaining 25 will incur a service fee for being an odd lot size.
DeviatingSettlementUnit <DevtgSttlmUnit> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 2953 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 2954
Or   FaceAmount <FaceAmt> [1..1] Amount 2954
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 2954
28.4.2.1.2.2.47  FinancialInstrumentForm <FinInstrmForm>
Presence: [0..1]
Definition: Indicates the form of the financial Instrument.
FinancialInstrumentForm <FinInstrmForm> contains the following FinancialInstrumentForm2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BookingAppearance <BookgApprnc> [0..1]  1348
{Or     Code <Cd> [1..1] CodeSet 1349
Or}     Proprietary <Prtry> [1..1] ± 1349
   LegalForm <LglForm> [0..1] ± 1349
28.4.2.1.2.2.47.1  BookingAppearance <BookgApprnc>
Presence: [0..1]
Definition: Indicates the booking appearance of the financial Instrument.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1348 August 2026
```


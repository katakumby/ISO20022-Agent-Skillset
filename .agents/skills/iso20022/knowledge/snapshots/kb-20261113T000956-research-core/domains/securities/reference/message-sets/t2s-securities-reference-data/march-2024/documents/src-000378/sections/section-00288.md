---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.3 CommonFinancialInstrumentAttributes11", "13.1.6.3.45 FinancialInstrumentForm <FinInstrmForm>"]
file_pages: [373]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.3.45 FinancialInstrumentForm <FinInstrmForm>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 373 to 373.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 373

```text
DeviatingSettlementUnit <DevtgSttlmUnit> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 476 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 476
Or   FaceAmount <FaceAmt> [1..1] Amount 476
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 476
13.1.6.3.45  FinancialInstrumentForm <FinInstrmForm>
Presence: [0..1]
Definition: Indicates the form of the financial Instrument.
FinancialInstrumentForm <FinInstrmForm> contains the following FinancialInstrumentForm2
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BookingAppearance <BookgApprnc> [0..1]  373
{Or     Code <Cd> [1..1] CodeSet 373
Or}     Proprietary <Prtry> [1..1] ± 374
   LegalForm <LglForm> [0..1] ± 374
13.1.6.3.45.1  BookingAppearance <BookgApprnc>
Presence: [0..1]
Definition: Indicates the booking appearance of the financial Instrument.
BookingAppearance <BookgApprnc> contains one of the following Appearance3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 373
Or}   Proprietary <Prtry> [1..1] ± 374
13.1.6.3.45.1.1  Code <Cd>
Presence: [1..1]
Definition: Appearance expressed as an ISO 20022 code.
Datatype: "Appearance1Code" on page 509
CodeName Name Definition
DELI Deliverable Physical certificates exist.
NDEL NotDeliverable Not yet deliverable contract.
LIMI Limited Limited or partial deliverability.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 373 March 2024
```


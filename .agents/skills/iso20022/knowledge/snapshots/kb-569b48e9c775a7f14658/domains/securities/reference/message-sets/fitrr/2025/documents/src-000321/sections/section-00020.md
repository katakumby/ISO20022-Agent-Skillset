---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["3 auth.017.001.02 FinancialInstrumentReportingReferenceDataReportV02", "3.4 Message Building Blocks", "3.4.2 ReferenceData <RefData>", "3.4.2.6 DerivativeInstrumentAttributes <DerivInstrmAttrbts>", "3.4.2.6.3 UnderlyingInstrument <UndrlygInstrm>", "3.4.2.6.3.2 Basket <Bskt>"]
file_pages: [29]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.017.001.02"]
---

# 3.4.2.6.3.2 Basket <Bskt>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 29 to 29.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 29

```text
3.4.2.6.3.2  Basket <Bskt>
Presence: [1..1]
Definition: Instrument consists of multiple instruments.
Impacted by: C3 "BasketInstrumentUniquenessRule", C10 "OneElementPresentRule"
Basket <Bskt> contains the following elements (see "FinancialInstrument53" on page 328 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..*] IdentifierSet 328
   LEI <LEI> [0..*] IdentifierSet 328
Constraints
• BasketInstrumentUniquenessRule
Where an underlying instrument basket is populated, all ISINs or LEIs must be unique.
• OneElementPresentRule
At least one of 5 elements must be present.
Following Must be True
    /ISIN[*] Must be present
 Or    /LEI[*] Must be present
3.4.2.6.4  OptionType <OptnTp>
Presence: [0..1]
Definition: Specifies whether it is a call option (right to purchase a specific underlying asset) or a put
option (right to sell a specific underlying asset).
Usage:
Within the scope of MiFIR, RTS 23, the following meanings should be used where a swaption is being
detailed, "Put", in case of receiver swaption, in which the buyer has the right to enter into a swap as a
fixed-rate receiver. Call", in case of payer swaption, in which the buyer has the right to enter into a swap
as a fixed-rate payer. Caps and floors shall interpret this field as, "Put", in case of a Floor, "Call", in
case of a Cap. Field only applies to derivatives that are options or warrants.
Datatype: "OptionType2Code" on page 442
CodeName Name Definition
CALL Call Right to buy a quantity of an asset for an
agreed price at exercise date.
PUTO Put Right to sell a quantity of an asset for an
agreed price at exercise date.
OTHR Other Right where the holder of the option
decides whether the option is put or call.
3.4.2.6.5  StrikePrice <StrkPric>
Presence: [0..1]
Definition: Attributes to specify the strike price of a derivative.
Approved by the Securities SEG on 17 July 2025 auth.017.001.02
FinancialInstrumentReportingReferenceDataReport
V02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
29 July 2025
```


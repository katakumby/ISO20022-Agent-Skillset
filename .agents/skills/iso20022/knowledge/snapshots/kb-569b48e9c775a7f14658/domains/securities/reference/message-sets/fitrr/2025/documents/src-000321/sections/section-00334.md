---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.2 SecuritiesTransactionReport7", "22.1.13.2.9 FinancialInstrument <FinInstrm>", "22.1.13.2.9.3 Other <Othr>", "22.1.13.2.9.3.3 DerivativeInstrumentAttributes <DerivInstrmAttrbts>", "22.1.13.2.9.3.3.8 AssetClassSpecificAttributes <AsstClssSpcfcAttrbts>", "22.1.13.2.9.3.3.8.3 Both <Both>", "22.1.13.2.9.3.3.8.3.1 Interest <Intrst>"]
file_pages: [388]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.2.9.3.3.8.3.1 Interest <Intrst>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 388 to 388.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 388

```text
Both <Both> contains the following AssetClassAttributes1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Interest <Intrst> [1..1] ± 388
   ForeignExchange <FX> [1..1] ± 388
22.1.13.2.9.3.3.8.3.1  Interest <Intrst>
Presence: [1..1]
Definition: Asset class is a non-financial instrument of type interest rate.
Interest <Intrst> contains the following elements (see "DerivativeInterest2" on page 326 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OtherNotionalCurrency <OthrNtnlCcy> [1..1] CodeSet C2 326
22.1.13.2.9.3.3.8.3.2  ForeignExchange <FX>
Presence: [1..1]
Definition: Asset class is a non-financial instrument of type foreign exchange.
ForeignExchange <FX> contains the following elements (see "DerivativeForeignExchange2" on
page 326 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OtherNotionalCurrency <OthrNtnlCcy> [1..1] CodeSet C2 326
22.1.13.2.10  InvestmentDecisionPerson <InvstmtDcsnPrsn>
Presence: [0..1]
Definition: Identifies the person or algorithm which is responsible within the reporting party for the
investment decision.
InvestmentDecisionPerson <InvstmtDcsnPrsn> contains one of the following
InvestmentParty1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Person <Prsn> [1..1] ± 388
Or}   Algorithm <Algo> [1..1] Text 389
22.1.13.2.10.1  Person <Prsn>
Presence: [1..1]
Definition: Identification of a person.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
388 July 2025
```


---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.2 SecuritiesTransactionReport7", "22.1.13.2.9 FinancialInstrument <FinInstrm>", "22.1.13.2.9.3 Other <Othr>", "22.1.13.2.9.3.3 DerivativeInstrumentAttributes <DerivInstrmAttrbts>", "22.1.13.2.9.3.3.8 AssetClassSpecificAttributes <AsstClssSpcfcAttrbts>"]
file_pages: [387]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.2.9.3.3.8 AssetClassSpecificAttributes <AsstClssSpcfcAttrbts>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 387 to 387.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 387

```text
CodeName Name Definition
OPTL Optional Determined by a third party or optional
for counterparty.
CASH Cash Cash transfer.
22.1.13.2.9.3.3.8  AssetClassSpecificAttributes <AsstClssSpcfcAttrbts>
Presence: [0..1]
Definition: Specific attributes of the underlying asset class of the financial instrument.
AssetClassSpecificAttributes <AsstClssSpcfcAttrbts> contains one of the following
AssetClassAttributes1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Interest <Intrst> [1..1] ± 387
Or   ForeignExchange <FX> [1..1] ± 387
Or}   Both <Both> [1..1]  387
     Interest <Intrst> [1..1] ± 388
     ForeignExchange <FX> [1..1] ± 388
22.1.13.2.9.3.3.8.1  Interest <Intrst>
Presence: [1..1]
Definition: Asset class is a non-financial instrument of type interest rate.
Interest <Intrst> contains the following elements (see "DerivativeInterest2" on page 326 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OtherNotionalCurrency <OthrNtnlCcy> [1..1] CodeSet C2 326
22.1.13.2.9.3.3.8.2  ForeignExchange <FX>
Presence: [1..1]
Definition: Asset class is a non-financial instrument of type foreign exchange.
ForeignExchange <FX> contains the following elements (see "DerivativeForeignExchange2" on
page 326 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OtherNotionalCurrency <OthrNtnlCcy> [1..1] CodeSet C2 326
22.1.13.2.9.3.3.8.3  Both <Both>
Presence: [1..1]
Definition: Asset class is composed of both an interest derivate and a foreign exchange derivative.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
387 July 2025
```


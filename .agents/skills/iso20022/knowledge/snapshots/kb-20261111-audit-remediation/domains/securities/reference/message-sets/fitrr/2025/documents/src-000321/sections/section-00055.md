---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03", "6.4 Message Building Blocks", "6.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "6.4.2.12 Derivative <Deriv>", "6.4.2.12.2 InterestRate <IntrstRate>", "6.4.2.12.2.1 UnderlyingType <UndrlygTp>", "6.4.2.12.2.1.2 Other <Othr>"]
file_pages: [71]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.033.001.03"]
---

# 6.4.2.12.2.1.2 Other <Othr>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 71 to 71.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 71

```text
CodeName Name Definition
XXMC FixedToFixedMultiCurrencySwap Fixed to Fixed Multi Currency Swap.
IFMC InflationMultiCurrencySwap Inflation Multi Currency Swap.
FFSC FloatToFloatSingleCurrencySwap Float to Float Single Currency Swap.
FFMC FloatToFloatMultiCurrencySwap Float to Float Multi Currency Swap.
IFSC InflationSingleCurrencySwap Inflation Single Currency Swap.
OSMC OvernightIndexMultiCurrencySwap Overnight Index Multi Currency Swap.
6.4.2.12.2.1.2  Other <Othr>
Presence: [1..1]
Definition: Where contract type is different from swaps, swaptions, futures on swaps and forwards on a
swap, this field is used.
Datatype: "UnderlyingInterestRateType3Code" on page 449
CodeName Name Definition
BOND Bond Underlying is a bond.
BNDF BondFuture Underlying is a bond future.
INTR InterestRate Underlying is interest rate.
IFUT InterestRateFutureFRA Underlying is an interest rate future or a
forward rate agreement (FRA).
6.4.2.12.2.2  UnderlyingBond <UndrlygBd>
Presence: [0..1]
Definition: Populated when the underlying type is a bond or a bond future. Details the issuer and
maturity date of the bond.
UnderlyingBond <UndrlygBd> contains the following BondDerivative2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Issuer <Issr> [1..1] IdentifierSet 71
   MaturityDate <MtrtyDt> [0..1] Date 71
   IssuanceDate <IssncDt> [0..1] Date 72
6.4.2.12.2.2.1  Issuer <Issr>
Presence: [1..1]
Definition: Legal Entity Identifier (LEI) code of the issuer of the direct or ultimate underlying bond.
Datatype: "LEIIdentifier" on page 451
6.4.2.12.2.2.2  MaturityDate <MtrtyDt>
Presence: [0..1]
Definition: Date of maturity of the underlying bond. This field applies to debt instruments with defined
maturity.
Approved by the Securities SEG on 17 July 2025 auth.033.001.03
FinancialInstrumentReportingNonEquityTransparen
cyDataReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
71 July 2025
```


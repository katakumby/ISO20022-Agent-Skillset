---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03", "6.4 Message Building Blocks", "6.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "6.4.2.12 Derivative <Deriv>", "6.4.2.12.2 InterestRate <IntrstRate>", "6.4.2.12.2.1 UnderlyingType <UndrlygTp>"]
file_pages: [70]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.033.001.03"]
---

# 6.4.2.12.2.1 UnderlyingType <UndrlygTp>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 70 to 70.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 70

```text
InterestRate <IntrstRate> contains the following InterestRateDerivative5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnderlyingType <UndrlygTp> [1..1]  70
{Or     SwapRelated <SwpRltd> [1..1] CodeSet 70
Or}     Other <Othr> [1..1] CodeSet 71
   UnderlyingBond <UndrlygBd> [0..1]  71
     Issuer <Issr> [1..1] IdentifierSet 71
     MaturityDate <MtrtyDt> [0..1] Date 71
     IssuanceDate <IssncDt> [0..1] Date 72
   SwaptionNotionalCurrency <SwptnNtnlCcy> [0..1] CodeSet C1 72
   UnderlyingSwapMaturityDate <UndrlygSwpMtrtyDt> [0..1] Date 72
   InflationIndex <InfltnIndx> [0..1]  C7 72
{Or     ISIN <ISIN> [1..1] IdentifierSet 72
Or}     Name <Nm> [1..1] Text 73
   InterestRateReference <IntrstRateRef> [1..1] ± 73
6.4.2.12.2.1  UnderlyingType <UndrlygTp>
Presence: [1..1]
Definition: Specific details on the underlying type of the interest rate derivative.
UnderlyingType <UndrlygTp> contains one of the following InterestRateDerivative2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SwapRelated <SwpRltd> [1..1] CodeSet 70
Or}   Other <Othr> [1..1] CodeSet 71
6.4.2.12.2.1.1  SwapRelated <SwpRltd>
Presence: [1..1]
Definition: Underlying interest rate type is a swap, swaption, a future on a swap or a forward on a swap
with regard to the underlying swap.
Datatype: "SwapType1Code" on page 446
CodeName Name Definition
OSSC OvernightIndexSingleCurrencySwap Overnight Index Single Currency Swap.
XFSC FixedToFloatSingleCurrencySwap Fixed to Float Single Currency Swap.
XFMC FixedToFloatMultiCurrencySwap Fixed to Float Multi Currency Swap.
XXSC FixedToFixedSingleCurrencySwap Fixed to Fixed Single Currency Swap.
Approved by the Securities SEG on 17 July 2025 auth.033.001.03
FinancialInstrumentReportingNonEquityTransparen
cyDataReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
70 July 2025
```


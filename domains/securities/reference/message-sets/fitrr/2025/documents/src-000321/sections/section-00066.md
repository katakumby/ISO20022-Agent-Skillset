---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03", "6.4 Message Building Blocks", "6.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "6.4.2.12 Derivative <Deriv>", "6.4.2.12.6 Credit <Cdt>", "6.4.2.12.6.4 CreditDefaultSwapIndexDerivative <CdtDfltSwpIndxDeriv>", "6.4.2.12.6.4.1 UnderlyingCreditDefaultSwapIdentification <UndrlygCdtDfltSwpId>"]
file_pages: [82]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.033.001.03"]
---

# 6.4.2.12.6.4.1 UnderlyingCreditDefaultSwapIdentification <UndrlygCdtDfltSwpId>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 82 to 82.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 82

```text
CreditDefaultSwapIndexDerivative <CdtDfltSwpIndxDeriv> contains the following
CreditDefaultSwapDerivative5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnderlyingCreditDefaultSwapIdentification
<UndrlygCdtDfltSwpId>
[0..1] IdentifierSet 82
   UnderlyingCreditDefaultSwapIndex
<UndrlygCdtDfltSwpIndx>
[1..1]  82
     UnderlyingIndexIdentification <UndrlygIndxId> [0..1] IdentifierSet 82
     UnderlyingIndexName <UndrlygIndxNm> [0..1] Text 83
     Series <Srs> [0..1] Quantity 83
     Version <Vrsn> [0..1] Quantity 83
     RollMonth <RollMnth> [0..12] Quantity 83
     NextRollDate <NxtRollDt> [0..1] Date 83
     NotionalCurrency <NtnlCcy> [1..1] CodeSet C2 83
6.4.2.12.6.4.1  UnderlyingCreditDefaultSwapIdentification <UndrlygCdtDfltSwpId>
Presence: [0..1]
Definition: Derivative on a credit default swap with the ISIN code of the underlying swap.
Datatype: "ISINOct2015Identifier" on page 450
6.4.2.12.6.4.2  UnderlyingCreditDefaultSwapIndex <UndrlygCdtDfltSwpIndx>
Presence: [1..1]
Definition: Describes the Credit Default Swap Index specific details the derivative is being made on.
UnderlyingCreditDefaultSwapIndex <UndrlygCdtDfltSwpIndx> contains the following
CreditDefaultSwapIndex3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnderlyingIndexIdentification <UndrlygIndxId> [0..1] IdentifierSet 82
   UnderlyingIndexName <UndrlygIndxNm> [0..1] Text 83
   Series <Srs> [0..1] Quantity 83
   Version <Vrsn> [0..1] Quantity 83
   RollMonth <RollMnth> [0..12] Quantity 83
   NextRollDate <NxtRollDt> [0..1] Date 83
   NotionalCurrency <NtnlCcy> [1..1] CodeSet C2 83
6.4.2.12.6.4.2.1  UnderlyingIndexIdentification <UndrlygIndxId>
Presence: [0..1]
Definition: Derivative on a credit default swap with the ISIN code of the underlying index.
Approved by the Securities SEG on 17 July 2025 auth.033.001.03
FinancialInstrumentReportingNonEquityTransparen
cyDataReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
82 July 2025
```


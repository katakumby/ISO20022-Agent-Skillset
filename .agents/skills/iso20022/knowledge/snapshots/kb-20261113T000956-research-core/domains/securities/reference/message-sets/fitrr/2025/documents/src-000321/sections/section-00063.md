---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03", "6.4 Message Building Blocks", "6.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "6.4.2.12 Derivative <Deriv>", "6.4.2.12.6 Credit <Cdt>", "6.4.2.12.6.2 CreditDefaultSwapIndex <CdtDfltSwpIndx>"]
file_pages: [79]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.033.001.03"]
---

# 6.4.2.12.6.2 CreditDefaultSwapIndex <CdtDfltSwpIndx>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 79 to 79.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 79

```text
SingleNameCreditDefaultSwap <SnglNmCdtDfltSwp> contains the following elements (see
"CreditDefaultSwapSingleName2" on page 325 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SovereignIssuer <SvrgnIssr> [1..1] Indicator 325
   ReferenceParty <RefPty> [0..1] ± 325
   NotionalCurrency <NtnlCcy> [1..1] CodeSet C2 325
6.4.2.12.6.2  CreditDefaultSwapIndex <CdtDfltSwpIndx>
Presence: [1..1]
Definition: A credit default swap on an index.
CreditDefaultSwapIndex <CdtDfltSwpIndx> contains the following CreditDefaultSwapIndex3
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnderlyingIndexIdentification <UndrlygIndxId> [0..1] IdentifierSet 79
   UnderlyingIndexName <UndrlygIndxNm> [0..1] Text 79
   Series <Srs> [0..1] Quantity 79
   Version <Vrsn> [0..1] Quantity 79
   RollMonth <RollMnth> [0..12] Quantity 80
   NextRollDate <NxtRollDt> [0..1] Date 80
   NotionalCurrency <NtnlCcy> [1..1] CodeSet C2 80
6.4.2.12.6.2.1  UnderlyingIndexIdentification <UndrlygIndxId>
Presence: [0..1]
Definition: Derivative on a credit default swap with the ISIN code of the underlying index.
Datatype: "ISINOct2015Identifier" on page 450
6.4.2.12.6.2.2  UnderlyingIndexName <UndrlygIndxNm>
Presence: [0..1]
Definition: To be populated for derivatives on a CDS index with the standardized name of the index.
Datatype: "Max25Text" on page 455
6.4.2.12.6.2.3  Series <Srs>
Presence: [0..1]
Definition: Series number of the composition of the index if applicable.
Datatype: "Number" on page 453
6.4.2.12.6.2.4  Version <Vrsn>
Presence: [0..1]
Approved by the Securities SEG on 17 July 2025 auth.033.001.03
FinancialInstrumentReportingNonEquityTransparen
cyDataReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
79 July 2025
```


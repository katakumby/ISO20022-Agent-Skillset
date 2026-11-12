---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03", "6.4 Message Building Blocks", "6.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "6.4.2.12 Derivative <Deriv>", "6.4.2.12.6 Credit <Cdt>", "6.4.2.12.6.1 SingleNameCreditDefaultSwap <SnglNmCdtDfltSwp>"]
file_pages: [78]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.033.001.03"]
---

# 6.4.2.12.6.1 SingleNameCreditDefaultSwap <SnglNmCdtDfltSwp>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 78 to 78.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 78

```text
Credit <Cdt> contains one of the following CreditDefaultSwapsDerivative4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SingleNameCreditDefaultSwap <SnglNmCdtDfltSwp> [1..1] ± 78
Or   CreditDefaultSwapIndex <CdtDfltSwpIndx> [1..1]  79
     UnderlyingIndexIdentification <UndrlygIndxId> [0..1] IdentifierSet 79
     UnderlyingIndexName <UndrlygIndxNm> [0..1] Text 79
     Series <Srs> [0..1] Quantity 79
     Version <Vrsn> [0..1] Quantity 79
     RollMonth <RollMnth> [0..12] Quantity 80
     NextRollDate <NxtRollDt> [0..1] Date 80
     NotionalCurrency <NtnlCcy> [1..1] CodeSet C2 80
Or   SingleNameCreditDefaultSwapDerivative
<SnglNmCdtDfltSwpDeriv>
[1..1]  C8 80
     UnderlyingCreditDefaultSwapIdentification
<UndrlygCdtDfltSwpId>
[0..1] IdentifierSet 81
     ObligationIdentification <OblgtnId> [1..1] IdentifierSet 81
     SingleName <SnglNm> [1..1] ± 81
Or}   CreditDefaultSwapIndexDerivative
<CdtDfltSwpIndxDeriv>
[1..1]  81
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
6.4.2.12.6.1  SingleNameCreditDefaultSwap <SnglNmCdtDfltSwp>
Presence: [1..1]
Definition: A credit default swap on a single name instrument.
Approved by the Securities SEG on 17 July 2025 auth.033.001.03
FinancialInstrumentReportingNonEquityTransparen
cyDataReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
78 July 2025
```


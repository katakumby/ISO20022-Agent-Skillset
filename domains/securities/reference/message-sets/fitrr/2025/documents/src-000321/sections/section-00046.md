---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03", "6.3 Constraints"]
file_pages: [58]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.033.001.03"]
---

# 6.3 Constraints

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 58 to 58.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 58

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or         SingleNameCreditDefaultSwapDerivative
<SnglNmCdtDfltSwpDeriv>
[1..1]  C8 80
           UnderlyingCreditDefaultSwapIdentification
<UndrlygCdtDfltSwpId>
[0..1] IdentifierSet 81
           ObligationIdentification <OblgtnId> [1..1] IdentifierSet 81
           SingleName <SnglNm> [1..1] ± 81
Or}         CreditDefaultSwapIndexDerivative <CdtDfltSwpIndxDeriv> [1..1]  81
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
Or}       EmissionAllowance <EmssnAllwnc> [1..1] CodeSet 84
   SupplementaryData <SplmtryData> [0..*] ± C5 84
6.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C3 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C4 NumberRule
If Number is negative, then Sign must be present.
Approved by the Securities SEG on 17 July 2025 auth.033.001.03
FinancialInstrumentReportingNonEquityTransparen
cyDataReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
58 July 2025
```


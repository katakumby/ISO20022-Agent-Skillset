---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03", "6.4 Message Building Blocks", "6.4.2 NonEquityTransparencyData <NonEqtyTrnsprncyData>", "6.4.2.12 Derivative <Deriv>", "6.4.2.12.6 Credit <Cdt>", "6.4.2.12.6.2 CreditDefaultSwapIndex <CdtDfltSwpIndx>", "6.4.2.12.6.2.5 RollMonth <RollMnth>"]
file_pages: [80]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.033.001.03"]
---

# 6.4.2.12.6.2.5 RollMonth <RollMnth>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 80 to 80.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 80

```text
Definition: New version of a series is issued if one of the constituents defaults and the index has to be
re-weighted to account for the new number of total constituents within the index.
Datatype: "Number" on page 453
6.4.2.12.6.2.5  RollMonth <RollMnth>
Presence: [0..12]
Definition: All months when the roll is expected as established by the index provider for a given year.
Field should be repeated for each month in the roll.
Datatype: "RestrictedMonthExact2Number" on page 453
6.4.2.12.6.2.6  NextRollDate <NxtRollDt>
Presence: [0..1]
Definition: To be populated in the case of a CDS Index or a derivative CDS Index with the next roll date
of the index as established by the index provider.
Datatype: "ISODate" on page 449
6.4.2.12.6.2.7  NotionalCurrency <NtnlCcy>
Presence: [1..1]
Definition: Currency in which the notional is denominated.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 417
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
6.4.2.12.6.3  SingleNameCreditDefaultSwapDerivative <SnglNmCdtDfltSwpDeriv>
Presence: [1..1]
Definition: A credit default swap derivative on a single name.
Impacted by: C8 "ValidISINRule"
SingleNameCreditDefaultSwapDerivative <SnglNmCdtDfltSwpDeriv> contains the following
CreditDefaultSwapDerivative6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnderlyingCreditDefaultSwapIdentification
<UndrlygCdtDfltSwpId>
[0..1] IdentifierSet 81
   ObligationIdentification <OblgtnId> [1..1] IdentifierSet 81
   SingleName <SnglNm> [1..1] ± 81
Approved by the Securities SEG on 17 July 2025 auth.033.001.03
FinancialInstrumentReportingNonEquityTransparen
cyDataReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
80 July 2025
```


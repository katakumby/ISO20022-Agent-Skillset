---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["19 semt.003.001.02 AccountingStatementOfHoldingsV02", "19.2 Structure"]
file_pages: [389, 390]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.003.001.02"]
---

# 19.2 Structure

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 389 to 390.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 389

```text
19.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <AcctgStmtOfHldgsV02> [1..1]  C7
   MessageIdentification <MsgId> [1..1] ± 391
   PreviousReference <PrvsRef> [0..*] ± 391
   RelatedReference <RltdRef> [0..*] ± 391
   MessagePagination <MsgPgntn> [1..1] ± 392
   StatementGeneralDetails <StmtGnlDtls> [1..1]  392
     Reference <Ref> [1..1] Text 392
     StatementDateTime <StmtDtTm> [1..1] ± 392
     CreationDateTime <CreDtTm> [0..1] ± 393
     Frequency <Frqcy> [1..1] ± 393
     UpdateType <UpdTp> [1..1] ± 393
     ActivityIndicator <ActvtyInd> [1..1] Indicator 393
     StatementBasis <StmtBsis> [1..1] ± 394
     ReportNumber <RptNb> [0..1] Text 394
     AuditedIndicator <AudtdInd> [1..1] Indicator 394
   AccountDetails <AcctDtls> [1..1] ± 394
   BalanceForAccount <BalForAcct> [0..*] ± C1, C6 395
   SubAccountDetails <SubAcctDtls> [0..*] ± 396
   TotalValues <TtlVals> [0..1] ± 396
   Extension <Xtnsn> [0..*] ± C11 396
19.3 Constraints
C1 AccruedInterestAmountSignRule
If AccruedInterestAmount is present, then AccruedInterestAmountSign must be present. If
AccruedInterestAmount is not present, then AccruedInterestAmountSign may not be present.
C2 AccruedInterestAmountSignRule
If AccruedInterestAmount is present, then AccruedInterestAmountSign must be present. If
AccruedInterestAmount is not present, then AccruedInterestAmountSign may not be present.
C3 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
Approved by the Securities SEG on 27 January 2026 semt.003.001.02
AccountingStatementOfHoldingsV02
Investment Funds - Maintenance 2025 - 2026 389 May 2026
```

## File page 390

```text
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C4 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C5 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered by the ISO 9362 Registration Authority in the BIC directory,
and consists of eight (8) or eleven (11) contiguous characters.
C6 BalanceAtSafekeepingPlaceRule
If SafekeepingPlace is present, then BalanceAtSafekeepingPlace is not allowed.
C7 BalanceForAccountOrSubAccountDetailsRule
If StatementGeneralDetails/ActivityIndicator is "true" or "1" (Yes), then either
BalanceForAccount or SubAccountDetails is mandatory. If StatementGeneralDetails/
ActivityIndicator is "false" or "0" (No), then BalanceForAccount and SubAccountDetails may be
present.
This constraint is defined at the MessageDefinition level.
C8 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C9 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C10 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C11 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C12 FinancialInstrumentIdentificationGuideline
It is recommended that ISIN be used in Identification\SecurityIdentification3Choice.
C13 Party1Rule
If PlaceSafekeeping is not SHHE, then Party is mandatory. If PlaceSafekeeping is SHHE, then
Party is optional.
C14 StreetNameAndOrPostOfficeBoxRule
If StreetName is not present, then PostOfficeBox is mandatory. If StreetName is present, then
PostOfficeBox is optional.
Approved by the Securities SEG on 27 January 2026 semt.003.001.02
AccountingStatementOfHoldingsV02
Investment Funds - Maintenance 2025 - 2026 390 May 2026
```


---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["18 semt.002.001.02 CustodyStatementOfHoldingsV02", "18.2 Structure"]
file_pages: [377, 378]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.02"]
---

# 18.2 Structure

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 377 to 378.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 377

```text
18.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <CtdyStmtOfHldgsV02> [1..1]  C9
   MessageIdentification <MsgId> [1..1] ± 379
   PreviousReference <PrvsRef> [0..*] ± 379
   RelatedReference <RltdRef> [0..*] ± 379
   MessagePagination <MsgPgntn> [1..1] ± 380
   StatementGeneralDetails <StmtGnlDtls> [1..1]  380
     Reference <Ref> [1..1] Text 380
     StatementDateTime <StmtDtTm> [1..1] ± 381
     CreationDateTime <CreDtTm> [0..1] ± 381
     Frequency <Frqcy> [1..1] ± 381
     UpdateType <UpdTp> [1..1] ± 381
     ActivityIndicator <ActvtyInd> [1..1] Indicator 382
     StatementBasis <StmtBsis> [1..1] ± 382
     ReportNumber <RptNb> [0..1] Text 382
   AccountDetails <AcctDtls> [1..1] ± 382
   BalanceForAccount <BalForAcct> [0..*] ± C1, C8,
C5
383
   SubAccountDetails <SubAcctDtls> [0..*] ± 385
   TotalValues <TtlVals> [0..1] ± 385
   Extension <Xtnsn> [0..*] ± C13 385
18.3 Constraints
C1 AccruedInterestAmountSignRule
if AccruedInterestAmount is present, then AccruedInterestAmountSign must be present. If
AccruedInterestAmount is not present, then AccruedInterestAmountSign may not be present.
C2 AccruedInterestAmountSignRule
If AccruedInterestAmount is present, then AccruedInterestAmountSign must be present. If
AccruedInterestAmount is not present, then AccruedInterestAmountSign may not be present.
C3 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
Approved by the Securities SEG on 27 January 2026 semt.002.001.02 CustodyStatementOfHoldingsV02
Investment Funds - Maintenance 2025 - 2026 377 May 2026
```

## File page 378

```text
C4 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C5 AggregateQuantityGuideline
The AggregateQuantity should be the sum of AvailableQuantity and NotAvailableQuantity if
AvailableQuantity and NotAvailableQuantity are both present.
C6 AggregateQuantityGuideline
The AggregateQuantity should be the sum of AvailableQuantity and NotAvailableQuantity if
AvailableQuantityand NotAvailableQuantity are both present.
C7 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered by the ISO 9362 Registration Authority in the BIC directory,
and consists of eight (8) or eleven (11) contiguous characters.
C8 BalanceAtSafekeepingPlaceRule
If SafekeepingPlace is present, then BalanceAtSafekeepingPlace is not allowed.
C9 BalanceForAccountOrSubAccountDetailsRule
If StatementGeneralDetails/ActivityIndicator is "true" or "1" (Yes), then either
BalanceForAccount or SubAccountDetails is mandatory. If StatementGeneralDetails/
ActivityIndicator is "false" or "0" (No), then BalanceForAccount and SubAccountDetails may be
present.
This constraint is defined at the MessageDefinition level.
C10 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C11 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C12 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C13 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C14 FinancialInstrumentIdentificationGuideline
It is recommended that ISIN be used in Identification\SecurityIdentification3Choice.
Approved by the Securities SEG on 27 January 2026 semt.002.001.02 CustodyStatementOfHoldingsV02
Investment Funds - Maintenance 2025 - 2026 378 May 2026
```


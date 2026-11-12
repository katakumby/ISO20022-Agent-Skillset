---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["21 semt.005.001.02 AccountingStatementOfHoldingsCancellationV02", "21.2 Structure"]
file_pages: [404]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.005.001.02"]
---

# 21.2 Structure

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 404 to 404.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 404

```text
21.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <AcctgStmtOfHldgsCxlV02> [1..1]  
   MessageIdentification <MsgId> [1..1] ± 405
   PreviousReference <PrvsRef> [0..1] ± 406
   RelatedReference <RltdRef> [0..1] ± 406
   MessagePagination <MsgPgntn> [1..1] ± 406
   StatementToBeCancelled <StmtToBeCanc> [0..1] ± C7 406
21.3 Constraints
C1 AccruedInterestAmountSignRule
If AccruedInterestAmount is present, then AccruedInterestAmountSign must be present. If
AccruedInterestAmount is not present, then AccruedInterestAmountSign may not be present.
C2 AccruedInterestAmountSignRule
If AccruedInterestAmount is present, then AccruedInterestAmountSign must be present. If
AccruedInterestAmount is not present, then AccruedInterestAmountSign may not be present.
C3 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
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
Approved by the Securities SEG on 27 January 2026 semt.005.001.02
AccountingStatementOfHoldingsCancellationV02
Investment Funds - Maintenance 2025 - 2026 404 May 2026
```


---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["22 semt.006.001.02 StatementOfInvestmentFundTransactionsV02", "22.3 Constraints"]
file_pages: [411]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.006.001.02"]
---

# 22.3 Constraints

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 411 to 411.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 411

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       SecuritiesForm <SctiesForm> [0..1] CodeSet 423
       ClassType <ClssTp> [0..1] Text 424
       DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 424
       TransactionDetails <TxDtls> [1..*] ± C9, C10 424
       BalanceByPage <BalByPg> [0..1] ± 426
   Extension <Xtnsn> [0..*] ± C5 426
22.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered by the ISO 9362 Registration Authority in the BIC directory,
and consists of eight (8) or eleven (11) contiguous characters.
C3 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C4 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C5 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C6 StreetNameAndOrPostOfficeBoxRule
If StreetName is not present, then PostOfficeBox is mandatory. If StreetName is present, then
PostOfficeBox is optional.
C7 TransactionOnAccountOrSubAccountDetailsRule
If StatementGeneralDetails/ActivityIndicator is "true" or "1" (Yes), then either
TransactionOnAccount or SubAccountDetails is mandatory. If StatementGeneralDetails/
ActivityIndicator is "false" or "0" (No), then TransactionOnAccount and SubAccountDetails are
not allowed.
This constraint is defined at the MessageDefinition level.
Approved by the Securities SEG on 27 January 2026 semt.006.001.02
StatementOfInvestmentFundTransactionsV02
Investment Funds - Maintenance 2025 - 2026 411 May 2026
```


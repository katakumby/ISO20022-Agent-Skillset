---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["23 semt.007.001.02 StatementOfInvestmentFundTransactionsCancellationV02", "23.2 Structure"]
file_pages: [428]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.007.001.02"]
---

# 23.2 Structure

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 428 to 428.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 428

```text
23.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <StmtOfInvstmtFndTxsCxlV02> [1..1]  
   MessageIdentification <MsgId> [1..1] ± 429
   PreviousReference <PrvsRef> [0..1] ± 429
   RelatedReference <RltdRef> [0..1] ± 429
   MessagePagination <MsgPgntn> [1..1] ± 430
   StatementToBeCancelled <StmtToBeCanc> [0..1] ± C7 430
23.3 Constraints
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
TransactionOnAccount or SubAccountDetails must be present. If StatementGeneralDetails/
ActivityIndicator is "false" or "0" (No), then TransactionOnAccount and SubAccountDetails are
not allowed.
Approved by the Securities SEG on 27 January 2026 semt.007.001.02
StatementOfInvestmentFundTransactionsCancellati
onV02
Investment Funds - Maintenance 2025 - 2026 428 May 2026
```


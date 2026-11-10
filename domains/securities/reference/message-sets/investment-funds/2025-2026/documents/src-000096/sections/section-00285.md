---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["20 semt.004.001.02 CustodyStatementOfHoldingsCancellationV02", "20.2 Structure"]
file_pages: [399]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.004.001.02"]
---

# 20.2 Structure

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 399 to 399.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 399

```text
20.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <CtdyStmtOfHldgsCxlV02> [1..1]  
   MessageIdentification <MsgId> [1..1] ± 400
   PreviousReference <PrvsRef> [0..1] ± 401
   RelatedReference <RltdRef> [0..1] ± 401
   MessagePagination <MsgPgntn> [1..1] ± 401
   StatementToBeCancelled <StmtToBeCanc> [0..1] ± C9 402
20.3 Constraints
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
Approved by the Securities SEG on 27 January 2026 semt.004.001.02
CustodyStatementOfHoldingsCancellationV02
Investment Funds - Maintenance 2025 - 2026 399 May 2026
```


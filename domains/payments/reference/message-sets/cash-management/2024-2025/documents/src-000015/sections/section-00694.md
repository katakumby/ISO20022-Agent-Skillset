---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.2 Message Datatypes", "37.2.2 CodeSet", "37.2.2.57 SystemClosureReason1Code"]
file_pages: [879]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.2.2.57 SystemClosureReason1Code

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 879 to 879.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 879

```text
CodeName Name Definition
OTCG ForecastOTCTransactions Balance representing the forecast of the
total of all cash legs of transactions
traded 'over the counter' (OTC).
OTCN NonCCPGuaranteedOTCTransactions Balance representing the forecast of the
total of all cash legs of transactions
traded 'over the counter' (OTC) not going
through central counter party (CCP)
functions.
SAPD SAPDirectDebitAmount Balance represents the settlement
account processor direct debit amount.
SAPC SAPDirectCreditAmount Balance represents the settlement
account processor direct credit amount.
REPD CMUPRepoDebit Balance represents the total of the
central moneymarkets unit processor
repo debits.
REPC CMUPRepoCredit Balance represents the total of the
central moneymarkets unit processor
repo credits.
BSCD BulkSettlementCMUPDebit Balance represents the total of the bulk
settlement and central moneymarkets
unit processor debit.
BSCC BulkSettlementCMUPCredit Balance represents the total of the bulk
settlement and central moneymarkets
unit processor credit.
SAPP SAPQueueAmount Balance represents the settlement
account processor queue amount.
IRLT IntradayRepoLimit Balance represents the intraday repo
limit.
IRDR IntradayRepoDrawings Balance represents the intraday repo
drawings.
DWRD DiscountWindowRepoDrawings Balance represents the discount window
repo drawings.
ADWR AvailableDMVForDiscountWindowRepo Balance represents the available
discounted market value for discount
window repo.
AIDR AvailableDMVForIntradayRepo Balance represents the available
discounted market value for intraday
repo.
37.2.2.57  SystemClosureReason1Code
Definition: Specifies the reason for system inactivity.
Type: CodeSet
CodeName Name Definition
BHOL BankingHoliday System is closed due to a bank holiday.
SMTN SystemMaintenance System is closed for maintenance
reasons.
NOOP NoOperation System is not processing any operation.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 879 February 2025
```


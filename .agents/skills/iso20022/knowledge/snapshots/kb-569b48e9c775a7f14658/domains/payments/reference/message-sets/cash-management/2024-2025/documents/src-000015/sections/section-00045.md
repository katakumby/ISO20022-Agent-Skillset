---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 camt.004.001.10 ReturnAccountV10", "3.4 Message Building Blocks", "3.4.2 ReportOrError <RptOrErr>", "3.4.2.1 AccountReport <AcctRpt>", "3.4.2.1.2 AccountOrError <AcctOrErr>", "3.4.2.1.2.1 Account <Acct>", "3.4.2.1.2.1.9 CurrentBilateralLimit <CurBilLmt>", "3.4.2.1.2.1.9.4 BilateralBalance <BilBal>", "3.4.2.1.2.1.9.4.3 Type <Tp>", "3.4.2.1.2.1.9.4.3.2 Proprietary <Prtry>"]
file_pages: [79]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.004.001.10"]
---

# 3.4.2.1.2.1.9.4.3.2 Proprietary <Prtry>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 79 to 79.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 79

```text
CodeName Name Definition
NSET NonSettledSecurities Balance representing the cash
equivalent of all non-settled securities
transactions.
OTCC CCPGuaranteedOTCTransactions Balance representing the Forecast of the
total of all cash-legs of transactions 'over
the counter' (OTC), going through central
counter party (CCP) functions.
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
3.4.2.1.2.1.9.4.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the nature of a balance, in a proprietary form.
Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10
Cash Management - Maintenance 2024 - 2025 79 February 2025
```


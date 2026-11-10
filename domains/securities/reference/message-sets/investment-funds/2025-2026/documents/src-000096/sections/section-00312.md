---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["23 semt.007.001.02 StatementOfInvestmentFundTransactionsCancellationV02", "23.4 Message Building Blocks", "23.4.4 MessagePagination <MsgPgntn>"]
file_pages: [430, 431, 432]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.007.001.02"]
---

# 23.4.4 MessagePagination <MsgPgntn>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 430 to 432.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 430

```text
RelatedReference <RltdRef> contains the following elements (see "AdditionalReference2" on
page 4538 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4538
   ReferenceIssuer <RefIssr> [0..1] ± 4538
   MessageName <MsgNm> [0..1] Text 4538
23.4.4 MessagePagination <MsgPgntn>
Presence: [1..1]
Definition: Pagination of the message.
MessagePagination <MsgPgntn> contains the following elements (see "Pagination" on page 4833 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 4833
   LastPageIndicator <LastPgInd> [1..1] Indicator 4833
23.4.5 StatementToBeCancelled <StmtToBeCanc>
Presence: [0..1]
Definition: The Statement of Investment Fund Transactions message to cancel.
Impacted by: C7 "TransactionOnAccountOrSubAccountDetailsRule"
Approved by the Securities SEG on 27 January 2026 semt.007.001.02
StatementOfInvestmentFundTransactionsCancellati
onV02
Investment Funds - Maintenance 2025 - 2026 430 May 2026
```

## File page 431

```text
StatementToBeCancelled <StmtToBeCanc> contains the following elements (see
"StatementOfInvestmentFundTransactions2" on page 4346 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   StatementGeneralDetails <StmtGnlDtls> [0..1]  4348
     Reference <Ref> [1..1] Text 4348
     StatementPeriod <StmtPrd> [1..1] ± 4348
     CreationDateTime <CreDtTm> [0..1] ± 4348
     Frequency <Frqcy> [0..1] CodeSet 4349
     UpdateType <UpdTp> [1..1] CodeSet 4349
     ActivityIndicator <ActvtyInd> [1..1] Indicator 4349
     ReportNumber <RptNb> [0..1] Text 4350
   InvestmentAccountDetails <InvstmtAcctDtls> [0..1] ± 4350
   TransactionOnAccount <TxOnAcct> [0..*]  4350
     Identification <Id> [1..1] ± 4351
     Name <Nm> [0..1] Text 4352
     SupplementaryIdentification <SplmtryId> [0..1] Text 4352
     SecuritiesForm <SctiesForm> [0..1] CodeSet 4352
     ClassType <ClssTp> [0..1] Text 4352
     DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4352
     TransactionDetails <TxDtls> [1..*] ± C9, C10 4352
     BalanceByPage <BalByPg> [0..1] ± 4354
   SubAccountDetails <SubAcctDtls> [1..1]  C8 4354
     Identification <Id> [1..1] ± 4355
     ActivityIndicator <ActvtyInd> [1..1] Indicator 4355
     TransactionOnSubAccount <TxOnSubAcct> [0..*]  4355
       Identification <Id> [1..1] ± 4356
       Name <Nm> [0..1] Text 4357
       SupplementaryIdentification <SplmtryId> [0..1] Text 4357
       SecuritiesForm <SctiesForm> [0..1] CodeSet 4357
       ClassType <ClssTp> [0..1] Text 4357
       DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4357
       TransactionDetails <TxDtls> [1..*] ± C9, C10 4357
       BalanceByPage <BalByPg> [0..1] ± 4359
Approved by the Securities SEG on 27 January 2026 semt.007.001.02
StatementOfInvestmentFundTransactionsCancellati
onV02
Investment Funds - Maintenance 2025 - 2026 431 May 2026
```

## File page 432

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Extension <Xtnsn> [0..*] ± C16 4359
Constraints
• TransactionOnAccountOrSubAccountDetailsRule
If StatementGeneralDetails/ActivityIndicator is "true" or "1" (Yes), then either TransactionOnAccount
or SubAccountDetails must be present. If StatementGeneralDetails/ActivityIndicator is "false" or "0"
(No), then TransactionOnAccount and SubAccountDetails are not allowed.
Approved by the Securities SEG on 27 January 2026 semt.007.001.02
StatementOfInvestmentFundTransactionsCancellati
onV02
Investment Funds - Maintenance 2025 - 2026 432 May 2026
```


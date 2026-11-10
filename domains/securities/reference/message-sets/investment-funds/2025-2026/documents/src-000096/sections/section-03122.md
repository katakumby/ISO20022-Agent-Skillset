---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.1 BalanceQuantity1Choice", "66.1.5.1.1 Quantity <Qty>"]
file_pages: [4346, 4347]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.1.1 Quantity <Qty>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4346 to 4347.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4346

```text
66.1.5.1.1  Quantity <Qty>
Presence: [1..1]
Definition: Total quantity of financial instruments of the balance.
Quantity <Qty> contains one of the following elements (see "FinancialInstrumentQuantityChoice" on
page 5142 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 5142
Or   FaceAmount <FaceAmt> [1..1] Amount 5142
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 5142
66.1.5.1.2  QuantityAsDSS <QtyAsDSS>
Presence: [1..1]
Definition: Total quantity of financial instruments of the balance.
QuantityAsDSS <QtyAsDSS> contains the following elements (see "GenericIdentification6" on
page 4553 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Issuer <Issr> [1..1] Text 4553
   Information <Inf> [1..1] Text 4553
   Balance <Bal> [1..1] Quantity 4553
66.1.5.2  StatementOfInvestmentFundTransactions2
Definition: Information about a statement of investment fund transactions.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4346 May 2026
```

## File page 4347

```text
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
   Extension <Xtnsn> [0..*] ± C16 4359
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4347 May 2026
```


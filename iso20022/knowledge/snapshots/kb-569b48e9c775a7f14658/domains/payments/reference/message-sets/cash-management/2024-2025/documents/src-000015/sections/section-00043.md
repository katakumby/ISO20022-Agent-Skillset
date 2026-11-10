---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 camt.004.001.10 ReturnAccountV10", "3.4 Message Building Blocks", "3.4.2 ReportOrError <RptOrErr>", "3.4.2.1 AccountReport <AcctRpt>", "3.4.2.1.2 AccountOrError <AcctOrErr>", "3.4.2.1.2.1 Account <Acct>", "3.4.2.1.2.1.9 CurrentBilateralLimit <CurBilLmt>", "3.4.2.1.2.1.9.2 LimitAmount <LmtAmt>"]
file_pages: [73]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.004.001.10"]
---

# 3.4.2.1.2.1.9.2 LimitAmount <LmtAmt>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 73 to 73.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 73

```text
3.4.2.1.2.1.9.2  LimitAmount <LmtAmt>
Presence: [1..1]
Definition: Amount of money of the limit, expressed in an eligible currency.
LimitAmount <LmtAmt> contains one of the following elements (see "Amount2Choice" on page 788
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 788
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 788
3.4.2.1.2.1.9.3  CreditDebitIndicator <CdtDbtInd>
Presence: [1..1]
Definition: Specifies if a limit is a debit limit or a credit limit.
Datatype: "CreditDebitCode" on page 851
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
3.4.2.1.2.1.9.4  BilateralBalance <BilBal>
Presence: [0..*]
Definition: Balance calculated with regard to one member in the system.
BilateralBalance <BilBal> contains the following CashBalance11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount 73
   CreditDebitIndicator <CdtDbtInd> [1..1] CodeSet 74
   Type <Tp> [0..1]  74
{Or     Code <Cd> [1..1] CodeSet 74
Or}     Proprietary <Prtry> [1..1] Text 79
   Status <Sts> [0..1] CodeSet 80
   ValueDate <ValDt> [0..1] ± 80
   NumberOfPayments <NbOfPmts> [0..1] Quantity 80
3.4.2.1.2.1.9.4.1  Amount <Amt>
Presence: [1..1]
Definition: Currency and amount of money of the cash balance.
Datatype: "ImpliedCurrencyAndAmount" on page 848
Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10
Cash Management - Maintenance 2024 - 2025 73 February 2025
```


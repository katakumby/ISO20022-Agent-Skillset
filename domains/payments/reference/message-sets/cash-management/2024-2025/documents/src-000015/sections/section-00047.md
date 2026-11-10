---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 camt.004.001.10 ReturnAccountV10", "3.4 Message Building Blocks", "3.4.2 ReportOrError <RptOrErr>", "3.4.2.1 AccountReport <AcctRpt>", "3.4.2.1.2 AccountOrError <AcctOrErr>", "3.4.2.1.2.1 Account <Acct>", "3.4.2.1.2.1.10 StandingOrder <StgOrdr>", "3.4.2.1.2.1.10.1 Amount <Amt>"]
file_pages: [82]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.004.001.10"]
---

# 3.4.2.1.2.1.10.1 Amount <Amt>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 82 to 82.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 82

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     PendingPredefinedOrder <PdgPrdfndOrdr> [1..1]  91
       TotalAmount <TtlAmt> [1..1] Amount 92
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 92
       Currency <Ccy> [0..1] CodeSet C1 92
     SetStandingOrder <SetStgOrdr> [1..1]  92
       TotalAmount <TtlAmt> [1..1] Amount 93
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 93
       Currency <Ccy> [0..1] CodeSet C1 93
     PendingStandingOrder <PdgStgOrdr> [1..1]  93
       TotalAmount <TtlAmt> [1..1] Amount 94
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 94
       Currency <Ccy> [0..1] CodeSet C1 94
   ZeroSweepIndicator <ZeroSweepInd> [0..1] Indicator 94
3.4.2.1.2.1.10.1  Amount <Amt>
Presence: [1..1]
Definition: Amount of money and currency to be transferred when a payment instruction is created as a
result of a standing order.
Amount <Amt> contains one of the following elements (see "Amount2Choice" on page 788 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 788
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 788
3.4.2.1.2.1.10.2  CreditDebitIndicator <CdtDbtInd>
Presence: [1..1]
Definition: Specifies if the account is debited or credited by the standing order.
Datatype: "CreditDebitCode" on page 851
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
3.4.2.1.2.1.10.3  Currency <Ccy>
Presence: [0..1]
Definition: Unique and unambiguous identification for a standing order, as assigned by the account
servicer or the account owner.
Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10
Cash Management - Maintenance 2024 - 2025 82 February 2025
```


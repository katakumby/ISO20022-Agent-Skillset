---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["9 camt.010.001.09 ReturnLimitV09", "9.4 Message Building Blocks", "9.4.2 ReportOrError <RptOrErr>", "9.4.2.1 BusinessReport <BizRpt>", "9.4.2.1.2 DefaultLimit <DfltLmt>", "9.4.2.1.2.2 LimitOrError <LmtOrErr>", "9.4.2.1.2.2.1 Limit <Lmt>", "9.4.2.1.2.2.1.6 UsedAmountCreditDebitIndicator <UsdAmtCdtDbtInd>"]
file_pages: [419]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.010.001.09"]
---

# 9.4.2.1.2.2.1.6 UsedAmountCreditDebitIndicator <UsdAmtCdtDbtInd>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 419 to 419.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 419

```text
UsedAmount <UsdAmt> contains one of the following elements (see "Amount2Choice" on page 788
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 788
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 788
9.4.2.1.2.2.1.6  UsedAmountCreditDebitIndicator <UsdAmtCdtDbtInd>
Presence: [0..1]
Definition: Specifies if the used amount of the limit is a debit amount or a credit amount.
Datatype: "CreditDebitCode" on page 851
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
9.4.2.1.2.2.1.7  UsedPercentage <UsdPctg>
Presence: [0..1]
Definition: Actual usage of the limit expressed as a percentage.
Datatype: "PercentageRate" on page 887
9.4.2.1.2.2.1.8  RemainingAmount <RmngAmt>
Presence: [0..1]
Definition: Actual usage of the limit expressed as an amount.
RemainingAmount <RmngAmt> contains one of the following elements (see "Amount2Choice" on
page 788 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 788
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 788
9.4.2.1.2.2.2  BusinessError <BizErr>
Presence: [1..*]
Definition: Reason the requested business information is not given.
BusinessError <BizErr> contains the following ErrorHandling5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  420
{Or     Code <Cd> [1..1] CodeSet 420
Or}     Proprietary <Prtry> [1..1] Text 420
   Description <Desc> [0..1] Text 420
Approved by the Payments SEG on 04 February 2025 camt.010.001.09 ReturnLimitV09
Cash Management - Maintenance 2024 - 2025 419 February 2025
```


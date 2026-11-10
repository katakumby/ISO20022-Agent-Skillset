---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["9 camt.010.001.09 ReturnLimitV09", "9.4 Message Building Blocks", "9.4.2 ReportOrError <RptOrErr>", "9.4.2.1 BusinessReport <BizRpt>", "9.4.2.1.1 CurrentLimit <CurLmt>", "9.4.2.1.1.2 LimitOrError <LmtOrErr>", "9.4.2.1.1.2.1 Limit <Lmt>", "9.4.2.1.1.2.1.2 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [408]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.010.001.09"]
---

# 9.4.2.1.1.2.1.2 CreditDebitIndicator <CdtDbtInd>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 408 to 408.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 408

```text
Amount <Amt> contains one of the following elements (see "Amount2Choice" on page 788 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 788
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 788
9.4.2.1.1.2.1.2  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Specifies if a limit is a debit limit or a credit limit.
Datatype: "CreditDebitCode" on page 851
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
9.4.2.1.1.2.1.3  Status <Sts>
Presence: [0..1]
Definition: Status of the limit, such as enabled or disabled.
Datatype: "LimitStatus1Code" on page 859
CodeName Name Definition
ENAB Enabled Limit is currently in effect.
DISA Disabled Limit is not currently in effect.
DELD Deleted Limit has been deleted or suspended.
REQD Requested Limit has been asked for and is not yet
enabled.
9.4.2.1.1.2.1.4  StartDateTime <StartDtTm>
Presence: [0..1]
Definition: Date and time at which the limit becomes effective.
StartDateTime <StartDtTm> contains one of the following elements (see "DateAndDateTime2Choice"
on page 801 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 801
Or}   DateTime <DtTm> [1..1] DateTime 801
9.4.2.1.1.2.1.5  UsedAmount <UsdAmt>
Presence: [0..1]
Definition: Actual usage of the limit expressed as an amount.
Approved by the Payments SEG on 04 February 2025 camt.010.001.09 ReturnLimitV09
Cash Management - Maintenance 2024 - 2025 408 February 2025
```


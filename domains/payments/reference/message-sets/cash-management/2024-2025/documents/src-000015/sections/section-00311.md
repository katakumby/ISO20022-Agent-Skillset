---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["10 camt.011.001.08 ModifyLimitV08", "10.4 Message Building Blocks", "10.4.2 LimitDetails <LmtDtls>", "10.4.2.3 OldLimitValueSet <OdLmtValSet>", "10.4.2.3.2 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [448]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.011.001.08"]
---

# 10.4.2.3.2 CreditDebitIndicator <CdtDbtInd>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 448 to 448.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 448

```text
Amount <Amt> contains one of the following elements (see "Amount2Choice" on page 788 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 788
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 788
10.4.2.3.2  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Specifies if a limit is a debit limit or a credit limit.
Datatype: "CreditDebitCode" on page 851
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
10.4.2.4  LimitValueAmendment <LmtValAmdmnt>
Presence: [0..1]
Definition: Difference between new limit value and old limit value.
LimitValueAmendment <LmtValAmdmnt> contains one of the following Amount4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IncreaseAmount <IncrAmt> [1..1] ± 448
Or}   DecreaseAmount <DcrAmt> [1..1] ± 448
10.4.2.4.1  IncreaseAmount <IncrAmt>
Presence: [1..1]
Definition: Amount by which the limit has increased.
IncreaseAmount <IncrAmt> contains one of the following elements (see "Amount2Choice" on
page 788 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 788
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 788
10.4.2.4.2  DecreaseAmount <DcrAmt>
Presence: [1..1]
Definition: Amount by which the limit has decreased.
Approved by the Payments SEG on 04 February 2025 camt.011.001.08 ModifyLimitV08
Cash Management - Maintenance 2024 - 2025 448 February 2025
```


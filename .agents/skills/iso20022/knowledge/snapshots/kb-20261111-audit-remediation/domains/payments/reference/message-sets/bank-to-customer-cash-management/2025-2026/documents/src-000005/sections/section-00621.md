---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.15 Miscellaneous", "6.1.15.8 TransactionInterest4", "6.1.15.8.2 Record <Rcrd>", "6.1.15.8.2.2 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [854]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.15.8.2.2 CreditDebitIndicator <CdtDbtInd>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 854 to 854.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 854

```text
6.1.15.8.2.2  CreditDebitIndicator <CdtDbtInd>
Presence: [1..1]
Definition: Indicates whether the interest amount included in the entry is credit or debit amount.
Usage: A zero amount is considered to be a credit.
Datatype: "CreditDebitCode" on page 892
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
6.1.15.8.2.3  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of interest.
Type <Tp> contains one of the following InterestType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 854
Or}   Proprietary <Prtry> [1..1] Text 854
6.1.15.8.2.3.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the type of interest.
Datatype: "InterestType1Code" on page 901
CodeName Name Definition
INDY IntraDay During or within a business day.
OVRN OverNight Period of time between the end of a
business day and the start of the next
business day (usually the day after).
6.1.15.8.2.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the type of interest in uncoded form.
Datatype: "Max35Text" on page 916
6.1.15.8.2.4  Rate <Rate>
Presence: [0..1]
Definition: Set of elements used to qualify the interest rate.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
854 March 2026
```


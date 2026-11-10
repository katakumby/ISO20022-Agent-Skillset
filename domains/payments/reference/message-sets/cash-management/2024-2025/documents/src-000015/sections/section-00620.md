---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.5 Balance", "37.1.5.1 CashBalance13", "37.1.5.1.2 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [797]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.5.1.2 CreditDebitIndicator <CdtDbtInd>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 797 to 797.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 797

```text
37.1.5.1.2  CreditDebitIndicator <CdtDbtInd>
Presence: [1..1]
Definition: Indicates whether the balance is a credit or a debit balance. A zero balance is considered to
be a credit balance.
Datatype: "CreditDebitCode" on page 851
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
37.1.5.1.3  Type <Tp>
Presence: [0..1]
Definition: Specifies the nature of a balance.
Type <Tp> contains one of the following BalanceType11Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 797
Or}   Proprietary <Prtry> [1..1] Text 797
37.1.5.1.3.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the nature of a balance, in a coded form.
Datatype: "ExternalSystemBalanceType1Code" on page 856
37.1.5.1.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the nature of a balance, in a proprietary form.
Datatype: "Max35Text" on page 889
37.1.5.1.4  Status <Sts>
Presence: [0..1]
Definition: Current status of a cash balance.
Datatype: "BalanceStatus1Code" on page 850
CodeName Name Definition
PDNG Pending Balance corresponding to the pending
transactions.
STLD Settled Final status of a transaction when the
associated transfer of cash has been
successfully processed.
37.1.5.1.5  ValueDate <ValDt>
Presence: [0..1]
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 797 February 2025
```


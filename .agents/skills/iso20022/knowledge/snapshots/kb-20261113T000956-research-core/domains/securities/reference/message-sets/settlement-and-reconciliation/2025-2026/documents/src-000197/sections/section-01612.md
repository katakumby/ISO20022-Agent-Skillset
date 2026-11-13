---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.140 SecuritiesTransactionType5Code"]
file_pages: [2160]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.140 SecuritiesTransactionType5Code

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2160 to 2160.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2160

```text
CodeName Name Definition
ISSU Issuance Relates to the issuance of a security
such as an equity or a depositary
receipt.
SLRE LendingReallocation Internal reallocation of a holding on loan
from one safekeeping account to
another.
INSP MoveOfStock Relates to a movement of shares into or
out of a pooled account.
SBBK SellBuyBack Relates to a sell buy back transaction.
REDI Withdrawal Relates to the withdrawal of specified
amounts from specified subaccounts.
INTT TradedInterestChanged Relates to a cash movement resulting
from a change in traded interest
pursuant to a coupon rate adjustment.
35.2.2.140  SecuritiesTransactionType5Code
Definition: Specifies underlying information regarding the type of transaction.
Type: CodeSet
CodeName Name Definition
TRAD Trade Relates to the settlement of a trade.
35.2.2.141  SettlementConditionModificationStatus1Code
Definition: Specifies the status of a securities settlement condition modification request.
Type: CodeSet
CodeName Name Definition
PACK AcknowledgedAccepted Instruction has been acknowledged/
accepted by the account servicer.
REJT Rejected Instruction has been rejected for further
processing.
MODP Pending Modification is pending. At this time, it is
unknown whether the modification can
be affected.
DEND Denied Modification Request will not be
executed.
MODC Completed Modification has been completed.
35.2.2.142  SettlementDate4Code
Definition: Specifies the date of settlement, in coded form.
Type: CodeSet
CodeName Name Definition
WISS WhenIssued Settlement is to be done when the
security is issued.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2160 March 2026
```


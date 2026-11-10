---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.149 SecuritiesTransactionType5Code"]
file_pages: [3300]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.149 SecuritiesTransactionType5Code

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3300 to 3300.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3300

```text
CodeName Name Definition
REBL Rebalancing Relates to a rebalanced transaction.
TRIN TransferIn Transaction is an incoming credit to an
account on the shareholders register,
and is not linked to a shift in investment
(subscription or switch), but to account
management.
TOUT TransferOut Transaction is a debit to an account on
the shareholders register, and is not
linked to a shift in investment
(redemption or switch), but to account
management.
82.2.2.149  SecuritiesTransactionType5Code
Definition: Specifies underlying information regarding the type of transaction.
Type: CodeSet
CodeName Name Definition
TRAD Trade Relates to the settlement of a trade.
82.2.2.150  SecurityStatus2Code
Definition: Specifies the status of the security.
Type: CodeSet
CodeName Name Definition
ACTV Active The status is active.
INAC Inactive The status is inactive.
SUSP Suspended The status is suspended.
82.2.2.151  SettlementDate4Code
Definition: Specifies the date of settlement, in coded form.
Type: CodeSet
CodeName Name Definition
WISS WhenIssued Settlement is to be done when the
security is issued.
82.2.2.152  SettlementQueryType1Code
Definition: Specifies the type of settlement instruction query to be executed.
Type: CodeSet
CodeName Name Definition
INST Instruction Queries settlement instructions based on
criteria excluding statuses.
STTS Status Queries settlement instructions based on
criteria that includes statuses.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3300 August 2026
```


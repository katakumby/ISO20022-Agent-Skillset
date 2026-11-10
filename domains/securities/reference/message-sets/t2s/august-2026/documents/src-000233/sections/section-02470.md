---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.133 RequestType1Code"]
file_pages: [3287]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.133 RequestType1Code

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3287 to 3287.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3287

```text
CodeName Name Definition
PAIR Pairoff Relates to a transaction that is paired off
and netted against one or more previous
transactions. A paired off transaction is a
buyback to offset and effectively
liquidate a prior sale of securities or a
sellback to offset and effectively liquidate
a prior buy of securities.
ROLP RepoContractRollover Relates to a repo rollover of a contract
extending the closing or maturity date
without the underlying collateral
impacted.
RATE RepoRate Is part of a pair-off.
CALL RepurchaseCall Relates to the early closing/maturity date
for a term repo or a termination date of
an open repo with the underlying
collateral.
CADJ Swap Relates to a swap/substitution.
TOPU TopUp Relates to a repo rollover of a position
extending the closing or maturity date.
WTHD Withdrawal Relates to a repo rollover of a position
extending the closing or maturity date.
82.2.2.133  RequestType1Code
Definition: Specifies the request used to further detail the type of information that will be queried.
Type: CodeSet
CodeName Name Definition
RT01 ReleasePending Type is a request to release the pending
transactions.
RT02 HoldNormal Type is a request to hold normal
transactions.
RT03 Cancellation Type is a request to cancellation a
transaction.
RT04 ReSequence Type is a request to change the
sequence of the transactions.
RT05 ReleaseSuspicious Type is a request to release the
suspicious transactions.
82.2.2.134  RequestType2Code
Definition: Specifies the request used to further detail the type of information that will be queried.
Type: CodeSet
CodeName Name Definition
RT11 BankPositionEnquiry Type is an enquiry on the bank's
position.
RT12 SpecificTransactionEnquiry Type is an enquiry on a specific
transaction.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3287 August 2026
```


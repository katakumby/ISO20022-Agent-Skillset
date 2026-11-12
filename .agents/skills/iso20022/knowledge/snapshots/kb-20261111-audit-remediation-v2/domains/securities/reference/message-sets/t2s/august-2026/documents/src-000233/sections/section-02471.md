---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.135 ResidenceType1Code"]
file_pages: [3288]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.135 ResidenceType1Code

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3288 to 3288.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3288

```text
CodeName Name Definition
RT13 QueuedTransactionEnquiry Type is an enquiry on a queued
transaction.
RT14 SuspiciousTransactionEnquiry Type is an enquiry on a suspicious
transaction.
RT15 PendingInwardCreditsEnquiry Type is an enquiry on pending inward
credits.
82.2.2.135  ResidenceType1Code
Definition: Specifies the type of residence where the party has its permanent home or principal
establishment.
Type: CodeSet
CodeName Name Definition
DMST Domestic Residence is domestic.
FRGN Foreign Residence is foreign.
MXED Mixed Residence is mixed
82.2.2.136  RestrictionReference1Code
Definition: Specifies the restriction references to be applied to a transaction.
Type: CodeSet
Format
minLength 1
maxLength 4
CodeName Name Definition
ADDC AddCashRestrictionReference Addition of a cash restriction reference
representing a cash sub-balance to be
utilised within the settlement instruction
for the debiting or crediting of cash.
ADDS AddSecuritiesRestrictionReference Addition of a securities restriction
reference representing a securities sub-
position to be utilised within the
settlement instruction for the delivery or
receipt of securities.
REMC RemoveCashRestrictionReference Removal of a cash restriction reference,
already present within the settlement
instruction, representing a cash sub-
balance to be utilised within the
settlement instruction for the debiting or
crediting of cash.
REMS RemoveSecuritiesRestrictionReference Removal of a securities restriction
reference, already present within the
settlement instruction, representing a
securities sub-position to be utilised
within the settlement instruction for the
delivery or receipt of securities.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3288 August 2026
```


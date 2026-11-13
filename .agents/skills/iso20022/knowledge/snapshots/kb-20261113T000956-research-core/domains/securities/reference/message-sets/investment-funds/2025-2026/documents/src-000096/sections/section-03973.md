---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.2 CodeSet", "66.2.2.2 AccountingStatus1Code"]
file_pages: [5271]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.2.2 AccountingStatus1Code

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5271 to 5271.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5271

```text
CodeName Name Definition
SECT SectorNotAllowed Status of the account modification
instruction is accepted but modification
of the account data will not be carried
out for the sector code.
66.2.2.2  AccountingStatus1Code
Definition: Specifies the accounting status.
Type: CodeSet
CodeName Name Definition
YDOM Domestic Account or party is regarded as domestic
for reporting purposes.
NDOM NotDomestic Account or party is not regarded as
domestic for reporting purposes.
66.2.2.3  AccountManagementStatus1Code
Definition: Specifies the status of an account management instruction.
Type: CodeSet
CodeName Name Definition
RECE Received The account management instruction
has been received and is acknowledged.
ACCP Accepted The account management instruction
has been validated and accepted.
EXEC ProcessingOngoing The account management instruction is
being processed and the confirmation
will follow.
STNP SentToNextParty The account management instruction
has been sent to the next party, for
example, the next intermediary.
66.2.2.4  AccountManagementType2Code
Definition: Refer to an account management instruction ie, either an account opening instruction or an
account modification instruction or a get account details message.
Type: CodeSet
CodeName Name Definition
ACCO AccountOpening Refers to an account opening instruction
message.
ACCM AccountModification Refers to an account modification
instruction message.
GACC GetAccountDetails Refers to a get account details message.
66.2.2.5  AccountManagementType3Code
Definition: Specifies the instruction for which an status is required.
Type: CodeSet
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5271 May 2026
```


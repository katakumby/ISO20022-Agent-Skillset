---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.1 BlockedStatusReason2Choice", "66.1.45.1.2 Reason <Rsn>", "66.1.45.1.2.1 TransactionType <TxTp>", "66.1.45.1.2.1.2 Proprietary <Prtry>"]
file_pages: [5167]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.1.2.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5167 to 5167.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5167

```text
66.1.45.1.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Transaction type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.45.1.2.2  Blocked <Blckd>
Presence: [1..1]
Definition: Indicates whether the account is blocked.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.45.1.2.3  Reason <Rsn>
Presence: [0..*]
Definition: Reason for the blocked status.
Reason <Rsn> contains one of the following BlockedReason2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5167
Or}   Proprietary <Prtry> [1..1] ± 5168
66.1.45.1.2.3.1  Code <Cd>
Presence: [1..1]
Definition: Reason expressed as a code.
Datatype: "BlockedReason2Code" on page 5278
CodeName Name Definition
BKRP Bankruptcy Bankruptcy.
CMMT Commitment Commitment.
CNFS Confiscation Confiscation.
MORT MortisCausa Reserved in contemplation of death.
PCOM PendingComplianceVerification Pending compliance verification.
PLDG Pledged Pledged.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5167 May 2026
```


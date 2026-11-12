---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.22 Status19Choice", "35.1.29.22.13 SettlementStatus <SttlmSts>"]
file_pages: [1917]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.22.13 SettlementStatus <SttlmSts>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1917 to 1917.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1917

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.29.22.13  SettlementStatus <SttlmSts>
Presence: [1..1]
Definition: Provides the status of settlement of a transaction.
SettlementStatus <SttlmSts> contains one of the following elements (see
"SettlementStatus19Choice" on page 1893 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1893
Or}   Proprietary <Prtry> [1..1] ± 1894
35.1.29.22.14  SettlementConditionModificationStatus <SttlmCondModSts>
Presence: [1..1]
Definition: Provides the status of a securities settlement condition modification request.
SettlementConditionModificationStatus <SttlmCondModSts> contains one of the following
SettlementConditionModificationStatus3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1917
Or}   Proprietary <Prtry> [1..1] ± 1918
35.1.29.22.14.1  Code <Cd>
Presence: [1..1]
Definition: Provides the status of the securities settlement condition modification request.
Datatype: "SettlementConditionModificationStatus1Code" on page 2160
CodeName Name Definition
PACK AcknowledgedAccepted Instruction has been acknowledged/
accepted by the account servicer.
REJT Rejected Instruction has been rejected for further
processing.
MODP Pending Modification is pending. At this time, it is
unknown whether the modification can
be affected.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1917 March 2026
```


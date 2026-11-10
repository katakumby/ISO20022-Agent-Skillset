---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.42 RepairStatus14Choice"]
file_pages: [1945]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.42 RepairStatus14Choice

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1945 to 1945.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1945

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.29.42  RepairStatus14Choice
Definition: Specifies whether the status is provided with a reason or not.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1945
Or}   Reason <Rsn> [1..*]  1945
     Code <Cd> [1..1] ± 1945
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1946
35.1.29.42.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 2087
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
35.1.29.42.2  Reason <Rsn>
Presence: [1..*]
Definition: Specifies the reason of the repair status.
Reason <Rsn> contains the following RepairReason10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] ± 1945
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1946
35.1.29.42.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a rejected or repair status.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1945 March 2026
```


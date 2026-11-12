---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000011"]
source_editions: ["Version 4 March 2024"]
message_ids: []
heading_path: ["3 Message Items Types"]
file_pages: [26]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 3 Message Items Types

Source: [src-000011](../../../../../../../../evidence/omitted/b1a725a8c57af20c03e238c2.md). Locator: one-based file pages 26 to 26.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 26

```text
3 Message Items Types
3.1 MessageComponents
3.1.1 Financial Institution Identification
3.1.1.1  ClearingSystemMemberIdentification2
Definition: Unique identification, as assigned by a clearing system, to unambiguously identify a member
of the clearing system.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClearingSystemIdentification <ClrSysId> [0..1] ± 26
   MemberIdentification <MmbId> [1..1] Text 26
3.1.1.1.1  ClearingSystemIdentification <ClrSysId>
Presence: [0..1]
Definition: Specification of a pre-agreed offering between clearing agents or the channel through which
the payment instruction is processed.
ClearingSystemIdentification <ClrSysId> contains one of the following elements (see
"ClearingSystemIdentification2Choice" on page 49 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 50
Or}   Proprietary <Prtry> [1..1] Text 50
3.1.1.1.2  MemberIdentification <MmbId>
Presence: [1..1]
Definition: Identification of a member of a clearing system.
Datatype: "Max35Text" on page 57
3.1.1.2  BranchAndFinancialInstitutionIdentification8
Definition: Unique and unambiguous identification of a financial institution or a branch of a financial
institution.
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 Message Items Types
Business Application Header - Version 4 26 March 2024
```


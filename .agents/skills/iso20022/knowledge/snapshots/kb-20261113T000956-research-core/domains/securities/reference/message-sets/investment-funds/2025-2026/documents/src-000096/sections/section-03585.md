---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.18 ModificationScope45"]
file_pages: [4835]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.18 ModificationScope45

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4835 to 4835.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4835

```text
66.1.28.18  ModificationScope45
Definition: Scope of the modification to be applied on an identified set of information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ModificationScopeIndication <ModScpIndctn> [1..1] CodeSet 4835
   AdditionalInformation <AddtlInf> [1..*] ± 4835
66.1.28.18.1  ModificationScopeIndication <ModScpIndctn>
Presence: [1..1]
Definition: Type of modification to be applied.
Datatype: "DataModification1Code" on page 5293
CodeName Name Definition
INSE InsertNewDataSet Insert a new set of data.
UPDT UpdateDataSetDetails Update the details of an existing set of
data.
DELT DeleteDataSet Delete an existing set of data.
66.1.28.18.2  AdditionalInformation <AddtlInf>
Presence: [1..*]
Definition: Additional information such as remarks or notes that must be conveyed about the party and
or limitations and restrictions.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditiononalInformation13"
on page 4867 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Limitation <Lmttn> [0..1] Text 4867
   AdditionalInformation <AddtlInf> [0..1] Text 4867
   AccountValidation <AcctVldtn> [0..1] Text 4868
   Type <Tp> [0..1] Text 4868
   Regulator <Rgltr> [0..1] ± 4868
   Status <Sts> [0..1]  4868
{Or     Code <Cd> [1..1] CodeSet 4868
Or}     Proprietary <Prtry> [1..1] ± 4869
   Period <Prd> [0..1] ± 4869
66.1.28.19  Extension1
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4835 May 2026
```


---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.16 NonEligibleProceedsIndicator3Choice"]
file_pages: [916]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.16 NonEligibleProceedsIndicator3Choice

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 916 to 916.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 916

```text
16.1.15.16  NonEligibleProceedsIndicator3Choice
Definition: Choice between a standard code or proprietary code to specify the eligibility of outturn
resources.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 916
Or}   Proprietary <Prtry> [1..1] ± 916
16.1.15.16.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify information regarding the non eligibility of the outturn resources.
Datatype: "NonEligibleProceedsIndicator1Code" on page 1222
CodeName Name Definition
NELC NonEligibleCurrency Currency not eligible for settlement in the
Central Securities Depository (CSD).
ACLI AccountLimitation Participant's account limitation.
ONEL OtherNonEligibility Other source of non eligibility.
16.1.15.16.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification to specify information regarding the non eligibility of the outturn
resources.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.17  CorporateActionProcessingStatus5Choice
Definition: Specifies the status of the details of the corporate action event.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1]  917
     EventCompletenessStatus <EvtCmpltnsSts> [1..1] CodeSet 917
     EventConfirmationStatus <EvtConfSts> [1..1] CodeSet 917
Or}   Proprietary <Prtry> [1..1] ± 917
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 916 February 2026
```


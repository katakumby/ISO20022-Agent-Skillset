---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.8 RejectionStatus37Choice", "35.1.29.8.2 Reason <Rsn>", "35.1.29.8.2.1 Code <Cd>", "35.1.29.8.2.1.2 Proprietary <Prtry>"]
file_pages: [1882]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.8.2.1.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1882 to 1882.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1882

```text
CodeName Name Definition
VALR InvalidRule Account servicer validation rule rejection.
35.1.29.8.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.29.8.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 2191
35.1.29.9  SettlementStatus18Choice
Definition: Choice of format for the settlement status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Pending <Pdg> [1..1] ± 1883
Or   Failing <Flng> [1..1]  1883
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1883
Or}     Reason <Rsn> [1..*]  1884
       Code <Cd> [1..1]  1884
{Or         Code <Cd> [1..1] CodeSet 1884
Or}         Proprietary <Prtry> [1..1] ± 1887
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1888
Or}   Proprietary <Prtry> [1..1] ± 1888
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1882 March 2026
```


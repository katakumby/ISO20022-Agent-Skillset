---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "25.4 Message Building Blocks", "25.4.6 ProcessingStatus <PrcgSts>", "25.4.6.3 Completed <Cmpltd>"]
file_pages: [813]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.031.001.11"]
---

# 25.4.6.3 Completed <Cmpltd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 813 to 813.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 813

```text
Rejected <Rjctd> contains one of the following elements (see "RejectionOrRepairStatus42Choice" on
page 1919 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1919
Or}   Reason <Rsn> [1..*]  1919
     Code <Cd> [1..1] ± 1920
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1920
25.4.6.3  Completed <Cmpltd>
Presence: [1..1]
Definition: Modification request was completed.
Impacted by: C1 "AdditionalReasonInforrmationRule"
Completed <Cmpltd> contains the following elements (see "ProprietaryReason4" on page 1899 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 1899
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1899
Constraints
• AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
25.4.6.4  Denied <Dnd>
Presence: [1..1]
Definition: Modification request will not be executed.
Denied <Dnd> contains one of the following elements (see "DeniedStatus15Choice" on page 1939 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1940
Or}   Reason <Rsn> [1..*]  1940
     Code <Cd> [1..1] ± 1940
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1940
25.4.6.5  Pending <Pdg>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 sese.031.001.11
SecuritiesSettlementConditionModificationStatusAd
viceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 813 March 2026
```


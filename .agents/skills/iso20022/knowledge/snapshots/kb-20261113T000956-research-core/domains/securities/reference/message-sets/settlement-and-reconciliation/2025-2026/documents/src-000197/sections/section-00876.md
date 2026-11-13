---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["33 sese.039.001.08 SecuritiesSettlementTransactionModificationRequestStatusAdviceV08", "33.4 Message Building Blocks", "33.4.6 ModificationProcessingStatus <ModPrcgSts>", "33.4.6.3 Denied <Dnd>"]
file_pages: [1309]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.039.001.08"]
---

# 33.4.6.3 Denied <Dnd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1309 to 1309.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1309

```text
PendingProcessing <PdgPrcg> contains one of the following elements (see
"PendingProcessingStatus23Choice" on page 2014 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2015
Or}   Reason <Rsn> [1..*]  2015
     Code <Cd> [1..1] ± 2015
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2015
33.4.6.3  Denied <Dnd>
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
33.4.6.4  Rejected <Rjctd>
Presence: [1..1]
Definition: Modification request has been rejected for further processing.
Rejected <Rjctd> contains one of the following elements (see "RejectionStatus37Choice" on
page 1879 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1879
Or}   Reason <Rsn> [1..*]  1879
     Code <Cd> [1..1]  1880
{Or       Code <Cd> [1..1] CodeSet 1880
Or}       Proprietary <Prtry> [1..1] ± 1882
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1882
33.4.6.5  Repaired <Rprd>
Presence: [1..1]
Definition: Modification request is accepted but in repair.
Approved by the Securities SEG on 27 January 2026 sese.039.001.08
SecuritiesSettlementTransactionModificationReques
tStatusAdviceV08
Settlement And Reconciliation - Maintenance 2025 - 2026 1309 March 2026
```


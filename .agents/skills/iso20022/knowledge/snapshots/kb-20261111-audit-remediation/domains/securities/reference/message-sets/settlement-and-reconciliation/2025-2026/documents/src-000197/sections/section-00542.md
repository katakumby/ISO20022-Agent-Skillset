---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "25.4 Message Building Blocks", "25.4.6 ProcessingStatus <PrcgSts>"]
file_pages: [812]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.031.001.11"]
---

# 25.4.6 ProcessingStatus <PrcgSts>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 812 to 812.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 812

```text
Linkages <Lnkgs> contains the following elements (see "Linkages73" on page 1646 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingPosition <PrcgPos> [0..1] ± C11 1646
   MessageNumber <MsgNb> [0..1] ± C20 1647
   Reference <Ref> [1..1] ± 1647
   ReferenceOwner <RefOwnr> [0..1] ± 1648
25.4.6 ProcessingStatus <PrcgSts>
Presence: [1..1]
Definition: Provides details on the processing status of the request.
ProcessingStatus <PrcgSts> contains one of the following ProcessingStatus106Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AcknowledgedAccepted <AckdAccptd> [1..1] ± 812
Or   Rejected <Rjctd> [1..1] ± 812
Or   Completed <Cmpltd> [1..1] ± C1 813
Or   Denied <Dnd> [1..1] ± 813
Or   Pending <Pdg> [1..1] ± 813
Or}   Proprietary <Prtry> [1..1] ± 814
25.4.6.1  AcknowledgedAccepted <AckdAccptd>
Presence: [1..1]
Definition: Request has been acknowledged by the account servicer.
AcknowledgedAccepted <AckdAccptd> contains one of the following elements (see
"AcknowledgedAcceptedStatus21Choice" on page 1968 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1968
Or}   Reason <Rsn> [1..*] ± 1969
25.4.6.2  Rejected <Rjctd>
Presence: [1..1]
Definition: Modification Request has been rejected for further processing.
Approved by the Securities SEG on 27 January 2026 sese.031.001.11
SecuritiesSettlementConditionModificationStatusAd
viceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 812 March 2026
```


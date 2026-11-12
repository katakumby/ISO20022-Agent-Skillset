---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["9 seev.037.001.17 CorporateActionMovementReversalAdviceV17", "9.4 Message Building Blocks", "9.4.3 EventsLinkage <EvtsLkg>"]
file_pages: [672]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.037.001.17"]
---

# 9.4.3 EventsLinkage <EvtsLkg>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 672 to 672.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 672

```text
Definition: Identification of other documents as well as the document number.
OtherDocumentIdentification <OthrDocId> contains the following elements (see
"DocumentIdentification32" on page 858 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  858
{Or     AccountServicerDocumentIdentification
<AcctSvcrDocId>
[1..1] Text 858
Or}     AccountOwnerDocumentIdentification
<AcctOwnrDocId>
[1..1] Text 858
   DocumentNumber <DocNb> [0..1] ± C6 859
   LinkageType <LkgTp> [0..1] ± C22 859
9.4.3 EventsLinkage <EvtsLkg>
Presence: [0..*]
Definition: Identification of another corporate action event that needs to be closely linked to the
processing of the event notified in this document.
EventsLinkage <EvtsLkg> contains the following elements (see "CorporateActionEventReference3"
on page 876 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   EventIdentification <EvtId> [1..1]  876
{Or     LinkedOfficialCorporateActionEventIdentification
<LkdOffclCorpActnEvtId>
[1..1] Text 876
Or}     LinkedCorporateActionIdentification <LkdCorpActnId> [1..1] Text 876
   LinkageType <LkgTp> [0..1] ± C22 877
9.4.4 ReversalReason <RvslRsn>
Presence: [0..1]
Definition: Reason for the reversal.
Impacted by: C3 "AdditionalReasonInforrmationRule"
ReversalReason <RvslRsn> contains the following CorporateActionReversalReason8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [1..1]  673
{Or     Code <Cd> [1..1] CodeSet 673
Or}     Proprietary <Prtry> [1..1] ± 673
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 674
Approved by the Securities SEG on 27 January 2026 seev.037.001.17
CorporateActionMovementReversalAdviceV17
Corporate Actions - Maintenance 2025 - 2026 672 February 2026
```


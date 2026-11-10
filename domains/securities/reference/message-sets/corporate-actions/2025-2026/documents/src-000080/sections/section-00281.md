---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.8 EventsLinkage <EvtsLkg>"]
file_pages: [389]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.8 EventsLinkage <EvtsLkg>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 389 to 389.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 389

```text
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
7.4.8 EventsLinkage <EvtsLkg>
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
7.4.9 ReversalReason <RvslRsn>
Presence: [0..1]
Definition: Reason for the reversal.
Impacted by: C5 "AdditionalReasonInforrmationRule"
ReversalReason <RvslRsn> contains the following CorporateActionReversalReason8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [1..1]  390
{Or     Code <Cd> [1..1] CodeSet 390
Or}     Proprietary <Prtry> [1..1] ± 390
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 391
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 389 February 2026
```


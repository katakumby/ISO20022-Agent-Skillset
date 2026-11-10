---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.7 EventsLinkage <EvtsLkg>"]
file_pages: [560]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.7 EventsLinkage <EvtsLkg>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 560 to 560.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 560

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
8.4.7 EventsLinkage <EvtsLkg>
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
8.4.8 TransactionIdentification <TxId>
Presence: [0..1]
Definition: Transaction type and identification information.
TransactionIdentification <TxId> contains the following TransactionIdentification15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 560
8.4.8.1  MarketInfrastructureTransactionIdentification <MktInfrstrctrTxId>
Presence: [1..1]
Definition: Identification of a transaction assigned by a market infrastructure other than a central
securities depository, for example, Target2-Securities.
Datatype: "Max35Text" on page 1251
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 560 February 2026
```


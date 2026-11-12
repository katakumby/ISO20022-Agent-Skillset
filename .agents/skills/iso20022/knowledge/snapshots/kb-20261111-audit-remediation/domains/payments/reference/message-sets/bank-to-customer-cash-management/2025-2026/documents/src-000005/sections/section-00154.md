---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.21 ReturnInformation <RtrInf>", "2.4.2.15.18.2.21.3 Reason <Rsn>", "2.4.2.15.18.2.21.3.1 Code <Cd>"]
file_pages: [228]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.21.3.1 Code <Cd>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 228 to 228.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 228

```text
Reason <Rsn> contains one of the following ReturnReason5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 228
Or}   Proprietary <Prtry> [1..1] Text 228
2.4.2.15.18.2.21.3.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the return, as published in an external reason code list.
Datatype: "ExternalReturnReason1Code" on page 900
2.4.2.15.18.2.21.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the return, in a proprietary form.
Datatype: "Max35Text" on page 916
2.4.2.15.18.2.21.4  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Further details on the return reason.
Datatype: "Max105Text" on page 914
2.4.2.15.18.2.22  RelatedCorporateAction <RltdCorpActn>
Presence: [0..1]
Definition: Set of elements used to identify the underlying corporate action.
RelatedCorporateAction <RltdCorpActn> contains the following CorporateAction82 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   EventType <EvtTp> [1..1] ± C12 228
   CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 229
   OfficialCorporateActionEventIdentification
<OffclCorpActnEvtId>
[0..1] Text 229
2.4.2.15.18.2.22.1  EventType <EvtTp>
Presence: [1..1]
Definition: Type of corporate action event.
Impacted by: C12 "EventTypeRule"
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
228 March 2026
```


---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.21 ReturnInformation <RtrInf>", "4.4.2.14.18.2.21.3 Reason <Rsn>", "4.4.2.14.18.2.21.3.1 Code <Cd>"]
file_pages: [746]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.21.3.1 Code <Cd>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 746 to 746.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 746

```text
Reason <Rsn> contains one of the following ReturnReason5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 746
Or}   Proprietary <Prtry> [1..1] Text 746
4.4.2.14.18.2.21.3.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the return, as published in an external reason code list.
Datatype: "ExternalReturnReason1Code" on page 900
4.4.2.14.18.2.21.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the return, in a proprietary form.
Datatype: "Max35Text" on page 916
4.4.2.14.18.2.21.4  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Further details on the return reason.
Datatype: "Max105Text" on page 914
4.4.2.14.18.2.22  RelatedCorporateAction <RltdCorpActn>
Presence: [0..1]
Definition: Set of elements used to identify the underlying corporate action.
RelatedCorporateAction <RltdCorpActn> contains the following CorporateAction82 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   EventType <EvtTp> [1..1] ± C12 746
   CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 747
   OfficialCorporateActionEventIdentification
<OffclCorpActnEvtId>
[0..1] Text 747
4.4.2.14.18.2.22.1  EventType <EvtTp>
Presence: [1..1]
Definition: Type of corporate action event.
Impacted by: C12 "EventTypeRule"
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
746 March 2026
```


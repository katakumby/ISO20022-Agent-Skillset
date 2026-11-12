---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.2 SearchCriteria <SchCrit>", "4.4.2.2.2.2.3 PaymentSearch <PmtSch>", "4.4.2.2.2.2.3.3 PaymentIdentification <PmtId>", "4.4.2.2.2.2.3.3.4 LongBusinessIdentification <LngBizId>", "4.4.2.2.2.2.3.3.4.8 EntryType <NtryTp>"]
file_pages: [154]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.2.3.3.4.8 EntryType <NtryTp>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 154 to 154.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 154

```text
InstructedAgent <InstdAgt> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 803 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  804
     BICFI <BICFI> [0..1] IdentifierSet C2 804
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 805
     LEI <LEI> [0..1] IdentifierSet 805
     Name <Nm> [0..1] Text 805
     PostalAddress <PstlAdr> [0..1] ± 805
     Other <Othr> [0..1] ± 806
   BranchIdentification <BrnchId> [0..1]  807
     Identification <Id> [0..1] Text 807
     LEI <LEI> [0..1] IdentifierSet 807
     Name <Nm> [0..1] Text 807
     PostalAddress <PstlAdr> [0..1] ± 807
4.4.2.2.2.2.3.3.4.8  EntryType <NtryTp>
Presence: [0..1]
Definition: Optional qualifier providing additional system specific information about the entry.
Datatype: "EntryTypeIdentifier" on page 884
4.4.2.2.2.2.3.3.4.9  EndToEndIdentification <EndToEndId>
Presence: [0..1]
Definition: Unique identification, as assigned by the initiating party, to unambiguously identify the
transaction. This identification is passed on, unchanged, throughout the entire end-to-end chain.
Usage: The end-to-end identification can be used for reconciliation or to link tasks relating to the
transaction.
It can be included in several messages related to the transaction.
Usage: this is the former RelatedReference.
Datatype: "Max35Text" on page 889
4.4.2.2.2.2.3.3.5  ShortBusinessIdentification <ShrtBizId>
Presence: [1..1]
Definition: Business identification of the payment instruction given by the clearing agent.
Impacted by: C18 "TransactionIdentificationPresenceRule"
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 154 February 2025
```


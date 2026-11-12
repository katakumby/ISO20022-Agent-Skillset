---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.10 RelatedAgents <RltdAgts>", "4.4.2.14.18.2.10.8 ReceivingAgent <RcvgAgt>"]
file_pages: [676]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.10.8 ReceivingAgent <RcvgAgt>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 676 to 676.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 676

```text
IntermediaryAgent3 <IntrmyAgt3> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 830 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  830
     BICFI <BICFI> [0..1] IdentifierSet C3 831
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 831
     LEI <LEI> [0..1] IdentifierSet 831
     Name <Nm> [0..1] Text 831
     PostalAddress <PstlAdr> [0..1] ± 832
     Other <Othr> [0..1] ± 832
   BranchIdentification <BrnchId> [0..1]  833
     Identification <Id> [0..1] Text 833
     LEI <LEI> [0..1] IdentifierSet 833
     Name <Nm> [0..1] Text 833
     PostalAddress <PstlAdr> [0..1] ± 833
4.4.2.14.18.2.10.8  ReceivingAgent <RcvgAgt>
Presence: [0..1]
Definition: Party that receives securities from the delivering agent at the place of settlement, such as
central securities depository.
Can also be used in the context of treasury operations.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
676 March 2026
```


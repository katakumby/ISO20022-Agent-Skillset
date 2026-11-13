---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.18 EntryDetails <NtryDtls>", "3.4.2.15.18.2 TransactionDetails <TxDtls>", "3.4.2.15.18.2.10 RelatedAgents <RltdAgts>", "3.4.2.15.18.2.10.4 CreditorAgent <CdtrAgt>"]
file_pages: [415]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.18.2.10.4 CreditorAgent <CdtrAgt>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 415 to 415.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 415

```text
3.4.2.15.18.2.10.4  CreditorAgent <CdtrAgt>
Presence: [0..1]
Definition: Financial institution servicing an account for the creditor.
CreditorAgent <CdtrAgt> contains the following elements (see
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
3.4.2.15.18.2.10.5  IntermediaryAgent1 <IntrmyAgt1>
Presence: [0..1]
Definition: Agent between the debtor's agent and the creditor's agent.
Usage: If more than one intermediary agent is present, then IntermediaryAgent1 identifies the agent
between the DebtorAgent and the IntermediaryAgent2.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
415 March 2026
```


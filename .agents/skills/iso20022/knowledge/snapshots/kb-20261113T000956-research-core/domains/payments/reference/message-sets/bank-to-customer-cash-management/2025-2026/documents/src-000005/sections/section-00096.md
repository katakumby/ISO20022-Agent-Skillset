---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.10 RelatedAgents <RltdAgts>", "2.4.2.15.18.2.10.11 SettlementPlace <SttlmPlc>"]
file_pages: [161]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.10.11 SettlementPlace <SttlmPlc>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 161 to 161.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 161

```text
2.4.2.15.18.2.10.11  SettlementPlace <SttlmPlc>
Presence: [0..1]
Definition: Place where settlement of the securities takes place.
Usage: This is typed by a financial institution identification as this is the standard way to identify a
securities settlement agent/central system.
SettlementPlace <SttlmPlc> contains the following elements (see
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
2.4.2.15.18.2.10.12  Proprietary <Prtry>
Presence: [0..*]
Definition: Proprietary agent related to the underlying transaction.
Proprietary <Prtry> contains the following ProprietaryAgent5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] Text 161
   Agent <Agt> [1..1] ± 161
2.4.2.15.18.2.10.12.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the type of proprietary agent.
Datatype: "Max35Text" on page 916
2.4.2.15.18.2.10.12.2  Agent <Agt>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
161 March 2026
```


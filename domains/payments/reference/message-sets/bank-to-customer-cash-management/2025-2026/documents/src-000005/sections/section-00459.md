---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.10 RelatedAgents <RltdAgts>", "4.4.2.14.18.2.10.11 SettlementPlace <SttlmPlc>"]
file_pages: [679]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.10.11 SettlementPlace <SttlmPlc>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 679 to 679.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 679

```text
4.4.2.14.18.2.10.11  SettlementPlace <SttlmPlc>
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
4.4.2.14.18.2.10.12  Proprietary <Prtry>
Presence: [0..*]
Definition: Proprietary agent related to the underlying transaction.
Proprietary <Prtry> contains the following ProprietaryAgent5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] Text 679
   Agent <Agt> [1..1] ± 679
4.4.2.14.18.2.10.12.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the type of proprietary agent.
Datatype: "Max35Text" on page 916
4.4.2.14.18.2.10.12.2  Agent <Agt>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
679 March 2026
```


---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 camt.005.001.11 GetTransactionV11", "4.4 Message Building Blocks", "4.4.2 TransactionQueryDefinition <TxQryDef>", "4.4.2.2 TransactionCriteria <TxCrit>", "4.4.2.2.2 NewCriteria <NewCrit>", "4.4.2.2.2.2 SearchCriteria <SchCrit>", "4.4.2.2.2.2.1 PaymentTo <PmtTo>", "4.4.2.2.2.2.1.1 SystemIdentification <SysId>", "4.4.2.2.2.2.1.1.2 Proprietary <Prtry>"]
file_pages: [136]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.005.001.11"]
---

# 4.4.2.2.2.2.1.1.2 Proprietary <Prtry>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 136 to 136.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 136

```text
Definition: Infrastructure through which the payment instruction is processed, as published in an
external clearing system identification code list.
Datatype: "ExternalCashClearingSystem1Code" on page 853
4.4.2.2.2.2.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Clearing system identification in a proprietary form.
Datatype: "Max35Text" on page 889
4.4.2.2.2.2.1.2  MemberIdentification <MmbId>
Presence: [0..*]
Definition: Unique and unambiguous identification of a member within a system, assigned using the
member identification scheme of the system.
MemberIdentification <MmbId> contains the following elements (see
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
4.4.2.2.2.2.1.3  Country <Ctry>
Presence: [0..1]
Definition: Country in which the system is located.
Impacted by: C5 "Country"
Datatype: "CountryCode" on page 851
Approved by the Payments SEG on 04 February 2025 camt.005.001.11 GetTransactionV11
Cash Management - Maintenance 2024 - 2025 136 February 2025
```


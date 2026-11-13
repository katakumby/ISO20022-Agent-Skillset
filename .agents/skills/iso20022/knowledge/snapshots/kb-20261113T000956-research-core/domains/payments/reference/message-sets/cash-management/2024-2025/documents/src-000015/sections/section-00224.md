---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 camt.007.001.10 ModifyTransactionV10", "6.4 Message Building Blocks", "6.4.2 Modification <Mod>", "6.4.2.1 PaymentIdentification <PmtId>", "6.4.2.1.6 ProprietaryIdentification <PrtryId>"]
file_pages: [341]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.007.001.10"]
---

# 6.4.2.1.6 ProprietaryIdentification <PrtryId>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 341 to 341.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 341

```text
InstructingAgent <InstgAgt> contains the following elements (see
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
6.4.2.1.6  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Unique proprietary reference of the underlying payment instruction assigned by the system.
Datatype: "Max70Text" on page 890
6.4.2.2  NewPaymentValueSet <NewPmtValSet>
Presence: [1..1]
Definition: New payment values.
Approved by the Payments SEG on 04 February 2025 camt.007.001.10 ModifyTransactionV10
Cash Management - Maintenance 2024 - 2025 341 February 2025
```


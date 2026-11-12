---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.14 Charges <Chrgs>", "3.4.2.15.14.2 Record <Rcrd>", "3.4.2.15.14.2.8 Tax <Tax>"]
file_pages: [338]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.14.2.8 Tax <Tax>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 338 to 338.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 338

```text
Agent <Agt> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on
page 830 for details)
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
3.4.2.15.14.2.8  Tax <Tax>
Presence: [0..1]
Definition: Provides details on the tax applied to charges.
Tax <Tax> contains the following TaxCharges2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 338
   Rate <Rate> [0..1] Rate 338
   Amount <Amt> [0..1] Amount C2, C6 339
3.4.2.15.14.2.8.1  Identification <Id>
Presence: [0..1]
Definition: Unique reference to unambiguously identify the nature of the tax levied, such as Value
Added Tax (VAT).
Datatype: "Max35Text" on page 916
3.4.2.15.14.2.8.2  Rate <Rate>
Presence: [0..1]
Definition: Rate used to calculate the tax.
Datatype: "PercentageRate" on page 913
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
338 March 2026
```


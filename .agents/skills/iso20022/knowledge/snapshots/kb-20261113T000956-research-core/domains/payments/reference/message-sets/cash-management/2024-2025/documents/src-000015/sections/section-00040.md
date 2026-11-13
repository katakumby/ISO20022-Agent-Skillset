---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 camt.004.001.10 ReturnAccountV10", "3.4 Message Building Blocks", "3.4.2 ReportOrError <RptOrErr>", "3.4.2.1 AccountReport <AcctRpt>", "3.4.2.1.2 AccountOrError <AcctOrErr>", "3.4.2.1.2.1 Account <Acct>", "3.4.2.1.2.1.8 MultilateralBalance <MulBal>"]
file_pages: [70]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.004.001.10"]
---

# 3.4.2.1.2.1.8 MultilateralBalance <MulBal>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 70 to 70.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 70

```text
Servicer <Svcr> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on
page 803 for details)
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
3.4.2.1.2.1.8  MultilateralBalance <MulBal>
Presence: [0..*]
Definition: Balance is calculated with regard to many members in the system.
Approved by the Payments SEG on 04 February 2025 camt.004.001.10 ReturnAccountV10
Cash Management - Maintenance 2024 - 2025 70 February 2025
```


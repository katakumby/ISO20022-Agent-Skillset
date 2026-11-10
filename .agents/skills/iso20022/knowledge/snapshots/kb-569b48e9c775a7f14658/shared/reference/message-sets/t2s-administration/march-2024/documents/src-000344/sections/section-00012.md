---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["2 admi.005.001.02 ReportQueryRequestV02", "2.4 Message Building Blocks", "2.4.2 ReportQueryCriteria <RptQryCrit>", "2.4.2.2 SearchCriteria <SchCrit>", "2.4.2.2.2 Balance <Bal>", "2.4.2.2.2.3 CounterpartyIdentification <CtrPtyId>"]
file_pages: [16]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.005.001.02"]
---

# 2.4.2.2.2.3 CounterpartyIdentification <CtrPtyId>

Source: [src-000344](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 16 to 16.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 16

```text
CodeName Name Definition
BILA Bilateral Balance calculated regarding one
member in the system.
MULT Multilateral Balance calculated regarding all
members in the system.
2.4.2.2.2.3  CounterpartyIdentification <CtrPtyId>
Presence: [0..*]
Definition: Specifies the counterparty for which the balance is calculated.
CounterpartyIdentification <CtrPtyId> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 41 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  42
     BICFI <BICFI> [0..1] IdentifierSet C2 42
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 43
     LEI <LEI> [0..1] IdentifierSet 43
     Name <Nm> [0..1] Text 43
     PostalAddress <PstlAdr> [0..1] ± 43
     Other <Othr> [0..1] ± 44
   BranchIdentification <BrnchId> [0..1]  45
     Identification <Id> [0..1] Text 45
     LEI <LEI> [0..1] IdentifierSet 45
     Name <Nm> [0..1] Text 45
     PostalAddress <PstlAdr> [0..1] ± 45
2.4.2.2.2.4  ValueDate <ValDt>
Presence: [0..*]
Definition: Date and time at which the balance is or will be available.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
admi.005.001.02 ReportQueryRequestV02
Target2-Securities - Administration - Maintenance 2023 -
2024
16 March 2024
```


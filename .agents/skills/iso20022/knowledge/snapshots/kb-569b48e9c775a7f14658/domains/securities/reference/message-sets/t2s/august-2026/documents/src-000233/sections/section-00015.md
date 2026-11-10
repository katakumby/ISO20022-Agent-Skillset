---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["2 admi.005.001.02 ReportQueryRequestV02", "2.4 Message Building Blocks", "2.4.2 ReportQueryCriteria <RptQryCrit>", "2.4.2.2 SearchCriteria <SchCrit>", "2.4.2.2.2 Balance <Bal>", "2.4.2.2.2.3 CounterpartyIdentification <CtrPtyId>"]
file_pages: [46]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.005.001.02"]
---

# 2.4.2.2.2.3 CounterpartyIdentification <CtrPtyId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 46 to 46.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 46

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
"BranchAndFinancialInstitutionIdentification8" on page 2919 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  2920
     BICFI <BICFI> [0..1] IdentifierSet C3 2920
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 2920
     LEI <LEI> [0..1] IdentifierSet 2920
     Name <Nm> [0..1] Text 2921
     PostalAddress <PstlAdr> [0..1] ± 2921
     Other <Othr> [0..1] ± 2921
   BranchIdentification <BrnchId> [0..1]  2922
     Identification <Id> [0..1] Text 2922
     LEI <LEI> [0..1] IdentifierSet 2922
     Name <Nm> [0..1] Text 2922
     PostalAddress <PstlAdr> [0..1] ± 2923
2.4.2.2.2.4  ValueDate <ValDt>
Presence: [0..*]
Definition: Date and time at which the balance is or will be available.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
admi.005.001.02 ReportQueryRequestV02
Target2-Securities 46 August 2026
```


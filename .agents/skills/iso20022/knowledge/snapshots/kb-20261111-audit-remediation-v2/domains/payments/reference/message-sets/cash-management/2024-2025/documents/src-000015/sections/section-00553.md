---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["31 camt.070.001.06 ReturnStandingOrderV06", "31.4 Message Building Blocks", "31.4.2 ReportOrError <RptOrErr>", "31.4.2.1 Report <Rpt>", "31.4.2.1.2 StandingOrderOrError <StgOrdrOrErr>", "31.4.2.1.2.1 StandingOrder <StgOrdr>", "31.4.2.1.2.1.8 ValidityPeriod <VldtyPrd>", "31.4.2.1.2.1.8.1 FromDate <FrDt>"]
file_pages: [725]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.070.001.06"]
---

# 31.4.2.1.2.1.8.1 FromDate <FrDt>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 725 to 725.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 725

```text
ValidityPeriod <VldtyPrd> contains the following DatePeriod3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 725
   ToDate <ToDt> [0..1] Date 725
31.4.2.1.2.1.8.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 883
31.4.2.1.2.1.8.2  ToDate <ToDt>
Presence: [0..1]
Definition: End date of the range.
Datatype: "ISODate" on page 883
31.4.2.1.2.1.9  SystemMember <SysMmb>
Presence: [0..1]
Definition: Specifies if the account is debited or credited by the standing order.
SystemMember <SysMmb> contains the following elements (see
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
31.4.2.1.2.1.10  ResponsibleParty <RspnsblPty>
Presence: [0..1]
Approved by the Payments SEG on 04 February 2025 camt.070.001.06 ReturnStandingOrderV06
Cash Management - Maintenance 2024 - 2025 725 February 2025
```


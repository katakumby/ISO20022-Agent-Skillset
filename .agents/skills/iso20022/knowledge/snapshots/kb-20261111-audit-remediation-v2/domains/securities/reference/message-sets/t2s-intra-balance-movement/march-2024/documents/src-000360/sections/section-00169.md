---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["10 camt.079.001.02 IntraBalanceMovementQueryResponseV02", "10.4 Message Building Blocks", "10.4.4 ReportOrError <RptOrErr>", "10.4.4.1 Movements <Mvmnts>", "10.4.4.1.4 StatusAndReason <StsAndRsn>"]
file_pages: [207]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.079.001.02"]
---

# 10.4.4.1.4 StatusAndReason <StsAndRsn>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 207 to 207.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 207

```text
CashAccountServicer <CshAcctSvcr> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 400 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  401
     BICFI <BICFI> [0..1] IdentifierSet C6 401
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 402
     LEI <LEI> [0..1] IdentifierSet 402
     Name <Nm> [0..1] Text 402
     PostalAddress <PstlAdr> [0..1] ± 402
     Other <Othr> [0..1] ± 403
   BranchIdentification <BrnchId> [0..1]  404
     Identification <Id> [0..1] Text 404
     LEI <LEI> [0..1] IdentifierSet 404
     Name <Nm> [0..1] Text 404
     PostalAddress <PstlAdr> [0..1] ± 404
10.4.4.1.4  StatusAndReason <StsAndRsn>
Presence: [0..1]
Definition: Status and status reason of the transaction.
StatusAndReason <StsAndRsn> contains the following IntraBalanceStatusAndReason2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingStatus <PrcgSts> [0..*] ± 207
   SettlementStatus <SttlmSts> [0..*] ± C17 208
   Settled <Sttld> [0..1] ± C5 208
10.4.4.1.4.1  ProcessingStatus <PrcgSts>
Presence: [0..*]
Definition: Provides details on the processing status of the transaction.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.079.001.02
IntraBalanceMovementQueryResponseV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
207 March 2024
```


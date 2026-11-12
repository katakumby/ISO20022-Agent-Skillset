---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["9 camt.078.001.02 IntraBalanceMovementQueryV02", "9.4 Message Building Blocks", "9.4.2 QueryDefinition <QryDef>", "9.4.2.2 SearchCriteria <SchCrit>", "9.4.2.2.2 Status <Sts>", "9.4.2.2.2.1 Type <Tp>"]
file_pages: [167]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.078.001.02"]
---

# 9.4.2.2.2.1 Type <Tp>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 167 to 167.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 167

```text
9.4.2.2.2.1  Type <Tp>
Presence: [1..1]
Definition: Defines the status type of query criteria.
Type <Tp> contains the following IntraBalanceStatusType2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingStatus <PrcgSts> [0..*] ± 167
   SettlementStatus <SttlmSts> [0..*] ± 167
   Settled <Sttld> [0..1] ± C3 167
9.4.2.2.2.1.1  ProcessingStatus <PrcgSts>
Presence: [0..*]
Definition: Provides details on the processing status of the transaction.
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus68Choice" on page 455 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 455
Or}   Proprietary <Prtry> [1..1] ± 456
9.4.2.2.2.1.2  SettlementStatus <SttlmSts>
Presence: [0..*]
Definition: Provides the settlement status of a transaction.
SettlementStatus <SttlmSts> contains one of the following elements (see
"SettlementStatus26Choice" on page 449 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 449
Or}   Proprietary <Prtry> [1..1] ± 449
9.4.2.2.2.1.3  Settled <Sttld>
Presence: [0..1]
Definition: Specifies the state or the condition.
Impacted by: C3 "AdditionalReasonInforrmationRule"
Settled <Sttld> contains the following elements (see "ProprietaryReason4" on page 436 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 436
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 437
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
167 March 2024
```


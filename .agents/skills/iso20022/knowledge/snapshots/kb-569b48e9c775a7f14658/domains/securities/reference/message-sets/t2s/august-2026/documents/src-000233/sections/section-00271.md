---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["16 camt.078.001.02 IntraBalanceMovementQueryV02", "16.4 Message Building Blocks", "16.4.2 QueryDefinition <QryDef>", "16.4.2.2 SearchCriteria <SchCrit>", "16.4.2.2.2 Status <Sts>", "16.4.2.2.2.1 Type <Tp>"]
file_pages: [358]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.078.001.02"]
---

# 16.4.2.2.2.1 Type <Tp>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 358 to 358.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 358

```text
16.4.2.2.2.1  Type <Tp>
Presence: [1..1]
Definition: Defines the status type of query criteria.
Type <Tp> contains the following IntraBalanceStatusType2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingStatus <PrcgSts> [0..*] ± 358
   SettlementStatus <SttlmSts> [0..*] ± 358
   Settled <Sttld> [0..1] ± C3 358
16.4.2.2.2.1.1  ProcessingStatus <PrcgSts>
Presence: [0..*]
Definition: Provides details on the processing status of the transaction.
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus68Choice" on page 3145 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3145
Or}   Proprietary <Prtry> [1..1] ± 3145
16.4.2.2.2.1.2  SettlementStatus <SttlmSts>
Presence: [0..*]
Definition: Provides the settlement status of a transaction.
SettlementStatus <SttlmSts> contains one of the following elements (see
"SettlementStatus26Choice" on page 3129 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3129
Or}   Proprietary <Prtry> [1..1] ± 3130
16.4.2.2.2.1.3  Settled <Sttld>
Presence: [0..1]
Definition: Specifies the state or the condition.
Impacted by: C3 "AdditionalReasonInforrmationRule"
Settled <Sttld> contains the following elements (see "ProprietaryReason4" on page 3139 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] ± 3140
   AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 3140
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities 358 August 2026
```


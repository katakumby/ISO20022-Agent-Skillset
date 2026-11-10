---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["71 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "71.4 Message Building Blocks", "71.4.1 QueryDefinition <QryDef>", "71.4.1.2 SearchCriteria <SchCrit>", "71.4.1.2.2 Status <Sts>", "71.4.1.2.2.1 Type <Tp>", "71.4.1.2.2.1.1 ProcessingStatus <PrcgSts>"]
file_pages: [2431]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 71.4.1.2.2.1.1 ProcessingStatus <PrcgSts>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2431 to 2431.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2431

```text
71.4.1.2.2.1.1  ProcessingStatus <PrcgSts>
Presence: [0..*]
Definition: Provides details on the processing status of the transaction.
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ProcessingStatus70Choice" on page 3187 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3188
Or}   Proprietary <Prtry> [1..1] ± 3188
71.4.1.2.2.1.2  InferredMatchingStatus <IfrrdMtchgSts>
Presence: [0..*]
Definition: Provides the matching status of an instruction as known by the account servicer based on an
allegement. At this time no matching took place on the market (at the CSD/ICSD).
InferredMatchingStatus <IfrrdMtchgSts> contains one of the following elements (see
"MatchingStatus27Choice" on page 3151 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3152
Or}   Proprietary <Prtry> [1..1] ± 3152
71.4.1.2.2.1.3  MatchingStatus <MtchgSts>
Presence: [0..*]
Definition: Provides the matching status of the instruction.
MatchingStatus <MtchgSts> contains one of the following elements (see "MatchingStatus27Choice"
on page 3151 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3152
Or}   Proprietary <Prtry> [1..1] ± 3152
71.4.1.2.2.1.4  SettlementStatus <SttlmSts>
Presence: [0..*]
Definition: Provides the settlement status of a transaction.
SettlementStatus <SttlmSts> contains one of the following elements (see
"SettlementStatus26Choice" on page 3129 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3129
Or}   Proprietary <Prtry> [1..1] ± 3130
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities 2431 August 2026
```


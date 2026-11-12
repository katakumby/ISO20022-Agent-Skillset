---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["9 camt.078.001.02 IntraBalanceMovementQueryV02", "9.4 Message Building Blocks", "9.4.2 QueryDefinition <QryDef>", "9.4.2.2 SearchCriteria <SchCrit>", "9.4.2.2.12 EffectiveSettlementDate <FctvSttlmDt>", "9.4.2.2.12.2 DateTime <DtTm>", "9.4.2.2.12.2.3 FromToDateTime <FrToDtTm>"]
file_pages: [186]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.078.001.02"]
---

# 9.4.2.2.12.2.3 FromToDateTime <FrToDtTm>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 186 to 186.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 186

```text
9.4.2.2.12.2.3  FromToDateTime <FrToDtTm>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
FromToDateTime <FrToDtTm> contains the following elements (see "DateTimePeriod1" on page 398
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 398
   ToDateTime <ToDtTm> [1..1] DateTime 398
9.4.2.2.12.2.4  EqualDateTime <EQDtTm>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODateTime" on page 493
9.4.2.2.12.2.5  NotEqualDateTime <NEQDtTm>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODateTime" on page 493
9.4.2.2.13  Priority <Prty>
Presence: [0..*]
Definition: Specifies whether the transaction is to be executed with a high priority.
Priority <Prty> contains one of the following elements (see "PriorityNumeric4Choice" on page 414 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Numeric <Nmrc> [1..1] Text 414
Or}   Proprietary <Prtry> [1..1] ± 414
9.4.2.2.14  MessageOriginator <MsgOrgtr>
Presence: [0..*]
Definition: Party that originated the message, if other than the sender.
MessageOriginator <MsgOrgtr> contains the following elements (see "SystemPartyIdentification8" on
page 420 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 420
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 420
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.078.001.02 IntraBalanceMovementQueryV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
186 March 2024
```


---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["2 semt.028.001.01 IntraPositionMovementQueryV01", "2.4 Message Building Blocks", "2.4.1 QueryDefinition <QryDef>", "2.4.1.2 SearchCriteria <SchCrit>", "2.4.1.2.14 MessageOriginator <MsgOrgtr>"]
file_pages: [53]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.028.001.01"]
---

# 2.4.1.2.14 MessageOriginator <MsgOrgtr>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 53 to 53.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 53

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
2.4.1.2.14  MessageOriginator <MsgOrgtr>
Presence: [0..*]
Definition: Party that originated the message, if other than the sender.
MessageOriginator <MsgOrgtr> contains the following elements (see "SystemPartyIdentification8" on
page 257 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 257
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 257
2.4.1.2.15  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Specifies the creation date/time of the intra-position movement.
CreationDateTime <CreDtTm> contains one of the following DateAndDateTimeSearch5Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1]  53
{Or     FromDate <FrDt> [1..1] Date 54
Or     ToDate <ToDt> [1..1] Date 54
Or     FromToDate <FrToDt> [1..1] ± 54
Or     EqualDate <EQDt> [1..1] Date 54
Or}     NotEqualDate <NEQDt> [1..1] Date 54
Or}   DateTime <DtTm> [1..1]  54
{Or     FromDateTime <FrDtTm> [1..1] DateTime 55
Or     ToDateTime <ToDtTm> [1..1] DateTime 55
Or     FromToDateTime <FrToDtTm> [1..1] ± 55
Or     EqualDateTime <EQDtTm> [1..1] DateTime 55
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 55
2.4.1.2.15.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Approved by the Securities SEG on 21 August 2025 semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities - Settlement Restrictions 53 September 2025
```


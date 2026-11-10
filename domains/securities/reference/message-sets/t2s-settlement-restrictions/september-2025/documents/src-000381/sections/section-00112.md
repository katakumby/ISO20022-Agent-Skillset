---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["6 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01", "6.4 Message Building Blocks", "6.4.1 QueryDefinition <QryDef>", "6.4.1.2 SearchCriteria <SchCrit>", "6.4.1.2.7 CreationDateTime <CreDtTm>"]
file_pages: [141]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.032.001.01"]
---

# 6.4.1.2.7 CreationDateTime <CreDtTm>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 141 to 141.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 141

```text
MessageOriginator <MsgOrgtr> contains the following elements (see "SystemPartyIdentification8" on
page 257 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 257
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 257
6.4.1.2.7  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Specifies the creation date/time of the settlement instruction or the intra-position movement.
CreationDateTime <CreDtTm> contains one of the following DateAndDateTimeSearch5Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1]  141
{Or     FromDate <FrDt> [1..1] Date 142
Or     ToDate <ToDt> [1..1] Date 142
Or     FromToDate <FrToDt> [1..1] ± 142
Or     EqualDate <EQDt> [1..1] Date 142
Or}     NotEqualDate <NEQDt> [1..1] Date 142
Or}   DateTime <DtTm> [1..1]  142
{Or     FromDateTime <FrDtTm> [1..1] DateTime 143
Or     ToDateTime <ToDtTm> [1..1] DateTime 143
Or     FromToDateTime <FrToDtTm> [1..1] ± 143
Or     EqualDateTime <EQDtTm> [1..1] DateTime 143
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 143
6.4.1.2.7.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Approved by the Securities SEG on 21 August 2025 semt.032.001.01
SecuritiesTransactionCancellationRequestQueryV0
1
Target2-Securities - Settlement Restrictions 141 September 2025
```


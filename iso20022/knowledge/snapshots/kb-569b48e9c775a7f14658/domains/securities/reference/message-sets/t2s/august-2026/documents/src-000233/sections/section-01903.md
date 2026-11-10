---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["73 semt.028.001.01 IntraPositionMovementQueryV01", "73.4 Message Building Blocks", "73.4.1 QueryDefinition <QryDef>", "73.4.1.2 SearchCriteria <SchCrit>", "73.4.1.2.14 MessageOriginator <MsgOrgtr>"]
file_pages: [2608]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.028.001.01"]
---

# 73.4.1.2.14 MessageOriginator <MsgOrgtr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2608 to 2608.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2608

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
73.4.1.2.14  MessageOriginator <MsgOrgtr>
Presence: [0..*]
Definition: Party that originated the message, if other than the sender.
MessageOriginator <MsgOrgtr> contains the following elements (see "SystemPartyIdentification8" on
page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
73.4.1.2.15  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Specifies the creation date/time of the intra-position movement.
CreationDateTime <CreDtTm> contains one of the following DateAndDateTimeSearch5Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1]  2608
{Or     FromDate <FrDt> [1..1] Date 2609
Or     ToDate <ToDt> [1..1] Date 2609
Or     FromToDate <FrToDt> [1..1] ± 2609
Or     EqualDate <EQDt> [1..1] Date 2609
Or}     NotEqualDate <NEQDt> [1..1] Date 2609
Or}   DateTime <DtTm> [1..1]  2609
{Or     FromDateTime <FrDtTm> [1..1] DateTime 2610
Or     ToDateTime <ToDtTm> [1..1] DateTime 2610
Or     FromToDateTime <FrToDtTm> [1..1] ± 2610
Or     EqualDateTime <EQDtTm> [1..1] DateTime 2610
Or}     NotEqualDateTime <NEQDtTm> [1..1] DateTime 2610
73.4.1.2.15.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities 2608 August 2026
```


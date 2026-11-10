---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["35 reda.015.001.01 PartyQueryV01", "35.4 Message Building Blocks", "35.4.2 SearchCriteria <SchCrit>", "35.4.2.7 RestrictionIssueDate <RstrctnIsseDt>", "35.4.2.7.2 Date <Dt>", "35.4.2.7.2.3 FromToDate <FrToDt>"]
file_pages: [2066]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.015.001.01"]
---

# 35.4.2.7.2.3 FromToDate <FrToDt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2066 to 2066.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2066

```text
Datatype: "ISODate" on page 3319
35.4.2.7.2.3  FromToDate <FrToDt>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 2908 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 2908
   ToDate <ToDt> [1..1] Date 2908
35.4.2.7.2.4  EqualDate <EQDt>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODate" on page 3319
35.4.2.7.2.5  NotEqualDate <NEQDt>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODate" on page 3319
35.4.2.8  ResidenceType <ResTp>
Presence: [0..1]
Definition: Specifies the type of residence where the party has its permanent home or principal
establishment.
Datatype: "ResidenceType1Code" on page 3288
CodeName Name Definition
DMST Domestic Residence is domestic.
FRGN Foreign Residence is foreign.
MXED Mixed Residence is mixed
35.4.2.9  LockStatus <LckSts>
Presence: [0..1]
Definition: Specifies whether the party is locked or not, and the reason for this status, when required.
LockStatus <LckSts> contains the following PartyLockStatus1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidFrom <VldFr> [0..1] Date 2067
   Status <Sts> [1..1] CodeSet 2067
   LockReason <LckRsn> [0..*] Text 2067
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.015.001.01 PartyQueryV01
Target2-Securities 2066 August 2026
```


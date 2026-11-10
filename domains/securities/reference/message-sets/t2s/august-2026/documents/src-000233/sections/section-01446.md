---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["35 reda.015.001.01 PartyQueryV01", "35.4 Message Building Blocks", "35.4.2 SearchCriteria <SchCrit>", "35.4.2.1 OpeningDate <OpngDt>"]
file_pages: [2060]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.015.001.01"]
---

# 35.4.2.1 OpeningDate <OpngDt>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2060 to 2060.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2060

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ResidenceType <ResTp> [0..1] CodeSet 2066
   LockStatus <LckSts> [0..1]  2066
     ValidFrom <VldFr> [0..1] Date 2067
     Status <Sts> [1..1] CodeSet 2067
     LockReason <LckRsn> [0..*] Text 2067
35.4.2.1  OpeningDate <OpngDt>
Presence: [0..1]
Definition: Specifies the opening date of the party.
OpeningDate <OpngDt> contains one of the following DatePeriodSearch1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDate <FrDt> [1..1] Date 2060
Or   ToDate <ToDt> [1..1] Date 2060
Or   FromToDate <FrToDt> [1..1] ± 2060
Or   EqualDate <EQDt> [1..1] Date 2061
Or}   NotEqualDate <NEQDt> [1..1] Date 2061
35.4.2.1.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 3319
35.4.2.1.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 3319
35.4.2.1.3  FromToDate <FrToDt>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 2908 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 2908
   ToDate <ToDt> [1..1] Date 2908
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.015.001.01 PartyQueryV01
Target2-Securities 2060 August 2026
```


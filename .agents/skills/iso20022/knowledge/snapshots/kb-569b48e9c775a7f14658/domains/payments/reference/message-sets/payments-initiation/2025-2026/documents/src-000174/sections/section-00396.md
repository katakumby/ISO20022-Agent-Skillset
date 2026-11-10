---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.8 Frequency", "6.1.8.1 Frequency36Choice", "6.1.8.1.3 PointInTime <PtInTm>", "6.1.8.1.3.2 PointInTime <PtInTm>"]
file_pages: [547]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.8.1.3.2 PointInTime <PtInTm>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 547 to 547.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 547

```text
CodeName Name Definition
YEAR Annual Event takes place every year or once a
year.
MNTH Monthly Event takes place every month or once a
month.
QURT Quarterly Event takes place every three months or
four times a year.
MIAN SemiAnnual Event takes place every six months or
two times a year.
WEEK Weekly Event takes place once a week.
DAIL Daily Event takes place every day.
ADHO Adhoc Event takes place on request or as
necessary.
INDA IntraDay Event takes place several times a day.
FRTN Fortnightly Event takes place every two weeks.
6.1.8.1.3.2  PointInTime <PtInTm>
Presence: [1..1]
Definition: Further information on the exact point in time the event should take place.
Datatype: "Exact2NumericText" on page 607
6.1.9 Identification Information
6.1.9.1  GenericIdentification30
Definition: Information related to an identification, for example, party identification or account
identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 547
   Issuer <Issr> [1..1] Text 547
   SchemeName <SchmeNm> [0..1] Text 548
6.1.9.1.1  Identification <Id>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Datatype: "Exact4AlphaNumericText" on page 607
6.1.9.1.2  Issuer <Issr>
Presence: [1..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 609
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 547 March 2026
```


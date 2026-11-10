---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.16 Frequency"]
file_pages: [2958]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.16 Frequency

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2958 to 2958.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2958

```text
QuotingInstitution <QtgInstn> contains one of the following elements (see
"PartyIdentification120Choice" on page 3079 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C2 3079
Or   ProprietaryIdentification <PrtryId> [1..1] ± 3079
Or}   NameAndAddress <NmAndAdr> [1..1] ± 3079
82.1.16 Frequency
82.1.16.1  Frequency22Choice
Definition: Choice of format for a frequency, for example, the frequency of delivery of a statement.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2958
Or}   Proprietary <Prtry> [1..1] ± 2959
82.1.16.1.1  Code <Cd>
Presence: [1..1]
Definition: Frequency expressed as an ISO 20022 code.
Datatype: "EventFrequency7Code" on page 3238
CodeName Name Definition
YEAR Annual Event takes place every year or once a
year.
ADHO Adhoc Event takes place as necessary.
MNTH Monthly Event takes place every month or once a
month.
DAIL Daily Event takes place every day.
INDA IntraDay Event takes place several times a day.
WEEK Weekly Event takes place once a week.
SEMI SemiAnnual Event takes place every six months or
two times a year.
QUTR Quarterly Event takes place every three months or
four times a year.
TOMN EveryTwoMonths Event takes place every two months.
TOWK EveryTwoWeeks Event takes place every two weeks.
TWMN TwiceAMonth Event takes place two times a month.
OVNG Overnight Event takes place overnight.
ONDE OnDemand Event takes place on demand.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2958 August 2026
```


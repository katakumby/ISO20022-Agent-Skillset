---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.8 Frequency"]
file_pages: [477]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.8 Frequency

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 477 to 477.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 477

```text
13.1.8 Frequency
13.1.8.1  Frequency35Choice
Definition: Choice of format for a frequency, for example, the frequency of payment.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 477
Or}   Proprietary <Prtry> [1..1] ± 477
13.1.8.1.1  Code <Cd>
Presence: [1..1]
Definition: Frequency expressed as an ISO 20022 code.
Datatype: "Frequency5Code" on page 515
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
OVNG Overnight Event takes place overnight.
TEND TenDays Event takes place every ten business
days.
13.1.8.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Frequency expressed as a proprietary code.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 477 March 2024
```


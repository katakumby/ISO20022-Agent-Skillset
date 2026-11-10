---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.6 Date Time", "12.1.6.3 DateAndDateTime2Choice"]
file_pages: [390]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.6.3 DateAndDateTime2Choice

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 390 to 390.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 390

```text
Constraints
• CoexistenceIssuerSchemeNameRule
(Rule)
During ISO 15022-20022 coexistence, Issuer length must be 4 characters and SchemeName length
must be 4 characters or less. Issuer and Scheme Name must be an ISO registered Issuer and
SchemeName.
12.1.6.3  DateAndDateTime2Choice
Definition: Choice between a date or a date and time format.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 390
Or}   DateTime <DtTm> [1..1] DateTime 390
12.1.6.3.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Datatype: ISODate on page 487
12.1.6.3.2  DateTime <DtTm>
Presence: [1..1]
Definition: Specified date and time.
Datatype: ISODateTime on page 487
12.1.6.4  DateAndDateTimeChoice
Definition: Choice between a date or a date and time format.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 390
Or}   DateTime <DtTm> [1..1] DateTime 390
12.1.6.4.1  Date <Dt>
Presence: [1..1]
Definition: Specified date.
Datatype: ISODate on page 487
12.1.6.4.2  DateTime <DtTm>
Presence: [1..1]
Definition: Specified date and time.
Datatype: ISODateTime on page 487
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 390
```


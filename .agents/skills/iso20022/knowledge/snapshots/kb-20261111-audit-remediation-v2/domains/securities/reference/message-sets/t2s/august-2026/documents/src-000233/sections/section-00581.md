---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "27.4.2.3.20 Issuance <Issnc>", "27.4.2.3.20.1 IssuePlace <IssePlc>"]
file_pages: [766]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.3.20.1 IssuePlace <IssePlc>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 766 to 766.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 766

```text
27.4.2.3.20.1  IssuePlace <IssePlc>
Presence: [0..1]
Definition: Indicates where the financial instrument was issued.
Datatype: "MICIdentifier" on page 3322
27.4.2.3.20.2  CountryOfIssue <CtryOfIsse>
Presence: [0..1]
Definition: Country where a security is issued by the issuer or its agent.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 3234
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
27.4.2.3.20.3  IssueDate <IsseDt>
Presence: [0..1]
Definition: Date/time at which the security was made available.
Datatype: "ISODate" on page 3319
27.4.2.3.20.4  AnnouncementDate <AnncmntDt>
Presence: [0..1]
Definition: Date/time, as announced by the issuer, at which the securities will be issued.
Datatype: "ISODateTime" on page 3320
27.4.2.3.20.5  ISINValidFrom <ISINVldFr>
Presence: [0..1]
Definition: Defines the date from which the instrument code is valid. This date can be before the actual
issue date of an instrument for 'when-issued' securities, but may not be a date in the future for a new
security.
Datatype: "ISODate" on page 3319
27.4.2.3.20.6  IssuerOrganisation <IssrOrg>
Presence: [0..1]
Definition: Legal entity that has the right to issue securities.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 766 August 2026
```


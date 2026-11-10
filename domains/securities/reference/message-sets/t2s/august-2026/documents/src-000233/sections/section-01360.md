---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "32.4.3.1.1.3.18 Issuance <Issnc>", "32.4.3.1.1.3.18.2 CountryOfIssue <CtryOfIsse>"]
file_pages: [1969]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.3.18.2 CountryOfIssue <CtryOfIsse>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1969 to 1969.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1969

```text
Datatype: "MICIdentifier" on page 3322
32.4.3.1.1.3.18.2  CountryOfIssue <CtryOfIsse>
Presence: [0..1]
Definition: Country where a security is issued by the issuer or its agent.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 3234
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
32.4.3.1.1.3.18.3  IssueDate <IsseDt>
Presence: [0..1]
Definition: Date/time at which the security was made available.
Datatype: "ISODate" on page 3319
32.4.3.1.1.3.18.4  AnnouncementDate <AnncmntDt>
Presence: [0..1]
Definition: Date/time, as announced by the issuer, at which the securities will be issued.
Datatype: "ISODateTime" on page 3320
32.4.3.1.1.3.18.5  IssuerOrganisation <IssrOrg>
Presence: [0..1]
Definition: Legal entity that has the right to issue securities.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1969 August 2026
```


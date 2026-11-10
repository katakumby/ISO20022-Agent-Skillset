---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.3 CommonFinancialInstrumentAttributes11", "13.1.6.3.18 Issuance <Issnc>", "13.1.6.3.18.2 CountryOfIssue <CtryOfIsse>"]
file_pages: [338]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.3.18.2 CountryOfIssue <CtryOfIsse>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 338 to 338.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 338

```text
Datatype: "MICIdentifier" on page 531
13.1.6.3.18.2  CountryOfIssue <CtryOfIsse>
Presence: [0..1]
Definition: Country where a security is issued by the issuer or its agent.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 513
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
13.1.6.3.18.3  IssueDate <IsseDt>
Presence: [0..1]
Definition: Date/time at which the security was made available.
Datatype: "ISODate" on page 529
13.1.6.3.18.4  AnnouncementDate <AnncmntDt>
Presence: [0..1]
Definition: Date/time, as announced by the issuer, at which the securities will be issued.
Datatype: "ISODateTime" on page 529
13.1.6.3.18.5  IssuerOrganisation <IssrOrg>
Presence: [0..1]
Definition: Legal entity that has the right to issue securities.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 338 March 2024
```


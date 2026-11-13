---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["31 reda.010.001.01 SecurityQueryV01", "31.4 Message Building Blocks", "31.4.4 SmallSetReturnCriteria <SmlSetRtrCrit>", "31.4.4.3 ISOSecurityShortName <ISOSctyShrtNm>"]
file_pages: [1780]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.010.001.01"]
---

# 31.4.4.3 ISOSecurityShortName <ISOSctyShrtNm>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1780 to 1780.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1780

```text
31.4.4.3  ISOSecurityShortName <ISOSctyShrtNm>
Presence: [1..1]
Definition: Short name of the security expressed as ISO 18773/18774.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 3323):
• Meaning When True: Requested
• Meaning When False: Not Requested
31.4.4.4  ClassificationFinancialInstrument <ClssfctnFinInstrm>
Presence: [1..1]
Definition: Classification type of the financial instrument, as per the ISO Classification of Financial
Instrument (CFI) codification, for example, common share with voting rights, fully paid, or registered.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 3323):
• Meaning When True: Requested
• Meaning When False: Not Requested
31.4.4.5  MaturityDate <MtrtyDt>
Presence: [1..1]
Definition: Planned final repayment date at the time of issuance.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 3323):
• Meaning When True: Requested
• Meaning When False: Not Requested
31.4.4.6  IssueDate <IsseDt>
Presence: [1..1]
Definition: Date/time at which the security was made available.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 3323):
• Meaning When True: Requested
• Meaning When False: Not Requested
31.4.4.7  IssueCurrency <IsseCcy>
Presence: [1..1]
Definition: Currency in which a security is issued or redenominated.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 3323):
• Meaning When True: Requested
• Meaning When False: Not Requested
31.4.4.8  CountryOfIssue <CtryOfIsse>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.010.001.01 SecurityQueryV01
Target2-Securities 1780 August 2026
```


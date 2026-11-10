---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["6 reda.010.001.01 SecurityQueryV01", "6.4 Message Building Blocks", "6.4.4 SmallSetReturnCriteria <SmlSetRtrCrit>", "6.4.4.3 ISOSecurityShortName <ISOSctyShrtNm>"]
file_pages: [90]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.010.001.01"]
---

# 6.4.4.3 ISOSecurityShortName <ISOSctyShrtNm>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 90 to 90.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 90

```text
6.4.4.3  ISOSecurityShortName <ISOSctyShrtNm>
Presence: [1..1]
Definition: Short name of the security expressed as ISO 18773/18774.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 531):
• Meaning When True: Requested
• Meaning When False: Not Requested
6.4.4.4  ClassificationFinancialInstrument <ClssfctnFinInstrm>
Presence: [1..1]
Definition: Classification type of the financial instrument, as per the ISO Classification of Financial
Instrument (CFI) codification, for example, common share with voting rights, fully paid, or registered.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 531):
• Meaning When True: Requested
• Meaning When False: Not Requested
6.4.4.5  MaturityDate <MtrtyDt>
Presence: [1..1]
Definition: Planned final repayment date at the time of issuance.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 531):
• Meaning When True: Requested
• Meaning When False: Not Requested
6.4.4.6  IssueDate <IsseDt>
Presence: [1..1]
Definition: Date/time at which the security was made available.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 531):
• Meaning When True: Requested
• Meaning When False: Not Requested
6.4.4.7  IssueCurrency <IsseCcy>
Presence: [1..1]
Definition: Currency in which a security is issued or redenominated.
Datatype: One of the following values must be used (see "RequestedIndicator" on page 531):
• Meaning When True: Requested
• Meaning When False: Not Requested
6.4.4.8  CountryOfIssue <CtryOfIsse>
Presence: [1..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.010.001.01 SecurityQueryV01
Target2-Securities - Securities Reference Data 90 March 2024
```


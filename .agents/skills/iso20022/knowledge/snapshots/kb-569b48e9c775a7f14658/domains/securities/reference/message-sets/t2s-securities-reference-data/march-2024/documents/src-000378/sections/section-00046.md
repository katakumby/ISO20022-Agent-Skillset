---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["6 reda.010.001.01 SecurityQueryV01", "6.4 Message Building Blocks", "6.4.3 SearchCriteria <SchCrit>", "6.4.3.4 IssueDate <IsseDt>", "6.4.3.4.5 NotEqualDate <NEQDt>"]
file_pages: [86]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.010.001.01"]
---

# 6.4.3.4.5 NotEqualDate <NEQDt>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 86 to 86.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 86

```text
6.4.3.4.5  NotEqualDate <NEQDt>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODate" on page 529
6.4.3.5  IssueCurrency <IsseCcy>
Presence: [0..1]
Definition: Currency in which a security is issued or redenominated.
Impacted by: C1 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 508
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
6.4.3.6  CountryOfIssue <CtryOfIsse>
Presence: [0..1]
Definition: Primary market or country where a security is issued by the issuer or its agent.
Impacted by: C3 "Country"
Datatype: "CountryCode" on page 513
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
6.4.3.7  SecurityStatus <SctySts>
Presence: [0..1]
Definition: Specifies the status of the security within its lifecycle.
SecurityStatus <SctySts> contains one of the following SecurityStatus3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 86
Or}   Proprietary <Prtry> [1..1] ± 87
6.4.3.7.1  Code <Cd>
Presence: [1..1]
Definition: Security status expressed as an ISO 20022 code.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.010.001.01 SecurityQueryV01
Target2-Securities - Securities Reference Data 86 March 2024
```


---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["2 acmt.025.001.02 AccountQueryListV02", "2.4 Message Building Blocks", "2.4.4 Organisation <Org>", "2.4.4.3 CountryOfOperation <CtryOfOpr>"]
file_pages: [15]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.025.001.02"]
---

# 2.4.4.3 CountryOfOperation <CtryOfOpr>

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 15 to 15.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 15

```text
2.4.4.3  CountryOfOperation <CtryOfOpr>
Presence: [1..1]
Definition: Country in which the organisation has its business activity.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 174
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
2.4.4.4  RegistrationDate <RegnDt>
Presence: [0..1]
Definition: Date at which a given organisation was officially registered.
Datatype: "ISODate" on page 179
2.4.4.5  OperationalAddress <OprlAdr>
Presence: [0..1]
Definition: Specifies an operational address, for example, of a shared services centre.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.025.001.02 AccountQueryListV02
Target2-Securities - Cash Account Query and Report 15 August 2026
```


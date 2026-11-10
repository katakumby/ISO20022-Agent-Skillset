---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.2 CommonFinancialInstrumentAttributes12", "13.1.6.2.43 RedemptionPaymentCurrency <RedPmtCcy>"]
file_pages: [288]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.2.43 RedemptionPaymentCurrency <RedPmtCcy>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 288 to 288.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 288

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 478 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
13.1.6.2.43  RedemptionPaymentCurrency <RedPmtCcy>
Presence: [0..1]
Definition: ISO currency for the payment of the cash proceeds.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 507
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
13.1.6.2.44  Restriction <Rstrctn>
Presence: [0..*]
Definition: Regulatory restriction(s) linked to the security.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 288 March 2024
```


---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.8 NonDomicileCountry <NonDmclCtry>"]
file_pages: [434]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.8 NonDomicileCountry <NonDmclCtry>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 434 to 434.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 434

```text
CertificationBreakdownType <CertfctnBrkdwnTp> contains one of the following elements (see
"BeneficiaryCertificationType13Choice" on page 999 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 999
Or}   Proprietary <Prtry> [1..1] ± 1000
7.4.13.8  NonDomicileCountry <NonDmclCtry>
Presence: [0..*]
Definition: Holder of the security has to certify, in line with the terms of the corporate action, that it is not
domiciled in the country indicated.
Impacted by: C13 "Country"
Datatype: "CountryCode" on page 1205
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
7.4.13.9  ValidDomicileCountry <VldDmclCtry>
Presence: [0..*]
Definition: Country of domicile in which the Corporate Action option is valid. The holder of the security
has to certify that it is domiciled in the country indicated.
Impacted by: C13 "Country"
Datatype: "CountryCode" on page 1205
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
7.4.13.10  CurrencyOption <CcyOptn>
Presence: [0..1]
Definition: Currency in which cash proceeds are to be credited or debited.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 1157
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 434 February 2026
```


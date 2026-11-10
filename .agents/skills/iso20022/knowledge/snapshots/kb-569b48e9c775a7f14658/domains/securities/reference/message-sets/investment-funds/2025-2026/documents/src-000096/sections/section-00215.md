---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.8 SecurityIdentification <SctyId>", "15.4.5.8.7 ClassificationType <ClssfctnTp>"]
file_pages: [315]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.8.7 ClassificationType <ClssfctnTp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 315 to 315.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 315

```text
• Meaning When True: Yes
• Meaning When False: No
15.4.5.8.7  ClassificationType <ClssfctnTp>
Presence: [0..1]
Definition: Classification type of the financial instrument, as per the ISO Classification of Financial
Instrument (CFI) codification, for example, common share with voting rights, fully paid, or registered.
ClassificationType <ClssfctnTp> contains one of the following elements (see
"SecurityClassificationType2Choice" on page 4855 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CFI <CFI> [1..1] IdentifierSet 4855
Or}   AlternateClassification <AltrnClssfctn> [1..1] ± 4855
15.4.5.8.8  BaseCurrency <BaseCcy>
Presence: [0..1]
Definition: Currency of the investment fund class.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 5275
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
15.4.5.8.9  CountryOfDomicile <CtryOfDmcl>
Presence: [0..1]
Definition: Country where the fund has legal domicile.
Impacted by: C6 "Country"
Datatype: "CountryCode" on page 5290
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
15.4.5.8.10  RegisteredDistributionCountry <RegdDstrbtnCtry>
Presence: [0..*]
Definition: Country where the fund is registered for distribution.
Impacted by: C6 "Country"
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 315 May 2026
```


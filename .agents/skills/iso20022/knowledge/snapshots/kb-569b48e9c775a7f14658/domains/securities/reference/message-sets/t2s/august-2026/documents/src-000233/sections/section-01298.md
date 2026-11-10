---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.2 FinancialInstrumentType <FinInstrmTp>", "32.4.3.1.1.2.3 Debt <Debt>", "32.4.3.1.1.2.3.33 CapitalisedInterest <CptlsdIntrst>", "32.4.3.1.1.2.3.33.1 Code <Cd>"]
file_pages: [1886]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.2.3.33.1 Code <Cd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1886 to 1886.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1886

```text
CapitalisedInterest <CptlsdIntrst> contains one of the following DistributionPolicy2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1886
Or}   Proprietary <Prtry> [1..1] ± 1886
32.4.3.1.1.2.3.33.1  Code <Cd>
Presence: [1..1]
Definition: Distribution policy expressed as an ISO 20022 code.
Datatype: "DistributionPolicy1Code" on page 3236
CodeName Name Definition
DIST Distribution Income is distributed to the investors in
the fund.
ACCU Accumulation Income is added to the capital of the
fund.
32.4.3.1.1.2.3.33.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Distribution policy expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
32.4.3.1.1.2.3.34  ActualDenominationAmount <ActlDnmtnAmt>
Presence: [0..*]
Definition: Nominal value per security unit.
Impacted by: C1 "ActiveCurrency", C5 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 3209
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1886 August 2026
```


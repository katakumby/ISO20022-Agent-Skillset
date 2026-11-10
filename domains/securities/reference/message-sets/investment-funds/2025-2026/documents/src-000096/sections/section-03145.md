---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.6 AggregateBalanceInformation4", "66.1.5.6.11 FinancialInstrumentDetails <FinInstrmDtls>"]
file_pages: [4374]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.6.11 FinancialInstrumentDetails <FinInstrmDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4374 to 4374.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4374

```text
Definition: Place where the securities are safe-kept, physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository (CSD) or an International Central Securities
Depository (ICSD).
SafekeepingPlace <SfkpgPlc> contains one of the following elements (see
"SafekeepingPlaceFormatChoice" on page 5133 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  C13 5133
     PlaceSafekeeping <PlcSfkpg> [1..1] CodeSet 5134
     Narrative <Nrrtv> [0..1] Text 5134
     Party <Pty> [0..1] ± 5134
Or   IdentificationAsDSS <IdAsDSS> [1..1] ± 5135
Or}   IdentificationAsCountry <IdAsCtry> [1..1] CodeSet C12 5135
66.1.5.6.11  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [1..1]
Definition: Security held on the account for which the balance is calculated.
Impacted by: C12 "FinancialInstrumentIdentificationGuideline"
FinancialInstrumentDetails <FinInstrmDtls> contains the following elements (see
"FinancialInstrument13" on page 4517 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 4517
   Name <Nm> [0..1] Text 4518
   SupplementaryIdentification <SplmtryId> [0..1] Text 4518
   ClassType <ClssTp> [0..1] Text 4518
   SecuritiesForm <SctiesForm> [0..1] CodeSet 4519
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4519
Constraints
• FinancialInstrumentIdentificationGuideline
It is recommended that ISIN be used in Identification\SecurityIdentification3Choice.
66.1.5.6.12  PriceDetails <PricDtls>
Presence: [0..*]
Definition: Price of the financial instrument in one or more currencies.
Impacted by: C15 "ValueRule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4374 May 2026
```


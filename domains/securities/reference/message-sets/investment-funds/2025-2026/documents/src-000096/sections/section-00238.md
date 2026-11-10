---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.21 LocalMarketAnnex <LclMktAnx>", "15.4.5.21.6 CashSettlementDetails <CshSttlmDtls>", "15.4.5.21.6.1 Currency <Ccy>"]
file_pages: [341]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.21.6.1 Currency <Ccy>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 341 to 341.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 341

```text
Definition: Account to be used for cash settlement.
CashSettlementDetails <CshSttlmDtls> contains the following CashAccount205 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Currency <Ccy> [0..1] CodeSet C1 341
   PrimaryAccount <PmryAcct> [0..1]  341
     AccountIdentification <AcctId> [1..1]  342
       Identification <Id> [1..1] ± 342
       Name <Nm> [0..1] Text 342
     Servicer <Svcr> [0..1] IdentifierSet C2 342
     AccountTypeDescription <AcctTpDesc> [0..1] Text 343
   SecondaryAccount <ScndryAcct> [0..1]  343
     AccountIdentification <AcctId> [1..1]  343
       Identification <Id> [1..1] ± 343
       Name <Nm> [0..1] Text 344
     Servicer <Svcr> [0..1] IdentifierSet C2 344
     AccountTypeDescription <AcctTpDesc> [0..1] Text 344
15.4.5.21.6.1  Currency <Ccy>
Presence: [0..1]
Definition: Currency of the settlement.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 5275
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
15.4.5.21.6.2  PrimaryAccount <PmryAcct>
Presence: [0..1]
Definition: Cash account for settlement.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 341 May 2026
```


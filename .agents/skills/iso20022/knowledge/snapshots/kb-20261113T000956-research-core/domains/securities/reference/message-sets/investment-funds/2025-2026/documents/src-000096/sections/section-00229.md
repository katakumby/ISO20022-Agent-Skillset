---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.20 CashSettlementDetails <CshSttlmDtls>"]
file_pages: [331]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.20 CashSettlementDetails <CshSttlmDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 331 to 331.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 331

```text
15.4.5.20  CashSettlementDetails <CshSttlmDtls>
Presence: [0..*]
Definition: Account to be used for cash settlement.
CashSettlementDetails <CshSttlmDtls> contains the following CashAccount205 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Currency <Ccy> [0..1] CodeSet C1 331
   PrimaryAccount <PmryAcct> [0..1]  331
     AccountIdentification <AcctId> [1..1]  332
       Identification <Id> [1..1] ± 332
       Name <Nm> [0..1] Text 332
     Servicer <Svcr> [0..1] IdentifierSet C2 332
     AccountTypeDescription <AcctTpDesc> [0..1] Text 333
   SecondaryAccount <ScndryAcct> [0..1]  333
     AccountIdentification <AcctId> [1..1]  333
       Identification <Id> [1..1] ± 333
       Name <Nm> [0..1] Text 334
     Servicer <Svcr> [0..1] IdentifierSet C2 334
     AccountTypeDescription <AcctTpDesc> [0..1] Text 334
15.4.5.20.1  Currency <Ccy>
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
15.4.5.20.2  PrimaryAccount <PmryAcct>
Presence: [0..1]
Definition: Cash account for settlement.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 331 May 2026
```


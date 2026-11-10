---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.5 Financial Instrument", "22.1.5.2 CreditDefaultSwapSingleName2"]
file_pages: [325]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.5.2 CreditDefaultSwapSingleName2

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 325 to 325.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 325

```text
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
22.1.5.2  CreditDefaultSwapSingleName2
Definition: Credit default swap derivative specific for reporting on a single name credit default swap.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SovereignIssuer <SvrgnIssr> [1..1] Indicator 325
   ReferenceParty <RefPty> [0..1] ± 325
   NotionalCurrency <NtnlCcy> [1..1] CodeSet C2 325
22.1.5.2.1  SovereignIssuer <SvrgnIssr>
Presence: [1..1]
Definition: Reference entity of a single name credit default swap (CDS) or a derivative on single name
CDS.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 451):
• Meaning When True: True
• Meaning When False: False
22.1.5.2.2  ReferenceParty <RefPty>
Presence: [0..1]
Definition: Reference entity of a single name credit default swap (CDS) or a derivative on single name
credit default swap (CDS).
ReferenceParty <RefPty> contains one of the following elements (see
"DerivativePartyIdentification1Choice" on page 341 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Country <Ctry> [1..1] CodeSet C4 342
Or   CountrySubDivision <CtrySubDvsn> [1..1] CodeSet 342
Or}   LEI <LEI> [1..1] IdentifierSet 342
22.1.5.2.3  NotionalCurrency <NtnlCcy>
Presence: [1..1]
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
325 July 2025
```


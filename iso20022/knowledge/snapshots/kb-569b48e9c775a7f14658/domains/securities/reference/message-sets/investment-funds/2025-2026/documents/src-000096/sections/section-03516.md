---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.18 Crystallisation2"]
file_pages: [4766]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.18 Crystallisation2

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4766 to 4766.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4766

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
66.1.26.18  Crystallisation2
Definition: Number of crystallised units.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TrancheIdentification <TrchId> [1..1] Text 4766
   CrystallisedUnitsNumber <CrstllsdUnitsNb> [0..1] Quantity 4766
   UncrystallisedUnitsNumber <UcrstllsdUnitsNb> [0..1] Quantity 4766
   CrystallisedAmount <CrstllsdAmt> [0..1] Amount C1 4766
   UncrystallisedAmount <UcrstllsdAmt> [0..1] Amount C1 4767
   AdditionalInformation <AddtlInf> [0..*] ± 4767
66.1.26.18.1  TrancheIdentification <TrchId>
Presence: [1..1]
Definition: Identification of the tranche.
Datatype: "Max35Text" on page 5403
66.1.26.18.2  CrystallisedUnitsNumber <CrstllsdUnitsNb>
Presence: [0..1]
Definition: Number of units crystallised.
Datatype: "DecimalNumber" on page 5400
66.1.26.18.3  UncrystallisedUnitsNumber <UcrstllsdUnitsNb>
Presence: [0..1]
Definition: Number of units uncrystallised.
Datatype: "DecimalNumber" on page 5400
66.1.26.18.4  CrystallisedAmount <CrstllsdAmt>
Presence: [0..1]
Definition: Sum representing the crystallised amount.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 5268
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4766 May 2026
```


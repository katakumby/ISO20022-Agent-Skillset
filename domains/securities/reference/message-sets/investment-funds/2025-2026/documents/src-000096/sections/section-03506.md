---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.15 ProcessingCharacteristics11", "66.1.26.15.1 DealingCurrencyAccepted <DealgCcyAccptd>"]
file_pages: [4756]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.15.1 DealingCurrencyAccepted <DealgCcyAccptd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4756 to 4756.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4756

```text
Constraints
• DealingCutOffTimeFrameRule
If DealingCutOffTimeFrame is present, then DealingCutOffTimeFrame/OtherTimeFrameDescription
or DealingCutOffTimeFrame/ReferToOrderDesk or DealingCutOffTimeFrame/TradeMinus must be
present.
On Condition
    /DealingCutOffTimeFrame is present
Following Must be True
    /DealingCutOffTimeFrame/OtherTimeFrameDescription Must be present
 Or    /DealingCutOffTimeFrame/TradeMinus Must be present
 Or    /DealingCutOffTimeFrame/ReferToOrderDesk Must be present
66.1.26.15.1  DealingCurrencyAccepted <DealgCcyAccptd>
Presence: [0..*]
Definition: Currency in which a subscription is accepted.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 5275
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
66.1.26.15.2  InitialInvestmentApplication <InitlInvstmtAppl>
Presence: [0..1]
Definition: Specifies whether an application form is required for the initial investment.
InitialInvestmentApplication <InitlInvstmtAppl> contains the following Forms1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ApplicationForm <ApplForm> [1..1] Indicator 4756
   SignatureType <SgntrTp> [1..1] CodeSet 4756
66.1.26.15.2.1  ApplicationForm <ApplForm>
Presence: [1..1]
Definition: Indicates whether a physical application form is required.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.26.15.2.2  SignatureType <SgntrTp>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4756 May 2026
```


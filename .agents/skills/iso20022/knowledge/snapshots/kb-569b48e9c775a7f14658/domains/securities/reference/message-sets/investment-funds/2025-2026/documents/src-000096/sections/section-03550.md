---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.32 BenefitCrystallisationEvent2", "66.1.26.32.4 CrystallisationAmount <CrstllstnAmt>"]
file_pages: [4800]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.32.4 CrystallisationAmount <CrstllstnAmt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4800 to 4800.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4800

```text
66.1.26.32.4  CrystallisationAmount <CrstllstnAmt>
Presence: [0..1]
Definition: Amount of the crystallisation event.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
66.1.26.32.5  PercentageOfAllowance <PctgOfAllwnc>
Presence: [0..1]
Definition: Percentage of allowance used for the benefit crystallisation event.
Datatype: "PercentageRate" on page 5401
66.1.26.32.6  LifetimeAllowanceProtection <LftmAllwncPrtcn>
Presence: [0..1]
Definition: Indicates whether lifetime allowance protection impacts the benefit crystallisation event.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.26.32.7  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the benefit crystallisation event.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
66.1.26.33  ProcessingCharacteristics10
Definition: Processing characteristics linked to a redemption from an investment fund or alternative/
hedge fund.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4800 May 2026
```


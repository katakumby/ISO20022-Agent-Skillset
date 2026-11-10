---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.20 OtherDistributionStrategy1", "66.1.26.20.2 Target <Trgt>"]
file_pages: [4774]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.20.2 Target <Trgt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4774 to 4774.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4774

```text
66.1.26.20.2  Target <Trgt>
Presence: [0..1]
Definition: Choice of formats for the specification of whether the product is aimed at the type of return
profile.
Target <Trgt> contains one of the following elements (see "DistributionStrategy1Choice" on page 4781
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4781
Or}   Proprietary <Prtry> [1..1] ± 4781
66.1.26.20.3  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about the target market and the investor's risk tolerance.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
66.1.26.21  AdditionalAmount1Choice
Definition: Choice between additional cash in or resulting cash out.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AdditionalCashIn <AddtlCshIn> [1..1] Amount C2, C10 4774
Or}   ResultingCashOut <RsltgCshOut> [1..1] Amount C2, C10 4775
66.1.26.21.1  AdditionalCashIn <AddtlCshIn>
Presence: [1..1]
Definition: Additional amount of money paid by the investor in addition to the switch redemption amount.
Impacted by: C2 "ActiveOrHistoricCurrency", C10 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 5269
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4774 May 2026
```


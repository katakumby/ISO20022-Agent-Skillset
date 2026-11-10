---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.5 Portfolio <Prtfl>", "40.4.15.5.1 TaxEfficientProduct <TaxEffcntPdct>", "40.4.15.5.1.9 BonusOrWithdrawal <BnsOrWdrwl>", "40.4.15.5.1.9.3 Reason <Rsn>"]
file_pages: [1544]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.5.1.9.3 Reason <Rsn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1544 to 1544.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1544

```text
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
40.4.15.5.1.9.3  Reason <Rsn>
Presence: [0..1]
Definition: Reason for the bonus amount paid to or an amount withdrawn from the investment product.
Reason <Rsn> contains one of the following WithdrawalReason1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1544
Or}   Proprietary <Prtry> [1..1] ± 1544
40.4.15.5.1.9.3.1  Code <Cd>
Presence: [1..1]
Definition: Withdrawal reason expressed as a code.
Datatype: "PortfolioWithdrawalReason1Code" on page 5343
CodeName Name Definition
FTRS FirstTimeResidentialProperty Withdrawal is for a first time residential
property.
40.4.15.5.1.9.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Withdrawal reason expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
40.4.15.5.1.9.4  UnclaimedAmount <UclmdAmt>
Presence: [0..1]
Definition: Amount of an unclaimed bonus or an unclaimed withdrawal.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyAnd13DecimalAmount" on page 5269
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1544 May 2026
```


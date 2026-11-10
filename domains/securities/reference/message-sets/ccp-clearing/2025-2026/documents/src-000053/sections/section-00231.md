---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["10 MX secl.009.001.03 BuyInConfirmationV03", "10.4 Message Building Blocks", "10.4.3 BuyInDetails <BuyInDtls>", "10.4.3.5 SecuritiesBuyIn <SctiesBuyIn>", "10.4.3.5.3 Fees <Fees>"]
file_pages: [302]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.009.001.03"]
---

# 10.4.3.5.3 Fees <Fees>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 302 to 302.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 302

```text
10.4.3.5.3  Fees <Fees>
Presence: [0..1]
Definition: Amount of money related to the fees for the securities compensation.
Fees <Fees> contains the following elements (see AmountAndDirection20 on page 378 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount   'C2,
  'C6
378
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 379
10.4.3.6  RequiredCashCompensation <ReqrdCshCompstn>
Presence: [0..1]
Definition: Provides details about the cash compensation required, in case the central counterparty
could not buy the securities to cover the trade(s) that failed.
RequiredCashCompensation <ReqrdCshCompstn> contains the following CashCompensation1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementAmount <SttlmAmt> [1..1] ± 302
   Fees <Fees> [0..1] ± 302
   ValueDate <ValDt> [0..1] Date 303
10.4.3.6.1  SettlementAmount <SttlmAmt>
Presence: [1..1]
Definition: Provides the original amount to be settled.
SettlementAmount <SttlmAmt> contains the following elements (see AmountAndDirection20 on
page 378 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount   'C2,
  'C6
378
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 379
10.4.3.6.2  Fees <Fees>
Presence: [0..1]
Definition: Amount of fees linked to the cash compensation process.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.009.001.03 BuyInConfirmationV03
March 2026 302
```


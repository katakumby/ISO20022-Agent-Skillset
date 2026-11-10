---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["10 MX secl.009.001.03 BuyInConfirmationV03", "10.4 Message Building Blocks", "10.4.3 BuyInDetails <BuyInDtls>", "10.4.3.5 SecuritiesBuyIn <SctiesBuyIn>"]
file_pages: [301]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.009.001.03"]
---

# 10.4.3.5 SecuritiesBuyIn <SctiesBuyIn>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 301 to 301.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 301

```text
Price <Pric> contains the following elements (see Price4 on page 465 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 465
   Type <Tp> [0..1] CodeSet 466
10.4.3.5  SecuritiesBuyIn <SctiesBuyIn>
Presence: [0..1]
Definition: Specifies the elements related to the securities that the central counterparty had to buy in the
context of the buy-in process.
SecuritiesBuyIn <SctiesBuyIn> contains the following SecuritiesCompensation1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [1..1] ± 301
   SettlementAmount <SttlmAmt> [1..1] ± 301
   Fees <Fees> [0..1] ± 302
10.4.3.5.1  Depository <Dpstry>
Presence: [1..1]
Definition: Place where settlement of the securities takes place.
Depository <Dpstry> contains one of the following elements (see PartyIdentification34Choice on
page 446 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BIC <BIC> [1..1] IdentifierSet   'C4 446
Or   NameAndAddress <NmAndAdr> [1..1] ± 447
Or}   Country <Ctry> [1..1] CodeSet   'C5 447
10.4.3.5.2  SettlementAmount <SttlmAmt>
Presence: [1..1]
Definition: Provides the total amount of money to be settled.
SettlementAmount <SttlmAmt> contains the following elements (see AmountAndDirection20 on
page 378 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount   'C2,
  'C6
378
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 379
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.009.001.03 BuyInConfirmationV03
March 2026 301
```


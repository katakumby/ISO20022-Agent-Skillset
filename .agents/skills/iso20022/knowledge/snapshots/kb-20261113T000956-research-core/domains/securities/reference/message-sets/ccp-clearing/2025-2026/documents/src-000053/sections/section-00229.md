---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["10 MX secl.009.001.03 BuyInConfirmationV03", "10.4 Message Building Blocks", "10.4.3 BuyInDetails <BuyInDtls>", "10.4.3.1 BuyInNotificationIdentification <BuyInNtfctnId>"]
file_pages: [300]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.009.001.03"]
---

# 10.4.3.1 BuyInNotificationIdentification <BuyInNtfctnId>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 300 to 300.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 300

```text
BuyInDetails <BuyInDtls> contains the following BuyIn2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BuyInNotificationIdentification <BuyInNtfctnId> [0..1] Text 300
   BuyInIdentification <BuyInId> [1..1] Text 300
   Date <Dt> [1..1] Date 300
   Price <Pric> [0..1] ± 300
   SecuritiesBuyIn <SctiesBuyIn> [0..1]  301
     Depository <Dpstry> [1..1] ± 301
     SettlementAmount <SttlmAmt> [1..1] ± 301
     Fees <Fees> [0..1] ± 302
   RequiredCashCompensation <ReqrdCshCompstn> [0..1]  302
     SettlementAmount <SttlmAmt> [1..1] ± 302
     Fees <Fees> [0..1] ± 302
     ValueDate <ValDt> [0..1] Date 303
10.4.3.1  BuyInNotificationIdentification <BuyInNtfctnId>
Presence: [0..1]
Definition: Indicates the reference of the BuyInNotification message.
Datatype: Max35Text on page 493
10.4.3.2  BuyInIdentification <BuyInId>
Presence: [1..1]
Definition: Indicates the reference id of the buy in.
Datatype: Max35Text on page 493
10.4.3.3  Date <Dt>
Presence: [1..1]
Definition: Provides the date at which the buy occured.
Datatype: ISODate on page 487
10.4.3.4  Price <Pric>
Presence: [0..1]
Definition: Provides the price of the buy-in.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.009.001.03 BuyInConfirmationV03
March 2026 300
```


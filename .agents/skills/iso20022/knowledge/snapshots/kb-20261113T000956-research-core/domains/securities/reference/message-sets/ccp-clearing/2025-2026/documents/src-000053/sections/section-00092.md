---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["3 MX secl.002.001.05 TradeLegNotificationCancellationV05", "3.4 Message Building Blocks", "3.4.6 TradeLegDetails <TradLegDtls>", "3.4.6.25 TradeRegistrationOrigin <TradRegnOrgn>"]
file_pages: [116]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.002.001.05"]
---

# 3.4.6.25 TradeRegistrationOrigin <TradRegnOrgn>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 116 to 116.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 116

```text
TradingParty <TradgPty> contains one of the following elements (see PartyIdentification253Choice on
page 453 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BIC <BIC> [1..1] IdentifierSet   'C3 453
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 453
3.4.6.25  TradeRegistrationOrigin <TradRegnOrgn>
Presence: [0..1]
Definition: Indicates in which session the transaction/operation was executed by the final investor or an
intermediary.
Datatype: Max35Text on page 493
3.4.6.26  TradingPartyAccount <TradgPtyAcct>
Presence: [0..1]
Definition: Identifier of the trading participant's account at the trading venue using the venue's coding
system.
TradingPartyAccount <TradgPtyAcct> contains the following elements (see SecuritiesAccount19 on
page 375 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 375
   Type <Tp> [0..1] ± 375
   Name <Nm> [0..1] Text 375
3.4.6.27  TradingCapacity <TradgCpcty>
Presence: [1..1]
Definition: Specifies the role of the trading party in the transaction.
Datatype: TradingCapacity10Code on page 486
CodeName Name Definition
PRIN Principal Trading as Principal.
RISP RisklessPrincipal Trading as a riskless principal, ie, the
order to buy(sell) has been
simultaneously offset by an order to sell
(buy) with another party.
AGEN Agent Trading as Agent on behalf of a
customer.
MIXC Mixed Trading as an agent on behalf of the
customer and as a principal.
3.4.6.28  TradePostingCode <TradPstngCd>
Presence: [0..1]
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 116
```


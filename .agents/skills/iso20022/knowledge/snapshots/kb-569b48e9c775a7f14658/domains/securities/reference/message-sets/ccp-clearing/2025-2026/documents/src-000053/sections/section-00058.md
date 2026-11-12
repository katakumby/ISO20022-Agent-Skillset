---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["3 MX secl.002.001.05 TradeLegNotificationCancellationV05", "3.4 Message Building Blocks", "3.4.5 ClearingDetails <ClrDtls>", "3.4.5.4 TradeCounterpartyIdentification <TradCtrPtyId>", "3.4.5.4.1 TradeCounterpartyMemberIdentification <TradCtrPtyMmbId>"]
file_pages: [80]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.002.001.05"]
---

# 3.4.5.4.1 TradeCounterpartyMemberIdentification <TradCtrPtyMmbId>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 80 to 80.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 80

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       AccountIdentification <AcctId> [0..1] Text 92
       ProcessingIdentification <PrcgId> [0..1] Text 92
       ProcessingDate <PrcgDt> [0..1] ± 92
       SubAccount <SubAcct> [0..1]  92
         Identification <Id> [1..1] ± 93
         Name <Nm> [0..1] Text 93
         Characteristic <Chrtc> [0..1] Text 93
       ContactPerson <CtctPrsn> [0..1] ± 93
     Party2 <Pty2> [0..1]  94
       PartyIdentification <PtyId> [1..1] ± 94
       AccountIdentification <AcctId> [0..1] Text 95
       ProcessingIdentification <PrcgId> [0..1] Text 95
       ProcessingDate <PrcgDt> [0..1] ± 95
       SubAccount <SubAcct> [0..1]  95
         Identification <Id> [1..1] ± 96
         Name <Nm> [0..1] Text 96
         Characteristic <Chrtc> [0..1] Text 96
       ContactPerson <CtctPrsn> [0..1] ± 96
     SecuritiesSettlementSystem <SctiesSttlmSys> [0..1] Text 97
3.4.5.4.1  TradeCounterpartyMemberIdentification <TradCtrPtyMmbId>
Presence: [1..1]
Definition: External identification of the member who is the market counterpart member of the current
trade leg (in case of non guarantee trades, this field allows buyer and seller to identify each other).
TradeCounterpartyMemberIdentification <TradCtrPtyMmbId> contains one of the following
elements (see PartyIdentification253Choice on page 453 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BIC <BIC> [1..1] IdentifierSet   'C3 453
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 453
3.4.5.4.2  TradeCounterpartyClearingMemberIdentification <TradCtrPtyClrMmbId>
Presence: [1..1]
Definition: External identification of the clearing member of the market couterpart member (in case of
non guarantee trades, this field allows buyer and seller to identify each other).
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 80
```


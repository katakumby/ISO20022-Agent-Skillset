---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["2 MX secl.001.001.05 TradeLegNotificationV05", "2.4 Message Building Blocks", "2.4.5 ClearingDetails <ClrDtls>", "2.4.5.4 TradeCounterpartyIdentification <TradCtrPtyId>", "2.4.5.4.1 TradeCounterpartyMemberIdentification <TradCtrPtyMmbId>"]
file_pages: [22]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.001.001.05"]
---

# 2.4.5.4.1 TradeCounterpartyMemberIdentification <TradCtrPtyMmbId>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 22 to 22.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 22

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       AccountIdentification <AcctId> [0..1] Text 34
       ProcessingIdentification <PrcgId> [0..1] Text 34
       ProcessingDate <PrcgDt> [0..1] ± 34
       SubAccount <SubAcct> [0..1]  34
         Identification <Id> [1..1] ± 35
         Name <Nm> [0..1] Text 35
         Characteristic <Chrtc> [0..1] Text 35
       ContactPerson <CtctPrsn> [0..1] ± 35
     Party2 <Pty2> [0..1]  36
       PartyIdentification <PtyId> [1..1] ± 36
       AccountIdentification <AcctId> [0..1] Text 37
       ProcessingIdentification <PrcgId> [0..1] Text 37
       ProcessingDate <PrcgDt> [0..1] ± 37
       SubAccount <SubAcct> [0..1]  37
         Identification <Id> [1..1] ± 38
         Name <Nm> [0..1] Text 38
         Characteristic <Chrtc> [0..1] Text 38
       ContactPerson <CtctPrsn> [0..1] ± 38
     SecuritiesSettlementSystem <SctiesSttlmSys> [0..1] Text 39
2.4.5.4.1  TradeCounterpartyMemberIdentification <TradCtrPtyMmbId>
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
2.4.5.4.2  TradeCounterpartyClearingMemberIdentification <TradCtrPtyClrMmbId>
Presence: [1..1]
Definition: External identification of the clearing member of the market couterpart member (in case of
non guarantee trades, this field allows buyer and seller to identify each other).
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 22
```


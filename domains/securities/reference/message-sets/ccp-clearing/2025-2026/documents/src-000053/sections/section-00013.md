---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["2 MX secl.001.001.05 TradeLegNotificationV05", "2.4 Message Building Blocks", "2.4.5 ClearingDetails <ClrDtls>", "2.4.5.4 TradeCounterpartyIdentification <TradCtrPtyId>", "2.4.5.4.3 DeliveringParties <DlvrgPties>", "2.4.5.4.3.1 Depository <Dpstry>"]
file_pages: [24]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.001.001.05"]
---

# 2.4.5.4.3.1 Depository <Dpstry>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 24 to 24.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 24

```text
DeliveringParties <DlvrgPties> contains the following DeliveringPartiesAndAccount22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [1..1] ± 24
   Party1 <Pty1> [1..1]  25
     PartyIdentification <PtyId> [1..1] ± 25
     AccountIdentification <AcctId> [0..1] Text 26
     ProcessingIdentification <PrcgId> [0..1] Text 26
     ProcessingDate <PrcgDt> [0..1] ± 26
     SubAccount <SubAcct> [0..1]  26
       Identification <Id> [1..1] ± 27
       Name <Nm> [0..1] Text 27
       Characteristic <Chrtc> [0..1] Text 27
     ContactPerson <CtctPrsn> [0..1] ± 27
   Party2 <Pty2> [0..1]  28
     PartyIdentification <PtyId> [1..1] ± 28
     AccountIdentification <AcctId> [0..1] Text 29
     ProcessingIdentification <PrcgId> [0..1] Text 29
     ProcessingDate <PrcgDt> [0..1] ± 29
     SubAccount <SubAcct> [0..1]  29
       Identification <Id> [1..1] ± 30
       Name <Nm> [0..1] Text 30
       Characteristic <Chrtc> [0..1] Text 30
     ContactPerson <CtctPrsn> [0..1] ± 30
   SecuritiesSettlementSystem <SctiesSttlmSys> [0..1] Text 31
Constraints
• DepositoryGuideline
(Rule)
In a receive, the delivering depository is to be understood as the requested depository of the
delivering counterparty.
The field must be populated with the BIC of a national or international CSD. When no CSD exists in a
particular market, the stock exchange BIC will be used.
2.4.5.4.3.1  Depository <Dpstry>
Presence: [1..1]
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 24
```


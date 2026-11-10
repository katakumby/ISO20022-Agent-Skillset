---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["3 MX secl.002.001.05 TradeLegNotificationCancellationV05", "3.4 Message Building Blocks", "3.4.5 ClearingDetails <ClrDtls>", "3.4.5.4 TradeCounterpartyIdentification <TradCtrPtyId>", "3.4.5.4.3 DeliveringParties <DlvrgPties>", "3.4.5.4.3.1 Depository <Dpstry>"]
file_pages: [82]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.002.001.05"]
---

# 3.4.5.4.3.1 Depository <Dpstry>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 82 to 82.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 82

```text
DeliveringParties <DlvrgPties> contains the following DeliveringPartiesAndAccount22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [1..1] ± 82
   Party1 <Pty1> [1..1]  83
     PartyIdentification <PtyId> [1..1] ± 83
     AccountIdentification <AcctId> [0..1] Text 84
     ProcessingIdentification <PrcgId> [0..1] Text 84
     ProcessingDate <PrcgDt> [0..1] ± 84
     SubAccount <SubAcct> [0..1]  84
       Identification <Id> [1..1] ± 85
       Name <Nm> [0..1] Text 85
       Characteristic <Chrtc> [0..1] Text 85
     ContactPerson <CtctPrsn> [0..1] ± 85
   Party2 <Pty2> [0..1]  86
     PartyIdentification <PtyId> [1..1] ± 86
     AccountIdentification <AcctId> [0..1] Text 87
     ProcessingIdentification <PrcgId> [0..1] Text 87
     ProcessingDate <PrcgDt> [0..1] ± 87
     SubAccount <SubAcct> [0..1]  87
       Identification <Id> [1..1] ± 88
       Name <Nm> [0..1] Text 88
       Characteristic <Chrtc> [0..1] Text 88
     ContactPerson <CtctPrsn> [0..1] ± 88
   SecuritiesSettlementSystem <SctiesSttlmSys> [0..1] Text 89
Constraints
• DepositoryGuideline
(Rule)
In a receive, the delivering depository is to be understood as the requested depository of the
delivering counterparty.
The field must be populated with the BIC of a national or international CSD. When no CSD exists in a
particular market, the stock exchange BIC will be used.
3.4.5.4.3.1  Depository <Dpstry>
Presence: [1..1]
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 82
```


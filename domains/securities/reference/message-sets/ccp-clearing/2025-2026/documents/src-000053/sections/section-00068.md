---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["3 MX secl.002.001.05 TradeLegNotificationCancellationV05", "3.4 Message Building Blocks", "3.4.5 ClearingDetails <ClrDtls>", "3.4.5.4 TradeCounterpartyIdentification <TradCtrPtyId>", "3.4.5.4.4 ReceivingParties <RcvgPties>", "3.4.5.4.4.1 Depository <Dpstry>"]
file_pages: [90]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.002.001.05"]
---

# 3.4.5.4.4.1 Depository <Dpstry>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 90 to 90.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 90

```text
ReceivingParties <RcvgPties> contains the following ReceivingPartiesAndAccount22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [1..1] ± 90
   Party1 <Pty1> [1..1]  91
     PartyIdentification <PtyId> [1..1] ± 91
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
Constraints
• DepositoryGuideline
(Rule)
In a delivery, the receiving depository is to be understood as the requested depository of the
receiving counterparty.
The field must be populated with the BIC of a national or international CSD. When no CSD exists in a
particular market, the stock exchange BIC will be used.
3.4.5.4.4.1  Depository <Dpstry>
Presence: [1..1]
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 90
```


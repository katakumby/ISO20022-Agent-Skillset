---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["2 MX secl.001.001.05 TradeLegNotificationV05", "2.4 Message Building Blocks", "2.4.5 ClearingDetails <ClrDtls>", "2.4.5.4 TradeCounterpartyIdentification <TradCtrPtyId>", "2.4.5.4.4 ReceivingParties <RcvgPties>", "2.4.5.4.4.1 Depository <Dpstry>"]
file_pages: [32]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.001.001.05"]
---

# 2.4.5.4.4.1 Depository <Dpstry>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 32 to 32.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 32

```text
ReceivingParties <RcvgPties> contains the following ReceivingPartiesAndAccount22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [1..1] ± 32
   Party1 <Pty1> [1..1]  33
     PartyIdentification <PtyId> [1..1] ± 33
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
Constraints
• DepositoryGuideline
(Rule)
In a delivery, the receiving depository is to be understood as the requested depository of the
receiving counterparty.
The field must be populated with the BIC of a national or international CSD. When no CSD exists in a
particular market, the stock exchange BIC will be used.
2.4.5.4.4.1  Depository <Dpstry>
Presence: [1..1]
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 32
```


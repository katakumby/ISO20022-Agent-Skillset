---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["3 MX secl.002.001.05 TradeLegNotificationCancellationV05", "3.4 Message Building Blocks", "3.4.5 ClearingDetails <ClrDtls>", "3.4.5.1 SettlementNettingEligibleCode <SttlmNetgElgblCd>"]
file_pages: [77]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.002.001.05"]
---

# 3.4.5.1 SettlementNettingEligibleCode <SttlmNetgElgblCd>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 77 to 77.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 77

```text
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
3.4.5.1  SettlementNettingEligibleCode <SttlmNetgElgblCd>
Presence: [1..1]
Definition: Indicates to the clearing member whether the trade is eligible for settlement netting or not.
Datatype: NettingEligible1Code on page 480
CodeName Name Definition
GROS Gross Indicates that the trade is not eligible for
settlement netting.
NETT Nett Indicates that the trade is eligible for
settlement netting.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 77
```


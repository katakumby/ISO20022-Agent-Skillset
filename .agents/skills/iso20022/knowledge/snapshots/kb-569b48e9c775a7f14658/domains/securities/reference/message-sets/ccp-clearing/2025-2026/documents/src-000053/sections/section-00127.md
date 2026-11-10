---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["4 MX secl.003.001.05 TradeLegStatementV05", "4.4 Message Building Blocks", "4.4.5 StatementDetails <StmtDtls>", "4.4.5.4 TradeLegsDetails <TradLegsDtls>", "4.4.5.4.33 ClearingDetails <ClrDtls>", "4.4.5.4.33.1 SettlementNettingEligibleCode <SttlmNetgElgblCd>"]
file_pages: [169]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.003.001.05"]
---

# 4.4.5.4.33.1 SettlementNettingEligibleCode <SttlmNetgElgblCd>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 169 to 169.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 169

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       Depository <Dpstry> [1..1] ± 182
       Party1 <Pty1> [1..1]  183
         PartyIdentification <PtyId> [1..1] ± 183
         AccountIdentification <AcctId> [0..1] Text 184
         ProcessingIdentification <PrcgId> [0..1] Text 184
         ProcessingDate <PrcgDt> [0..1] ± 184
         SubAccount <SubAcct> [0..1]  184
           Identification <Id> [1..1] ± 185
           Name <Nm> [0..1] Text 185
           Characteristic <Chrtc> [0..1] Text 185
         ContactPerson <CtctPrsn> [0..1] ± 185
       Party2 <Pty2> [0..1]  186
         PartyIdentification <PtyId> [1..1] ± 186
         AccountIdentification <AcctId> [0..1] Text 187
         ProcessingIdentification <PrcgId> [0..1] Text 187
         ProcessingDate <PrcgDt> [0..1] ± 187
         SubAccount <SubAcct> [0..1]  187
           Identification <Id> [1..1] ± 188
           Name <Nm> [0..1] Text 188
           Characteristic <Chrtc> [0..1] Text 188
         ContactPerson <CtctPrsn> [0..1] ± 188
       SecuritiesSettlementSystem <SctiesSttlmSys> [0..1] Text 189
4.4.5.4.33.1  SettlementNettingEligibleCode <SttlmNetgElgblCd>
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
MX secl.003.001.05 TradeLegStatementV05
March 2026 169
```


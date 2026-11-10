---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["4 MX secl.003.001.05 TradeLegStatementV05", "4.4 Message Building Blocks", "4.4.5 StatementDetails <StmtDtls>", "4.4.5.4 TradeLegsDetails <TradLegsDtls>", "4.4.5.4.33 ClearingDetails <ClrDtls>", "4.4.5.4.33.4 TradeCounterpartyIdentification <TradCtrPtyId>", "4.4.5.4.33.4.4 ReceivingParties <RcvgPties>", "4.4.5.4.33.4.4.1 Depository <Dpstry>"]
file_pages: [182]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.003.001.05"]
---

# 4.4.5.4.33.4.4.1 Depository <Dpstry>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 182 to 182.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 182

```text
ReceivingParties <RcvgPties> contains the following ReceivingPartiesAndAccount22 elements
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
Constraints
• DepositoryGuideline
(Rule)
In a delivery, the receiving depository is to be understood as the requested depository of the
receiving counterparty.
The field must be populated with the BIC of a national or international CSD. When no CSD exists in a
particular market, the stock exchange BIC will be used.
4.4.5.4.33.4.4.1  Depository <Dpstry>
Presence: [1..1]
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.003.001.05 TradeLegStatementV05
March 2026 182
```


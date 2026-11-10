---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["11 MX secl.010.001.04 SettlementObligationReportV04", "11.4 Message Building Blocks", "11.4.7 SettlementParties <SttlmPties>", "11.4.7.2 ReceivingSettlementParties <RcvgSttlmPties>", "11.4.7.2.4 SecuritiesSettlementSystem <SctiesSttlmSys>"]
file_pages: [372]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.010.001.04"]
---

# 11.4.7.2.4 SecuritiesSettlementSystem <SctiesSttlmSys>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 372 to 372.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 372

```text
Party2 <Pty2> contains the following elements (see PartyIdentificationAndAccount228 on page 441 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PartyIdentification <PtyId> [1..1] ± 442
   AccountIdentification <AcctId> [0..1] Text 442
   ProcessingIdentification <PrcgId> [0..1] Text 442
   ProcessingDate <PrcgDt> [0..1] ± 442
   SubAccountDetails <SubAcctDtls> [0..1]  443
     Identification <Id> [1..1] ± 443
     Name <Nm> [0..1] Text 443
     Characteristic <Chrtc> [0..1] Text 443
   ContactPerson <CtctPrsn> [0..1] ± 444
11.4.7.2.4  SecuritiesSettlementSystem <SctiesSttlmSys>
Presence: [0..1]
Definition: Identifies the securities settlement system to be used.
Datatype: Max35Text on page 493
11.4.8 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Impacted by: C18 SupplementaryDataRule
SupplementaryData <SplmtryData> contains the following elements (see SupplementaryData1 on
page 440 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 441
   Envelope <Envlp> [1..1] (External Schema) 441
Constraints
• SupplementaryDataRule
(Rule)
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 372
```


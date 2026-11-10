---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["11 MX secl.010.001.04 SettlementObligationReportV04", "11.4 Message Building Blocks", "11.4.6 ReportDetails <RptDtls>", "11.4.6.2 SettlementObligationDetails <SttlmOblgtnDtls>", "11.4.6.2.14 SettlementParties <SttlmPties>", "11.4.6.2.14.2 ReceivingSettlementParties <RcvgSttlmPties>", "11.4.6.2.14.2.4 SecuritiesSettlementSystem <SctiesSttlmSys>"]
file_pages: [362]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.010.001.04"]
---

# 11.4.6.2.14.2.4 SecuritiesSettlementSystem <SctiesSttlmSys>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 362 to 362.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 362

```text
ContactPerson <CtctPrsn> contains the following elements (see ContactIdentification2 on page 458
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NamePrefix <NmPrfx> [0..1] CodeSet 459
   GivenName <GvnNm> [0..1] Text 459
   Name <Nm> [1..1] Text 459
   PhoneNumber <PhneNb> [0..1] Text 459
   MobileNumber <MobNb> [0..1] Text 459
   FaxNumber <FaxNb> [0..1] Text 459
   EmailAddress <EmailAdr> [0..1] Text 459
11.4.6.2.14.2.4  SecuritiesSettlementSystem <SctiesSttlmSys>
Presence: [0..1]
Definition: Identifies the securities settlement system to be used.
Datatype: Max35Text on page 493
11.4.6.2.15  AdditionalSettlementObligationDetails <AddtlSttlmOblgtnDtls>
Presence: [0..*]
Definition: Provides additional information about the settlement obligation details.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 362
```


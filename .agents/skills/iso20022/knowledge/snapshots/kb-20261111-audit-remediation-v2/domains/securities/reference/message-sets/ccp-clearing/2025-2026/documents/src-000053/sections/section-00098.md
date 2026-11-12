---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["3 MX secl.002.001.05 TradeLegNotificationCancellationV05", "3.4 Message Building Blocks", "3.4.8 CancellationReason <CxlRsn>", "3.4.8.2 Proprietary <Prtry>"]
file_pages: [122, 123]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.002.001.05"]
---

# 3.4.8.2 Proprietary <Prtry>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 122 to 123.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 122

```text
CodeName Name Definition
corporate action related cancellation,
CORP should be used.
OTHR Other Other. See Narrative.
CXLR EndOfLife Transaction is rejected by the executing
party, the rejection is final therefore the
order is cancelled in the system.
BYIY CancelledDueToBuyIn Instruction has been cancelled because
a buy-in has been initiated.
CTHP CancelledByThirdParty Instruction is cancelled by a Third party.
CANZ CancelledSplitPartialSettlement Original transaction has been cancelled
and replaced to allow a partial or split
settlement.
CANT CancelledDueToTransformation Original transaction has been cancelled
and replaced due to a corporate action.
CSUB CancelledByAgent Instruction has been cancelled by the
agent due to an event deadline
extension.
CANS CancelledBySystem Transaction is cancelled by the system.
CANI CancelledByYourself Transaction is cancelled by yourself.
CORP CancelledDueToCorporateAction Transaction has been cancelled due to a
corporate action.
3.4.8.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the related instruction is cancelled, or the related cancellation
request is executed.
Proprietary <Prtry> contains the following elements (see GenericIdentification30 on page 400 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 400
   Issuer <Issr> [1..1] Text 401
   SchemeName <SchmeNm> [0..1] Text 401
3.4.9 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Impacted by: C18 SupplementaryDataRule
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 122
```

## File page 123

```text
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
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 123
```


---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["11 MX secl.010.001.04 SettlementObligationReportV04", "11.4 Message Building Blocks", "11.4.6 ReportDetails <RptDtls>", "11.4.6.2 SettlementObligationDetails <SttlmOblgtnDtls>", "11.4.6.2.1 SettlementObligationIdentification <SttlmOblgtnId>"]
file_pages: [335]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.010.001.04"]
---

# 11.4.6.2.1 SettlementObligationIdentification <SttlmOblgtnId>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 335 to 335.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 335

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}         UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 367
       NetPositionIdentification <NetPosId> [0..1] Text 367
11.4.6.2.1  SettlementObligationIdentification <SttlmOblgtnId>
Presence: [1..1]
Definition: Provides the identification of the settlement obligation.
Datatype: Max35Text on page 493
11.4.6.2.2  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Provides details about the security identification.
Impacted by:   'C12 DescriptionPresenceRule  ', C13 DescriptionUsageRule, C14 ISINGuideline,
  'C15 ISINPresenceRule  ',   'C17 OtherIdentificationPresenceRule  '
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
SecurityIdentification48 on page 391 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 392
   OtherIdentification <OthrId> [0..*]  392
     Identification <Id> [1..1] Text 392
     Suffix <Sfx> [0..1] Text 393
     Type <Tp> [1..1] ± 393
   Description <Desc> [0..1] Text 393
Constraints
• DescriptionPresenceRule
(Rule)
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
Error handling:
– Error severity: Fatal
– Error Code: X00192
– Error Text: At least one identification must be present.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.010.001.04 SettlementObligationReportV04
March 2026 335
```


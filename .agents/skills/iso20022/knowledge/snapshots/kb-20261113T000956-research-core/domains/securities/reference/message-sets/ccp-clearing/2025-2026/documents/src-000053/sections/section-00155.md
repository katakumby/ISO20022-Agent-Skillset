---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["5 MX secl.004.001.04 NetPositionV04", "5.4 Message Building Blocks", "5.4.5 NetPositionReport <NetPosRpt>", "5.4.5.4 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [206]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.004.001.04"]
---

# 5.4.5.4 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 206 to 206.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 206

```text
5.4.5.4  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Provides details about the security identification.
Impacted by:   'C7 DescriptionPresenceRule  ', C8 DescriptionUsageRule, C9 ISINGuideline,
  'C10 ISINPresenceRule  ',   'C14 OtherIdentificationPresenceRule  '
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
• DescriptionUsageRule
(Rule)
Description must be used alone as the last resort.
• ISINGuideline
(Rule)
When a ISIN code exist. It is strongly recommended that the ISIN be used.
• ISINPresenceRule
(Rule)
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.004.001.04 NetPositionV04
March 2026 206
```


---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["2 MX secl.001.001.05 TradeLegNotificationV05", "2.4 Message Building Blocks", "2.4.6 TradeLegDetails <TradLegDtls>", "2.4.6.11 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [45]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.001.001.05"]
---

# 2.4.6.11 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 45 to 45.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 45

```text
Proprietary <Prtry> contains the following elements (see GenericIdentification30 on page 400 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 400
   Issuer <Issr> [1..1] Text 401
   SchemeName <SchmeNm> [0..1] Text 401
2.4.6.11  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Provides details about the security identification.
Impacted by:   'C11 DescriptionPresenceRule  ', C12 DescriptionUsageRule, C13 ISINGuideline,
  'C14 ISINPresenceRule  ',   'C17 OtherIdentificationPresenceRule  '
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
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.001.001.05 TradeLegNotificationV05
March 2026 45
```


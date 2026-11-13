---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.11 Margin Call Calculation", "12.1.11.1 MarginCalculation2", "12.1.11.1.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [409]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.11.1.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 409 to 409.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 409

```text
– Error Text: If Margin Details is present, then at least one of its elements (Initial Margin, Variation
Margin or Other Margin) must be present.
12.1.11.1.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [0..1]
Definition: Provides details about the security identification.
Impacted by:   'C8 DescriptionPresenceRule  ', C9 DescriptionUsageRule, C10 ISINGuideline,
  'C11 ISINPresenceRule  ',   'C12 OtherIdentificationPresenceRule  '
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
SecurityIdentification14 on page 393 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 394
   OtherIdentification <OthrId> [0..*]  395
     Identification <Id> [1..1] Text 395
     Suffix <Sfx> [0..1] Text 395
     Type <Tp> [1..1] ± 395
   Description <Desc> [0..1] Text 395
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
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 409
```


---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.11 Margin Call Calculation", "12.1.11.1 MarginCalculation2", "12.1.11.1.7 MarginTypeAmount <MrgnTpAmt>", "12.1.11.1.7.2 VariationMargin <VartnMrgn>", "12.1.11.1.7.2.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [418, 419]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.11.1.7.2.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 418 to 419.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 418

```text
VariationMargin <VartnMrgn> contains the following VariationMargin3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [0..1] ±   'C8,
C9, C10,
  'C11,
  'C12
418
   TotalVariationMargin <TtlVartnMrgn> [1..*]  420
     ShortLongIndicator <ShrtLngInd> [0..1] CodeSet 420
     AmountDetails <AmtDtls> [1..1]  421
       OriginalCurrencyAmount <OrgnlCcyAmt> [0..1] Amount   'C1,
  'C7
421
       ReportingAmount <RptgAmt> [1..1] Amount 421
   TotalMarkToMarket <TtlMrkToMkt> [1..1]  422
     OriginalCurrencyAmount <OrgnlCcyAmt> [0..1] Amount   'C1,
  'C7
422
     ReportingAmount <RptgAmt> [1..1] Amount 423
   MarkToMarketNetted <MrkToMktNetd> [0..*]  423
     OriginalCurrencyAmount <OrgnlCcyAmt> [0..1] Amount   'C1,
  'C7
423
     ReportingAmount <RptgAmt> [1..1] Amount 424
   MarkToMarketGross <MrkToMktGrss> [0..*]  424
     OriginalCurrencyAmount <OrgnlCcyAmt> [0..1] Amount   'C1,
  'C7
424
     ReportingAmount <RptgAmt> [1..1] Amount 425
   MarkToMarketFails <MrkToMktFls> [0..*]  425
     OriginalCurrencyAmount <OrgnlCcyAmt> [0..1] Amount   'C1,
  'C7
425
     ReportingAmount <RptgAmt> [1..1] Amount 426
   FailsHaircut <FlsHrcut> [0..1]  426
     OriginalCurrencyAmount <OrgnlCcyAmt> [0..1] Amount   'C1,
  'C7
426
     ReportingAmount <RptgAmt> [1..1] Amount 427
12.1.11.1.7.2.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [0..1]
Definition: Provides details about the security identification.
Impacted by:   'C8 DescriptionPresenceRule  ', C9 DescriptionUsageRule, C10 ISINGuideline,
  'C11 ISINPresenceRule  ',   'C12 OtherIdentificationPresenceRule  '
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 418
```

## File page 419

```text
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
• ISINPresenceRule
(Rule)
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 419
```


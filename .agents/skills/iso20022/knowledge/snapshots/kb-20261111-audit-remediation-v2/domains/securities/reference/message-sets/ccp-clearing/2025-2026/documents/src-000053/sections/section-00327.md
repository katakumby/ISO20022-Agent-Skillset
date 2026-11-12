---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.11 Margin Call Calculation", "12.1.11.1 MarginCalculation2", "12.1.11.1.7 MarginTypeAmount <MrgnTpAmt>", "12.1.11.1.7.2 VariationMargin <VartnMrgn>", "12.1.11.1.7.2.2 TotalVariationMargin <TtlVartnMrgn>"]
file_pages: [420]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.11.1.7.2.2 TotalVariationMargin <TtlVartnMrgn>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 420 to 420.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 420

```text
Error handling:
– Error severity: Fatal
– Error Code: X00194
– Error Text: At least one identification must be present.
• OtherIdentificationPresenceRule
(Rule)
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
Error handling:
– Error severity: Fatal
– Error Code: X00193
– Error Text: At least one identification must be present.
12.1.11.1.7.2.2  TotalVariationMargin <TtlVartnMrgn>
Presence: [1..*]
Definition: Margin required to cover the risk because of the price fluctuations occurred on the unsettled
exposures towards the central counterparty.
TotalVariationMargin <TtlVartnMrgn> contains the following TotalVariationMargin1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongIndicator <ShrtLngInd> [0..1] CodeSet 420
   AmountDetails <AmtDtls> [1..1]  421
     OriginalCurrencyAmount <OrgnlCcyAmt> [0..1] Amount   'C1,
  'C7
421
     ReportingAmount <RptgAmt> [1..1] Amount 421
12.1.11.1.7.2.2.1  ShortLongIndicator <ShrtLngInd>
Presence: [0..1]
Definition: Specifies whether the variation margin position is short or long, that is, wether the balance is
a negative or positive balance.
Datatype: ShortLong1Code on page 482
CodeName Name Definition
SHOR Short Position is short, that is, the balance is
negative.
LONG Long Position is long, that is, the balance is
positive.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 420
```


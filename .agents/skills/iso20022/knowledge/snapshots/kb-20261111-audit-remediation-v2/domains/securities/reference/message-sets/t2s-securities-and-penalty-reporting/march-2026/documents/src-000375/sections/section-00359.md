---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.22 Price", "7.1.22.3 PriceType4Choice", "7.1.22.3.2 Indicative <Indctv>"]
file_pages: [446]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.22.3.2 Indicative <Indctv>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 446 to 446.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 446

```text
Definition: Last reported price of a financial instrument in a market, determined by supply and demand.
Market <Mkt> contains the following elements (see "Price7" on page 444 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 444
   Value <Val> [1..1] ± 444
7.1.22.3.2  Indicative <Indctv>
Presence: [1..1]
Definition: Estimated price, for valuation purposes.
Indicative <Indctv> contains the following elements (see "Price7" on page 444 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 444
   Value <Val> [1..1] ± 444
7.1.22.4  TypeOfPrice29Choice
Definition: Choice of format for the type of price.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 446
Or}   Proprietary <Prtry> [1..1] ± 446
7.1.22.4.1  Code <Cd>
Presence: [1..1]
Definition: Type of price expressed as an ISO 20022 code.
Datatype: "TypeOfPrice14Code" on page 548
CodeName Name Definition
AVER Average Price is an average execution price.
7.1.22.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of price expressed as a proprietary code.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 446 March 2026
```


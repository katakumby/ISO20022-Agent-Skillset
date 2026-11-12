---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.12 DistributionStrategy1", "66.1.26.12.3 InvestmentAdvice <InvstmtAdvc>"]
file_pages: [4753]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.12.3 InvestmentAdvice <InvstmtAdvc>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4753 to 4753.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4753

```text
ExecutionWithAppropriatenessTestOrNonAdvisedServices
<ExctnWthApprprtnssTstOrNonAdvsdSvcs> contains one of the following elements (see
"DistributionStrategy1Choice" on page 4781 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4781
Or}   Proprietary <Prtry> [1..1] ± 4781
66.1.26.12.3  InvestmentAdvice <InvstmtAdvc>
Presence: [0..1]
Definition: Specifies to whom the product can be sold if investment advice has been provided. When
used in reference to MiFID, this is in the scope of the European MiFID Template (EMT) reference
06030.
InvestmentAdvice <InvstmtAdvc> contains one of the following elements (see
"DistributionStrategy1Choice" on page 4781 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4781
Or}   Proprietary <Prtry> [1..1] ± 4781
66.1.26.12.4  PortfolioManagement <PrtflMgmt>
Presence: [0..1]
Definition: Specifies to whom the product can be sold if portfolio management has been provided. When
used in reference to MiFID, this is in the scope of the European MiFID Template (EMT) reference
06040.
PortfolioManagement <PrtflMgmt> contains one of the following elements (see
"DistributionStrategy1Choice" on page 4781 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4781
Or}   Proprietary <Prtry> [1..1] ± 4781
66.1.26.12.5  Other <Othr>
Presence: [0..1]
Definition: Other distribution strategy.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4753 May 2026
```


---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.11 ModificationScope41", "66.1.26.11.2 InvestmentPlan <InvstmtPlan>", "66.1.26.11.2.18 InstalmentManagerRole <InstlmtMgrRole>"]
file_pages: [4752]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.11.2.18 InstalmentManagerRole <InstlmtMgrRole>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4752 to 4752.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4752

```text
66.1.26.11.2.18  InstalmentManagerRole <InstlmtMgrRole>
Presence: [0..1]
Definition: Role or function of the instalment manager.
InstalmentManagerRole <InstlmtMgrRole> contains one of the following elements (see
"PartyRole4Choice" on page 4956 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4956
Or}   Proprietary <Prtry> [1..1] ± 4958
66.1.26.12  DistributionStrategy1
Definition: Distribution strategy criteria.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ExecutionOnly <ExctnOnly> [0..1] ± 4752
   ExecutionWithAppropriatenessTestOrNonAdvisedService
s <ExctnWthApprprtnssTstOrNonAdvsdSvcs>
[0..1] ± 4752
   InvestmentAdvice <InvstmtAdvc> [0..1] ± 4753
   PortfolioManagement <PrtflMgmt> [0..1] ± 4753
   Other <Othr> [0..1] ± 4753
66.1.26.12.1  ExecutionOnly <ExctnOnly>
Presence: [0..1]
Definition: Specifies to whom the product can be sold on an execution-only basis. When used in
reference to MiFID, this is in the scope of the European MiFID Template (EMT) reference 06010.
ExecutionOnly <ExctnOnly> contains one of the following elements (see
"DistributionStrategy1Choice" on page 4781 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4781
Or}   Proprietary <Prtry> [1..1] ± 4781
66.1.26.12.2  ExecutionWithAppropriatenessTestOrNonAdvisedServices
<ExctnWthApprprtnssTstOrNonAdvsdSvcs>
Presence: [0..1]
Definition: Specifies to whom the product can be sold with an appropriateness test or to a non-advised
service. When used in reference to MiFID, this is in the scope of the European MiFID Template (EMT)
reference 06020.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4752 May 2026
```


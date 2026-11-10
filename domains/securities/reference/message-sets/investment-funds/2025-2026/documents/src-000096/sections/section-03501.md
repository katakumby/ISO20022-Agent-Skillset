---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.11 ModificationScope41", "66.1.26.11.2 InvestmentPlan <InvstmtPlan>", "66.1.26.11.2.12 ContractReference <CtrctRef>"]
file_pages: [4751]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.11.2.12 ContractReference <CtrctRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4751 to 4751.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4751

```text
66.1.26.11.2.12  ContractReference <CtrctRef>
Presence: [0..1]
Definition: Reference of the underlying investment contract. In some markets, such as Italy, this might
be required to segregate holdings between the same investment account.
Datatype: "Max35Text" on page 5403
66.1.26.11.2.13  RelatedContractReference <RltdCtrctRef>
Presence: [0..1]
Definition: Reference of the previous contract to which this savings or withdrawal plan is related.
Datatype: "Max35Text" on page 5403
66.1.26.11.2.14  ProductIdentification <PdctId>
Presence: [0..1]
Definition: Identification of the product as designated by the fund manager. In some markets, such as
Italy, the financial product or service related to a savings plan or withdrawal plan are identified by a
product identification or number.
Datatype: "Max35Text" on page 5403
66.1.26.11.2.15  SLAChargeAndCommissionReference <SLAChrgAndComssnRef>
Presence: [0..1]
Definition: Reference of the underlying service level agreement (SLA) governing fees.
Datatype: "Max35Text" on page 5403
66.1.26.11.2.16  InsuranceCover <InsrncCover>
Presence: [0..1]
Definition: Specifies the type of insurance contract to which the savings investment plan is linked.
InsuranceCover <InsrncCover> contains one of the following elements (see "InsuranceType2Choice"
on page 4864 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4865
Or}   Proprietary <Prtry> [1..1] ± 4865
66.1.26.11.2.17  PlanStatus <PlanSts>
Presence: [0..1]
Definition: Status of the savings or withdrawal investment plan.
PlanStatus <PlanSts> contains one of the following elements (see "PlanStatus2Choice" on page 5204
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5204
Or}   Proprietary <Prtry> [1..1] ± 5204
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4751 May 2026
```


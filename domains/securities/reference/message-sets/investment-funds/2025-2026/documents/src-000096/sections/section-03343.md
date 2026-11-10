---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.4 InvestmentAccountOwnershipInformation17", "66.1.24.4.3 ModifiedInvestorProfileValidation <ModfdInvstrPrflVldtn>", "66.1.24.4.3.2 InvestorProfileValidation <InvstrPrflVldtn>", "66.1.24.4.3.2.8 NextRevisionDate <NxtRvsnDt>"]
file_pages: [4584]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.4.3.2.8 NextRevisionDate <NxtRvsnDt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4584 to 4584.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4584

```text
CodeName Name Definition
ONDE OnDemand Event takes place on demand.
66.1.24.4.3.2.8  NextRevisionDate <NxtRvsnDt>
Presence: [0..1]
Definition: Specifies the date at which the next certification check will be performed.
Datatype: "ISODate" on page 5388
66.1.24.4.3.2.9  SalaryRange <SlryRg>
Presence: [0..1]
Definition: Limits between which a person's salary is estimated.
Datatype: "Max35Text" on page 5403
66.1.24.4.3.2.10  SourceOfWealth <SrcOfWlth>
Presence: [0..1]
Definition: Indicates the main source of revenue.
Datatype: "Max140Text" on page 5402
66.1.24.4.3.2.11  CustomerConductClassification <CstmrCndctClssfctn>
Presence: [0..1]
Definition: Specifies an assessment of the customer's behaviour at the time of the account opening
application.
CustomerConductClassification <CstmrCndctClssfctn> contains one of the following elements (see
"CustomerConductClassification1Choice" on page 4663 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4663
Or}   Proprietary <Prtry> [1..1] ± 4664
66.1.24.4.3.2.12  RiskLevel <RskLvl>
Presence: [0..1]
Definition: Specifies the customer's money laundering risk.
RiskLevel <RskLvl> contains one of the following elements (see "RiskLevel2Choice" on page 5003 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5003
Or}   Proprietary <Prtry> [1..1] ± 5004
66.1.24.4.3.2.13  KnowYourCustomerCheckType <KnowYourCstmrChckTp>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4584 May 2026
```


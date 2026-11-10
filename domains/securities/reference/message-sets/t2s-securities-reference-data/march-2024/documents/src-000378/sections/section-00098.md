---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset"]
file_pages: [147]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2 Asset

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 147 to 147.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 147

```text
13.1.2 Asset
13.1.2.1  Equity3
Definition: Financial instrument which represents a title of ownership in a company, ie, the shareholder
is entitled to a part of the company's profit - usually by payment of a dividend - and to voting rights, if
any. Each company issues generally different classes of shares, eg, ordinary or common shares, which
have no guaranteed amount of dividend but carry voting rights, or preferred shares, which receive
dividends before ordinary shares but have no voting right.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PreferenceToIncome <PrefToIncm> [1..1]  147
{Or     Code <Cd> [1..1] CodeSet 147
Or}     Proprietary <Prtry> [1..1] ± 148
   MaturityDate <MtrtyDt> [0..1] DateTime 148
   NonPaidAmount <NonPdAmt> [0..1] Amount C1, C5 148
   ParValue <ParVal> [0..1] Amount C1, C5 148
   VotingRightsPerShare <VtngRghtsPerShr> [0..1] Quantity 149
13.1.2.1.1  PreferenceToIncome <PrefToIncm>
Presence: [1..1]
Definition: Indicates the level of priority to claim on income and assets of the company in case of the
payment of dividends and in the event of a bankruptcy, for example, ordinary/common stocks, preferred
stocks, subordinated debt, etc.
PreferenceToIncome <PrefToIncm> contains one of the following PreferenceToIncome5Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 147
Or}   Proprietary <Prtry> [1..1] ± 148
13.1.2.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Preference to income expressed as an ISO 20022 code.
Datatype: "PreferenceToIncome1Code" on page 521
CodeName Name Definition
ORDN Ordinary Indicates an ordinary/common
preference to income.
PFRD Preferred Indicates a preferred claim upon income
and assets.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 147 March 2024
```


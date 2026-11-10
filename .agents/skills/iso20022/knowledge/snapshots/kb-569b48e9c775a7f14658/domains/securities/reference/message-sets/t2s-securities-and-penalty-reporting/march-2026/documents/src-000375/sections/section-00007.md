---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["2 semt.025.001.01 SecuritiesAccountPositionQueryV01", "2.4 Message Building Blocks", "2.4.2 SearchCriteria <SchCrit>", "2.4.2.1 AccountOwner <AcctOwnr>"]
file_pages: [8]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.025.001.01"]
---

# 2.4.2.1 AccountOwner <AcctOwnr>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 8 to 8.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 8

```text
SearchCriteria <SchCrit> contains the following PositionSearchCriteria4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwner <AcctOwnr> [0..1] ± 8
   AccountServicer <AcctSvcr> [0..1] ± 8
   SafekeepingAccount <SfkpgAcct> [0..1] ± 8
   FinancialInstrument <FinInstrm> [0..1] ± C4, C5,
C7, C8,
C9
9
   CountryOfIssue <CtryOfIsse> [0..1] CodeSet C3 10
   SubBalanceType <SubBalTp> [0..1] ± 10
   ReturnZeroPosition <RtrZeroPos> [1..1] Indicator 10
   OtherBusinessParties <OthrBizPties> [0..1]  11
     Investor <Invstr> [0..*] ± C6, C10,
C11
11
2.4.2.1  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "PartyIdentification136" on
page 413 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 414
   LEI <LEI> [0..1] IdentifierSet 414
2.4.2.2  AccountServicer <AcctSvcr>
Presence: [0..1]
Definition: Party that manages the account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and provides
information about the account.
AccountServicer <AcctSvcr> contains the following elements (see "PartyIdentification136" on
page 413 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 414
   LEI <LEI> [0..1] IdentifierSet 414
2.4.2.3  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Approved by the Securities SEG 19 February 2026. semt.025.001.01
SecuritiesAccountPositionQueryV01
Target2-Securities - Securities and Penalty Reporting 8 March 2026
```

